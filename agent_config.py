"""
agent_config.py
InSync Tech — Master Agent Router Config

Maps ElevenLabs agent_id to client and handler type.
Add new agents here as clients onboard.
Update AGENT_MAP in Railway environment variables for production.
"""

import os
import json

# Default agent map — override with AGENT_MAP env var in Railway
# Format: {"agent_id": {"client": "name", "handler": "intake|followup|client"}}
DEFAULT_AGENT_MAP = {
    "insync_intake":  {"client": "InSync Tech", "handler": "intake"},
    "insync_main":    {"client": "InSync Tech", "handler": "followup"},
}

def get_agent_map() -> dict:
    """Load agent map from env var or fall back to default."""
    raw = os.environ.get("AGENT_MAP", "")
    if raw:
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            pass
    return DEFAULT_AGENT_MAP

def resolve_agent(agent_id: str) -> dict:
    """
    Look up agent_id and return config dict.
    Falls back to followup handler if agent not found.
    """
    agent_map = get_agent_map()
    return agent_map.get(agent_id, {
        "client": os.environ.get("DEFAULT_BUSINESS_NAME", "InSync Tech"),
        "handler": "followup"
    })
