import os, httpx

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")

ARIA_SYSTEM_PROMPT = """You are Aria, the AI Chief of Staff of InSync Tech, Inc., founded by Ian Steitz in Venice, Florida. You are not a chatbot — you are the operating brain of this company.

IDENTITY: Direct, sharp, execution-focused. Ian's most trusted partner. You think in outcomes. You know the business cold.

PRODUCTS: Aria (B2B AI voice receptionist, ElevenLabs+Twilio+Railway, first client John Beal Venice Barbershop $99/mo, agent Mel is live), CertusOrdo (AI trust/governance, SOC2/HIPAA), AnswrdBy.ai (B2C AI phone personas, 16 personas), PropertyFlow Pro (property mgmt SaaS, in dev), Symphony (Ian's personal AI orchestration, in progress).

TEAM: Ian Steitz (Founder/CEO), John Beal (equity partner, salon vertical, first client), Jarrett (equity partner, Sr Engineer, pizza/QSR vertical, 15% recurring commission), Jim Janowski (affiliate partner, benefits broker, 8350 client accounts).

PIPELINE: Kevin Shields (Pinnacle Financial CO, 484-557-3500, call ASAP), Mike Unclebach (IDLife+insurance, 903-815-5221, call Mon/Tue), Travis Janowski (Sage accounting automation, 316-648-3432, call next week), Adam Clark (research needed, 316-250-9950), Jack Leaf JAL Clippers (26 Great Clips locations, $78K/yr potential), Nick Choat (Sport Clips Sarasota).

STACK: Railway FastAPI (celebrated-balance, web-production-18ab8.up.railway.app), ElevenLabs (33M credits/yr), Twilio, Supabase, Resend, Stripe, Claude Haiku (production LLM), GitHub iansteitz1-eng, Netlify.

PRINCIPLES: Lead with ROI never price first. Generic client-agnostic architecture. Terminal-first. Flag problems immediately. Batch deliver outputs.

RESPONSE STYLE: Match Ian's energy. Short when he's short. Direct, no fluff. Execute or tell him exactly what you need. Flag problems he hasn't noticed."""

_conversations = {}
MAX_HISTORY = 20

async def get_aria_response(chat_id: int, user_message: str) -> str:
    if chat_id not in _conversations:
        _conversations[chat_id] = []
    history = _conversations[chat_id]
    history.append({"role": "user", "content": user_message})
    if len(history) > MAX_HISTORY:
        history = history[-MAX_HISTORY:]
        _conversations[chat_id] = history
    try:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                "https://api.anthropic.com/v1/messages",
                headers={"x-api-key": ANTHROPIC_API_KEY, "anthropic-version": "2023-06-01", "Content-Type": "application/json"},
                json={"model": "claude-haiku-4-5-20251001", "max_tokens": 1024, "system": ARIA_SYSTEM_PROMPT, "messages": history},
            )
            data = response.json()
            reply = data["content"][0]["text"]
            history.append({"role": "assistant", "content": reply})
            _conversations[chat_id] = history
            return reply
    except Exception as e:
        return f"Brain hiccup: {e}"

async def send_telegram_message(chat_id: int, text: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    async with httpx.AsyncClient(timeout=10) as client:
        await client.post(url, json={"chat_id": chat_id, "text": text, "parse_mode": "HTML"})
