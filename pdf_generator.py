"""
pdf_generator.py
Generates a clean, populated ARIA intake report PDF from extracted fields.
Uses ReportLab — no external templates needed.
"""

import io
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)

# ─── BRAND COLORS ────────────────────────────────────────────────────────────
BLUE       = colors.HexColor("#1A3D6B")
LIGHT_BLUE = colors.HexColor("#2E75B6")
GRAY       = colors.HexColor("#404040")
MID_GRAY   = colors.HexColor("#666666")
LIGHT_BG   = colors.HexColor("#F0F4FA")
GREEN      = colors.HexColor("#1E7E34")
BORDER     = colors.HexColor("#C8D4E8")
WHITE      = colors.white


def _safe(val, fallback="—"):
    """Return value or fallback if None/empty."""
    if val is None:
        return fallback
    if isinstance(val, list):
        return ", ".join(str(v) for v in val) if val else fallback
    return str(val).strip() or fallback


def _hour_str(h: dict) -> str:
    """Format hours dict to readable string."""
    if not h or not isinstance(h, dict):
        return "—"
    if h.get("closed"):
        return "Closed"
    if h.get("by_appt"):
        return "By Appointment"
    o = h.get("open", "")
    c = h.get("close", "")
    if o and c:
        return f"{o} – {c}"
    return "—"


