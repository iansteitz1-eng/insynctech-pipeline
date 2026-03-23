"""
followup_email.py
InSync Tech — Resend delivery for post-call follow-up emails.

Wraps the Haiku-generated email content in the InSync Tech
branded template and delivers to the caller's email address.
"""

import os
import base64
import httpx
import logging
from datetime import datetime

log = logging.getLogger(__name__)

RESEND_API_KEY  = os.environ.get("RESEND_API_KEY", "")
RESEND_ENDPOINT = "https://api.resend.com/emails"

# From address — shows in the caller's inbox as InSync Tech
FOLLOWUP_FROM   = os.environ.get("FOLLOWUP_FROM_EMAIL", "hello@insynctech.io")


async def send_followup_email(
    to_email: str,
    subject: str,
    inner_html: str,
    business_name: str,
    tier: int,
    attachments: list = None
) -> dict:
    """
    Send the follow-up email to the caller.

    inner_html: the Haiku-generated content block
    attachments: list of dicts [{"filename": str, "content": bytes, "content_type": str}]
    """
    date_str = datetime.utcnow().strftime("%B %d, %Y")

    # Tier label for the header
    tier_labels = {
        3: "Information Overview",
        4: "Personalized Business Summary",
    }
    tier_label = tier_labels.get(tier, "Follow-Up")

    full_html = f"""
<html>
<body style="font-family: Arial, sans-serif; color: #404040;
             max-width: 680px; margin: 0 auto; padding: 0;">

  <!-- Header -->
  <div style="background: #1A3D6B; padding: 22px 30px; border-radius: 6px 6px 0 0;">
    <h1 style="color: white; margin: 0; font-size: 20px; letter-spacing: 0.5px;">
      InSync Tech
    </h1>
    <p style="color: #A8C4E8; margin: 5px 0 0; font-size: 13px;">
      {tier_label}  &nbsp;|&nbsp;  {date_str}
    </p>
  </div>

  <!-- Body -->
  <div style="padding: 28px 30px; background: #ffffff;">
    {inner_html}
  </div>

  <!-- Divider -->
  <div style="height: 4px; background: linear-gradient(to right, #1A3D6B, #2E75B6);"></div>

  <!-- Footer -->
  <div style="background: #F0F4FA; padding: 18px 30px; border-radius: 0 0 6px 6px;">
    <p style="margin: 0 0 6px; font-size: 12px; color: #666;">
      <b>InSync Tech Inc.</b> &nbsp;|&nbsp; Venice, Florida &nbsp;|&nbsp;
      <a href="https://insynctech.io" style="color: #2E75B6; text-decoration: none;">insynctech.io</a>
    </p>
    <p style="margin: 0; font-size: 11px; color: #999;">
      This message was sent on behalf of {business_name}.
      If you have questions, reply to this email or call your business directly.
    </p>
  </div>

</body>
</html>"""

    # Build payload
    payload = {
        "from":    FOLLOWUP_FROM,
        "to":      [to_email],
        "subject": subject,
        "html":    full_html,
    }

    # Add attachments if present (tier 4 PDF, etc.)
    if attachments:
        payload["attachments"] = [
            {
                "filename":     att["filename"],
                "content":      base64.b64encode(att["content"]).decode("utf-8"),
                "content_type": att.get("content_type", "application/octet-stream")
            }
            for att in attachments
        ]

    try:
        async with httpx.AsyncClient(timeout=30) as http:
            resp = await http.post(
                RESEND_ENDPOINT,
                headers={
                    "Authorization": f"Bearer {RESEND_API_KEY}",
                    "Content-Type":  "application/json"
                },
                json=payload
            )
            resp.raise_for_status()
            result = resp.json()
            log.info(f"Follow-up email sent to {to_email} — ID: {result.get('id', '?')}")
            return {"status": "sent", "resend_id": result.get("id"), "to": to_email}

    except Exception as e:
        log.error(f"Follow-up email failed to {to_email}: {e}")
        return {"status": "error", "reason": str(e)}
