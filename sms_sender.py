"""
sms_sender.py
InSync Tech — Twilio SMS delivery for post-call follow-ups.

Sends from a dedicated InSync Tech outbound number.
Handles E.164 formatting, opt-out safety, and logging.
"""

import os
import re
import logging
from twilio.rest import Client

log = logging.getLogger(__name__)

TWILIO_ACCOUNT_SID  = os.environ.get("TWILIO_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN   = os.environ.get("TWILIO_AUTH_TOKEN", "")
TWILIO_FROM_NUMBER  = os.environ.get("TWILIO_FOLLOWUP_NUMBER", "")  # dedicated outbound number


def _format_e164(phone: str) -> str | None:
    """
    Normalize a phone number to E.164 format (+1XXXXXXXXXX).
    Returns None if it can't be normalized.
    """
    if not phone:
        return None
    digits = re.sub(r"\D", "", phone)
    if len(digits) == 10:
        return f"+1{digits}"
    if len(digits) == 11 and digits.startswith("1"):
        return f"+{digits}"
    if len(digits) > 11:
        return f"+{digits}"
    return None


def send_followup_sms(to_phone: str, message: str) -> dict:
    """
    Send a follow-up SMS via Twilio.
    Returns dict with status and message SID or error.
    """
    if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER]):
        log.error("Twilio credentials not configured — SMS not sent")
        return {"status": "error", "reason": "twilio_not_configured"}

    formatted = _format_e164(to_phone)
    if not formatted:
        log.warning(f"Could not format phone number: {to_phone}")
        return {"status": "error", "reason": "invalid_phone_number"}

    # Append opt-out notice per TCPA best practice
    full_message = f"{message}\n\nReply STOP to unsubscribe."

    try:
        twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        msg = twilio_client.messages.create(
            body=full_message,
            from_=TWILIO_FROM_NUMBER,
            to=formatted
        )
        log.info(f"SMS sent to {formatted} — SID: {msg.sid}")
        return {"status": "sent", "sid": msg.sid, "to": formatted}

    except Exception as e:
        log.error(f"Twilio SMS failed to {formatted}: {e}")
        return {"status": "error", "reason": str(e)}
