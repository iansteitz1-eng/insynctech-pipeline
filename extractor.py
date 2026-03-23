"""
extractor.py
Claude Haiku — structured field extraction from intake call transcript.
Returns a dict matching every field in the ARIA intake form.
"""

import os
import json
import re
import anthropic

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
client = anthropic.AsyncAnthropic(api_key=ANTHROPIC_API_KEY)

SYSTEM_PROMPT = """You are a data extraction assistant for InSync Tech, an AI receptionist company.

You will receive a transcript of an onboarding interview between ARIA (an AI agent) and a new business client.
Your job is to extract every piece of information the client provided and return it as a clean JSON object.

Rules:
- Extract ONLY what the client actually said — do not infer or fabricate
- If a field was not mentioned, use null
- For list fields, return an array of strings
- Keep values concise but complete — preserve the client's actual words where meaningful
- For hours, use 24h format (e.g. "09:00" to "17:00") or plain text like "9am to 5pm"
- For boolean fields, use true/false/null

Return ONLY valid JSON. No preamble, no explanation, no markdown fences."""

EXTRACTION_PROMPT = """Extract all client information from this intake call transcript and return as JSON.

Use exactly these field names:

BUSINESS INFO:
business_legal_name, dba_name, owner_name, owner_title, business_type,
business_description, team_size, years_in_operation, business_address, website_url

CONTACT & DELIVERY:
report_email_addresses (array), owner_phone, report_delivery_preference

HOURS (each as object with open/close/closed/by_appt):
hours_monday, hours_tuesday, hours_wednesday, hours_thursday,
hours_friday, hours_saturday, hours_sunday, holiday_notes, seasonal_variations

GREETING & PERSONALITY:
agent_name, greeting_script_raw, tone_preference, voice_gender_preference,
ai_disclosure_preference, brand_phrases (array)

CALL HANDLING:
primary_call_reasons (array), common_repetitive_questions (array),
high_value_call_types (array), required_caller_fields (array),
industry_specific_capture_fields (array), appointment_handling_method,
booking_link, after_hours_script, after_hours_emergency_number,
escalation_path, escalation_number, complaint_handling,
escalation_trigger_list (array)

SERVICES & KNOWLEDGE:
services_list (array of objects with name/description/price),
popular_services (array), hidden_gem_services (array),
services_not_offered (array), pricing_approach, pricing_details,
faq_walk_ins, faq_payment_methods, faq_cancellation_policy,
faq_new_customers, faq_parking_location, faq_additional (array of objects with q/a),
prohibited_statements (array)

NOTIFICATIONS:
notification_triggers (array), callback_urgency_preference,
followup_preference, future_followup_interest

CURRENT SOFTWARE & SYSTEMS:
current_phone_system, call_routing_setup,
scheduling_software, booking_workflow,
crm_software, customer_data_location,
payment_system, online_payment_capability,
email_marketing_tools, review_platforms, social_presence,
accounting_software, operations_software,
integration_wishlist (array), highest_value_integration,
workflow_pain_points (array)

WISHLIST:
wishlist_features (array), pain_points_remaining (array),
future_vision, closing_notes

TRANSCRIPT:
---
{transcript}
---

Return ONLY the JSON object."""


async def extract_fields(transcript: str) -> dict:
    """
    Send transcript to Claude Haiku and return structured field dict.
    Falls back to empty dict on failure.
    """
    prompt = EXTRACTION_PROMPT.format(transcript=transcript)

    message = await client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = message.content[0].text.strip()

    # Strip any accidental markdown fences
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # Attempt to extract JSON object from response
        match = re.search(r"\{.*\}", raw, re.DOTALL)
        if match:
            return json.loads(match.group())
        raise ValueError(f"Haiku returned unparseable response: {raw[:200]}")
