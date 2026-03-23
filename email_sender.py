"""
email_sender.py
Delivers two attachments to the InSync Tech inbox via Resend:
  1. ARIA_Intake_Summary_[Business]_[Date].pdf  — full extracted data report
  2. ARIA_Intake_Form_[Business]_[Date].docx    — populated client intake form
"""

import os
import base64
import httpx
from datetime import datetime

RESEND_API_KEY  = os.environ.get("RESEND_API_KEY", "")
FROM_EMAIL      = os.environ.get("FROM_EMAIL", "intake@insynctech.io")
TO_EMAIL        = os.environ.get("INSYNC_INBOX", "ian@insynctech.io")
RESEND_ENDPOINT = "https://api.resend.com/emails"


async def send_intake_email(
    pdf_bytes: bytes,
    form_bytes: bytes,
    business_name: str,
    fields: dict,
    metadata: dict
) -> dict:
    date_str     = datetime.utcnow().strftime("%B %d, %Y")
    date_file    = datetime.utcnow().strftime("%Y%m%d")
    call_id      = metadata.get("conversation_id", "—")
    duration     = metadata.get("call_duration", 0)
    duration_str = f"{int(duration) // 60}m {int(duration) % 60}s" if duration else "—"
    safe_biz     = business_name.replace(" ", "_").replace("/", "-")

    subject = f"ARIA Intake Complete — {business_name}"

    owner       = fields.get("owner_name", "—")
    biz_type    = fields.get("business_type", "—")
    phone       = fields.get("owner_phone", "—")
    email_addrs = fields.get("report_email_addresses", "—")
    if isinstance(email_addrs, list):
        email_addrs = ", ".join(email_addrs)
    email_addrs = email_addrs or "—"

    agent_name  = fields.get("agent_name", "ARIA")
    tone        = fields.get("tone_preference", "—")
    greeting    = str(fields.get("greeting_script_raw", "—"))
    greeting_preview = greeting[:140] + ("..." if len(greeting) > 140 else "")
    escalation  = fields.get("escalation_number", "—")

    top_calls = fields.get("primary_call_reasons", [])
    top_calls_str = (", ".join(top_calls[:4]) if isinstance(top_calls, list) and top_calls
                     else str(top_calls) if top_calls else "—")

    after_hours   = str(fields.get("after_hours_script", "—"))
    after_preview = after_hours[:100] + ("..." if len(after_hours) > 100 else "")

    services = fields.get("services_list", [])
    if isinstance(services, list) and services:
        svc_names = [s.get("name", str(s)) if isinstance(s, dict) else str(s) for s in services[:5]]
        svc_str   = ", ".join(svc_names)
        if len(services) > 5:
            svc_str += f" (+{len(services)-5} more)"
    else:
        svc_str = "—"

    wishlist = fields.get("wishlist_features", [])
    wishlist_str = (", ".join(wishlist[:4]) if isinstance(wishlist, list) and wishlist
                    else str(wishlist) if wishlist else "—")

    html_body = f"""
<html>
<body style="font-family:Arial,sans-serif;color:#404040;max-width:700px;margin:0 auto;padding:0;">
  <div style="background:#1A3D6B;padding:22px 30px;border-radius:6px 6px 0 0;">
    <h2 style="color:white;margin:0;font-size:20px;">ARIA INTAKE COMPLETE</h2>
    <p style="color:#A8C4E8;margin:5px 0 0;font-size:13px;">InSync Tech — New Client Onboarding</p>
  </div>
  <div style="background:#F0F4FA;padding:16px 30px;border-left:4px solid #2E75B6;">
    <table style="width:100%;font-size:13px;border-collapse:collapse;">
      <tr><td style="color:#666;width:170px;padding:4px 0;font-weight:bold;">Business</td>
          <td style="color:#1A3D6B;font-weight:bold;font-size:14px;">{business_name}</td></tr>
      <tr><td style="color:#666;padding:3px 0;font-weight:bold;">Owner</td><td>{owner}</td></tr>
      <tr><td style="color:#666;padding:3px 0;font-weight:bold;">Type</td><td>{biz_type}</td></tr>
      <tr><td style="color:#666;padding:3px 0;font-weight:bold;">Phone</td><td>{phone}</td></tr>
      <tr><td style="color:#666;padding:3px 0;font-weight:bold;">Report Email</td><td>{email_addrs}</td></tr>
      <tr><td style="color:#666;padding:3px 0;font-weight:bold;">Interview Date</td><td>{date_str}</td></tr>
      <tr><td style="color:#666;padding:3px 0;font-weight:bold;">Call Duration</td><td>{duration_str}</td></tr>
      <tr><td style="color:#666;padding:3px 0;font-weight:bold;">Call ID</td>
          <td style="font-family:monospace;font-size:11px;color:#888;">{call_id}</td></tr>
    </table>
  </div>
  <div style="padding:22px 30px;">
    <h3 style="color:#1A3D6B;font-size:13px;border-bottom:2px solid #2E75B6;padding-bottom:5px;margin-top:0;">
      AGENT CONFIGURATION
    </h3>
    <table style="width:100%;font-size:12px;border-collapse:collapse;margin-bottom:16px;">
      <tr style="background:#F7F9FC;">
        <td style="color:#666;width:170px;padding:5px 8px;font-weight:bold;border:1px solid #C8D4E8;">Agent Name</td>
        <td style="padding:5px 8px;border:1px solid #C8D4E8;">{agent_name}</td></tr>
      <tr><td style="color:#666;padding:5px 8px;font-weight:bold;border:1px solid #C8D4E8;">Tone</td>
          <td style="padding:5px 8px;border:1px solid #C8D4E8;">{tone}</td></tr>
      <tr style="background:#F7F9FC;">
        <td style="color:#666;padding:5px 8px;font-weight:bold;border:1px solid #C8D4E8;">Greeting</td>
        <td style="padding:5px 8px;border:1px solid #C8D4E8;font-style:italic;">&ldquo;{greeting_preview}&rdquo;</td></tr>
      <tr><td style="color:#666;padding:5px 8px;font-weight:bold;border:1px solid #C8D4E8;">Top Call Reasons</td>
          <td style="padding:5px 8px;border:1px solid #C8D4E8;">{top_calls_str}</td></tr>
      <tr style="background:#F7F9FC;">
        <td style="color:#666;padding:5px 8px;font-weight:bold;border:1px solid #C8D4E8;">Escalation #</td>
        <td style="padding:5px 8px;border:1px solid #C8D4E8;">{escalation}</td></tr>
      <tr><td style="color:#666;padding:5px 8px;font-weight:bold;border:1px solid #C8D4E8;">After-Hours</td>
          <td style="padding:5px 8px;border:1px solid #C8D4E8;">{after_preview}</td></tr>
      <tr style="background:#F7F9FC;">
        <td style="color:#666;padding:5px 8px;font-weight:bold;border:1px solid #C8D4E8;">Services</td>
        <td style="padding:5px 8px;border:1px solid #C8D4E8;">{svc_str}</td></tr>
      <tr><td style="color:#666;padding:5px 8px;font-weight:bold;border:1px solid #C8D4E8;">Wishlist</td>
          <td style="padding:5px 8px;border:1px solid #C8D4E8;">{wishlist_str}</td></tr>
    </table>
    <div style="background:#EAF2FB;border-left:4px solid #2E75B6;padding:14px 18px;border-radius:0 4px 4px 0;margin-bottom:16px;">
      <p style="margin:0 0 6px;font-size:13px;color:#1A3D6B;font-weight:bold;">Two attachments included:</p>
      <p style="margin:0 0 4px;font-size:12px;color:#404040;">
        <b>1. ARIA_Intake_Summary_{safe_biz}_{date_file}.pdf</b> — Full extracted data report
      </p>
      <p style="margin:0;font-size:12px;color:#404040;">
        <b>2. ARIA_Intake_Form_{safe_biz}_{date_file}.docx</b> — Populated intake form, checkboxes checked, write-ins filled
      </p>
    </div>
    <p style="font-size:12px;color:#888;margin:0;">
      Review both attachments and begin agent build when ready.
      The .docx is the filing copy — save it to the client folder.
    </p>
  </div>
  <div style="background:#1A3D6B;padding:14px 30px;border-radius:0 0 6px 6px;text-align:center;">
    <p style="color:#A8C4E8;font-size:11px;margin:0;">
      InSync Tech Inc. &nbsp;|&nbsp; Venice, Florida &nbsp;|&nbsp; insynctech.io
    </p>
  </div>
</body>
</html>"""

    pdf_b64  = base64.b64encode(pdf_bytes).decode("utf-8")
    form_b64 = base64.b64encode(form_bytes).decode("utf-8")

    payload = {
        "from":    FROM_EMAIL,
        "to":      [TO_EMAIL],
        "subject": subject,
        "html":    html_body,
        "attachments": [
            {
                "filename":     f"ARIA_Intake_Summary_{safe_biz}_{date_file}.pdf",
                "content":      pdf_b64,
                "content_type": "application/pdf"
            },
            {
                "filename":     f"ARIA_Intake_Form_{safe_biz}_{date_file}.docx",
                "content":      form_b64,
                "content_type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            }
        ]
    }

    async with httpx.AsyncClient(timeout=30) as http:
        resp = await http.post(
            RESEND_ENDPOINT,
            headers={"Authorization": f"Bearer {RESEND_API_KEY}", "Content-Type": "application/json"},
            json=payload
        )
        resp.raise_for_status()
        return resp.json()