def generate_intake_pdf(fields: dict, metadata: dict) -> bytes:
    """Build and return PDF bytes for the populated intake report."""
    buf = io.BytesIO()
    doc = SimpleDocTemplate(
        buf,
        pagesize=letter,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
    )

    styles = getSampleStyleSheet()
    W = 7.0 * inch  # content width

    # ─── CUSTOM STYLES ───────────────────────────────────────────────────────
    title_style = ParagraphStyle("title", fontSize=22, textColor=BLUE,
                                  fontName="Helvetica-Bold", spaceAfter=4)
    sub_style   = ParagraphStyle("sub",   fontSize=12, textColor=LIGHT_BLUE,
                                  fontName="Helvetica", spaceAfter=2)
    meta_style  = ParagraphStyle("meta",  fontSize=9,  textColor=MID_GRAY,
                                  fontName="Helvetica-Oblique", spaceAfter=12)
    sec_style   = ParagraphStyle("sec",   fontSize=11, textColor=BLUE,
                                  fontName="Helvetica-Bold", spaceBefore=14, spaceAfter=6)
    label_style = ParagraphStyle("lbl",   fontSize=9,  textColor=MID_GRAY,
                                  fontName="Helvetica-Bold", spaceAfter=1)
    value_style = ParagraphStyle("val",   fontSize=10, textColor=GRAY,
                                  fontName="Helvetica", spaceAfter=6)
    note_style  = ParagraphStyle("note",  fontSize=8,  textColor=MID_GRAY,
                                  fontName="Helvetica-Oblique")

    def sec(title):
        return [
            Spacer(1, 0.1 * inch),
            HRFlowable(width=W, thickness=2, color=LIGHT_BLUE, spaceAfter=4),
            Paragraph(title.upper(), sec_style),
        ]

    def field(label, value, fallback="—"):
        v = _safe(value, fallback)
        return [
            Paragraph(label, label_style),
            Paragraph(v, value_style),
        ]

    def two_fields(l1, v1, l2, v2):
        half = W / 2 - 0.1 * inch
        t = Table(
            [[
                [Paragraph(l1, label_style), Paragraph(_safe(v1), value_style)],
                [Paragraph(l2, label_style), Paragraph(_safe(v2), value_style)],
            ]],
            colWidths=[half, half]
        )
        t.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING",  (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("BOTTOMPADDING",(0, 0), (-1, -1), 0),
            ("TOPPADDING",   (0, 0), (-1, -1), 0),
        ]))
        return [t]

    # ─── BUILD STORY ─────────────────────────────────────────────────────────
    story = []
    f = fields

    # Title block
    business = f.get("business_legal_name") or f.get("dba_name") or "New Client"
    received  = metadata.get("received_at", datetime.utcnow().isoformat())[:10]
    call_id   = metadata.get("conversation_id", "—")

    story += [
        Paragraph("ARIA INTAKE REPORT", title_style),
        Paragraph("InSync Tech Inc. — AI Receptionist Setup", sub_style),
        Paragraph(
            f"Business: {business}  |  Call ID: {call_id}  |  Received: {received}",
            meta_style
        ),
        HRFlowable(width=W, thickness=3, color=LIGHT_BLUE, spaceAfter=8),
    ]

    # ── SECTION 1 — BUSINESS INFO ─────────────────────────────────────────────
    story += sec("1. Business Information")
    story += two_fields("Legal Business Name", f.get("business_legal_name"),
                        "DBA", f.get("dba_name"))
    story += two_fields("Owner / Contact", f.get("owner_name"),
                        "Title", f.get("owner_title"))
    story += two_fields("Business Address", f.get("business_address"),
                        "Website", f.get("website_url"))
    story += two_fields("Industry / Type", f.get("business_type"),
                        "Years in Operation", f.get("years_in_operation"))
    story += two_fields("Team Size", f.get("team_size"),
                        "Owner Phone", f.get("owner_phone"))
    story += field("Business Description", f.get("business_description"))

    # ── SECTION 2 — CONTACT & DELIVERY ───────────────────────────────────────
    story += sec("2. Contact & Report Delivery")
    story += field("Report Email Address(es)", f.get("report_email_addresses"))
    story += field("Report Delivery Preference", f.get("report_delivery_preference"))

    # ── SECTION 3 — HOURS ────────────────────────────────────────────────────
    story += sec("3. Hours of Operation")

    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    hour_data = [["Day", "Hours"]]
    for d in days:
        h = f.get(f"hours_{d}")
        hour_data.append([d.capitalize(), _hour_str(h)])

    hour_table = Table(hour_data, colWidths=[1.4 * inch, 5.6 * inch])
    hour_table.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, 0),  LIGHT_BG),
        ("TEXTCOLOR",    (0, 0), (-1, 0),  BLUE),
        ("FONTNAME",     (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, -1), 9),
        ("FONTNAME",     (0, 1), (-1, -1), "Helvetica"),
        ("TEXTCOLOR",    (0, 1), (-1, -1), GRAY),
        ("GRID",         (0, 0), (-1, -1), 0.5, BORDER),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),   [WHITE, colors.HexColor("#F7F9FC")]),
        ("LEFTPADDING",  (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING",   (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 5),
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(hour_table)
    story.append(Spacer(1, 0.05 * inch))
    story += field("Holiday / Seasonal Notes", f.get("holiday_notes"))

    # ── SECTION 4 — GREETING & PERSONALITY ───────────────────────────────────
    story += sec("4. Greeting & Personality")
    story += two_fields("Agent Name", f.get("agent_name"),
                        "Voice Preference", f.get("voice_gender_preference"))
    story += field("Tone / Personality", f.get("tone_preference"))
    story += field("Opening Greeting Script", f.get("greeting_script_raw"))
    story += field("AI Disclosure Preference", f.get("ai_disclosure_preference"))
    story += field("Brand Phrases / Keywords", f.get("brand_phrases"))

    # ── SECTION 5 — CALL HANDLING ─────────────────────────────────────────────
    story += sec("5. Call Handling & Behavior")
    story += field("Primary Call Reasons", f.get("primary_call_reasons"))
    story += field("Common Repetitive Questions", f.get("common_repetitive_questions"))
    story += field("High-Value Call Types", f.get("high_value_call_types"))
    story += field("Required Caller Fields to Capture", f.get("required_caller_fields"))
    story += field("Industry-Specific Capture Fields", f.get("industry_specific_capture_fields"))
    story += two_fields("Appointment Handling", f.get("appointment_handling_method"),
                        "Booking Link", f.get("booking_link"))
    story += field("After-Hours Script", f.get("after_hours_script"))
    story += two_fields("After-Hours Emergency Number", f.get("after_hours_emergency_number"),
                        "Escalation Number", f.get("escalation_number"))
    story += field("Escalation Path", f.get("escalation_path"))
    story += field("Complaint Handling", f.get("complaint_handling"))
    story += field("Calls to Always Escalate (Never Handle)", f.get("escalation_trigger_list"))

    # ── SECTION 6 — SERVICES & KNOWLEDGE ─────────────────────────────────────
    story += sec("6. Services, Products & Business Knowledge")

    # Services table
    services = f.get("services_list", [])
    if services and isinstance(services, list):
        svc_data = [["Service / Product", "Description", "Price"]]
        for s in services:
            if isinstance(s, dict):
                svc_data.append([
                    _safe(s.get("name")),
                    _safe(s.get("description")),
                    _safe(s.get("price"))
                ])
            else:
                svc_data.append([str(s), "—", "—"])
        svc_table = Table(svc_data, colWidths=[2.0 * inch, 3.5 * inch, 1.5 * inch])
        svc_table.setStyle(TableStyle([
            ("BACKGROUND",   (0, 0), (-1, 0),  LIGHT_BG),
            ("TEXTCOLOR",    (0, 0), (-1, 0),  BLUE),
            ("FONTNAME",     (0, 0), (-1, 0),  "Helvetica-Bold"),
            ("FONTSIZE",     (0, 0), (-1, -1), 9),
            ("FONTNAME",     (0, 1), (-1, -1), "Helvetica"),
            ("TEXTCOLOR",    (0, 1), (-1, -1), GRAY),
            ("GRID",         (0, 0), (-1, -1), 0.5, BORDER),
            ("ROWBACKGROUNDS",(0,1),(-1,-1),   [WHITE, colors.HexColor("#F7F9FC")]),
            ("LEFTPADDING",  (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING",   (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING",(0, 0), (-1, -1), 4),
            ("VALIGN",       (0, 0), (-1, -1), "TOP"),
            ("WORDWRAP",     (0, 0), (-1, -1), True),
        ]))
        story.append(svc_table)
        story.append(Spacer(1, 0.05 * inch))

    story += two_fields("Pricing Approach", f.get("pricing_approach"),
                        "Popular Services", f.get("popular_services"))
    story += field("Services NOT Offered", f.get("services_not_offered"))
    story += field("Prohibited Statements / Never Say", f.get("prohibited_statements"))

    # FAQs
    faqs = [
        ("Walk-ins?", f.get("faq_walk_ins")),
        ("Payment Methods?", f.get("faq_payment_methods")),
        ("Cancellation Policy?", f.get("faq_cancellation_policy")),
        ("New Customers?", f.get("faq_new_customers")),
        ("Parking / Location?", f.get("faq_parking_location")),
    ]
    additional_faqs = f.get("faq_additional", [])

    faq_data = [["Question", "Answer"]]
    for q, a in faqs:
        if a:
            faq_data.append([q, _safe(a)])
    if isinstance(additional_faqs, list):
        for item in additional_faqs:
            if isinstance(item, dict):
                faq_data.append([_safe(item.get("q")), _safe(item.get("a"))])
            elif isinstance(item, str) and item:
                faq_data.append(["Additional", item])

    if len(faq_data) > 1:
        story.append(Paragraph("Frequently Asked Questions", label_style))
        faq_table = Table(faq_data, colWidths=[2.5 * inch, 4.5 * inch])
        faq_table.setStyle(TableStyle([
            ("BACKGROUND",   (0, 0), (-1, 0),  LIGHT_BG),
            ("TEXTCOLOR",    (0, 0), (-1, 0),  BLUE),
            ("FONTNAME",     (0, 0), (-1, 0),  "Helvetica-Bold"),
            ("FONTSIZE",     (0, 0), (-1, -1), 9),
            ("FONTNAME",     (0, 1), (-1, -1), "Helvetica"),
            ("TEXTCOLOR",    (0, 1), (-1, -1), GRAY),
            ("GRID",         (0, 0), (-1, -1), 0.5, BORDER),
            ("ROWBACKGROUNDS",(0,1),(-1,-1),   [WHITE, colors.HexColor("#F7F9FC")]),
            ("LEFTPADDING",  (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING",   (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING",(0, 0), (-1, -1), 4),
            ("VALIGN",       (0, 0), (-1, -1), "TOP"),
        ]))
        story.append(faq_table)
        story.append(Spacer(1, 0.05 * inch))

    # ── SECTION 7 — NOTIFICATIONS ────────────────────────────────────────────
    story += sec("7. Notifications & Follow-Up")
    story += field("Notification Triggers", f.get("notification_triggers"))
    story += two_fields("Callback Urgency", f.get("callback_urgency_preference"),
                        "Follow-Up Preference", f.get("followup_preference"))
    story += field("Future Follow-Up Interest", f.get("future_followup_interest"))

    # ── SECTION 9 — SOFTWARE & SYSTEMS ──────────────────────────────────────
    story += sec("9. Current Software & Systems")
    story += two_fields("Phone System", f.get("current_phone_system"),
                        "Call Routing", f.get("call_routing_setup"))
    story += two_fields("Scheduling / Booking", f.get("scheduling_software"),
                        "Booking Workflow", f.get("booking_workflow"))
    story += two_fields("CRM / Lead Management", f.get("crm_software"),
                        "Customer Data Location", f.get("customer_data_location"))
    story += two_fields("Payment System", f.get("payment_system"),
                        "Online Payments", f.get("online_payment_capability"))
    story += two_fields("Email / Marketing", f.get("email_marketing_tools"),
                        "Reviews / Reputation", f.get("review_platforms"))
    story += two_fields("Accounting Software", f.get("accounting_software"),
                        "Operations Software", f.get("operations_software"))
    story += field("Integration Wishlist", f.get("integration_wishlist"))
    story += field("Highest-Value Integration", f.get("highest_value_integration"))
    story += field("Workflow Pain Points", f.get("workflow_pain_points"))

    # ── SECTION 10 — WISHLIST ─────────────────────────────────────────────────
    story += sec("10. Future Features & Wishlist")
    story += field("Requested Future Features", f.get("wishlist_features"))
    story += field("Remaining Pain Points", f.get("pain_points_remaining"))
    story += field("Future Vision", f.get("future_vision"))
    story += field("Additional Notes", f.get("closing_notes"))

    # ── FOOTER ───────────────────────────────────────────────────────────────
    story += [
        Spacer(1, 0.2 * inch),
        HRFlowable(width=W, thickness=1, color=BORDER, spaceAfter=4),
        Paragraph(
            f"Generated by InSync Tech ARIA Intake Pipeline  |  "
            f"Call ID: {call_id}  |  {received}  |  insynctech.io",
            note_style
        )
    ]

    doc.build(story)
    return buf.getvalue()
