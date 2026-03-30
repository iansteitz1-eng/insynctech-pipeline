# ═══════════════════════════════════════════════════════════════════
# DEPLOYMENT RUNBOOK
# InSync Tech, Inc. — New Client Agent Deployment Guide
# ═══════════════════════════════════════════════════════════════════
# Last Updated: March 21, 2026
# ═══════════════════════════════════════════════════════════════════

# 1. PRE-DEPLOYMENT CHECKLIST

| Step | Owner | Status Template |
|------|-------|-----------------|
| Contract signed (DocuSign) | Aria/Ian | ☐ |
| Payment received or pilot terms confirmed | Aria | ☐ |
| Intake call completed (transcript available) | Client | ☐ |
| Intake data reviewed and extracted | Ian | ☐ |
| Business hours confirmed | Ian | ☐ |
| Services/pricing list confirmed | Ian | ☐ |
| Special instructions documented | Ian | ☐ |
| Voice preference selected (male/female/custom) | Client/Ian | ☐ |
| Twilio number provisioned | Ian | ☐ |
| ElevenLabs agent created | Ian | ☐ |

---

# 2. AGENT BUILD PROCESS

## Step 1: Provision Phone Number
```
1. Log into Twilio console
2. Buy a local number (prefer client's area code)
3. Note the number and SID
4. DO NOT configure voice URL yet — do that after agent creation
```

## Step 2: Create ElevenLabs Agent
```
1. Log into ElevenLabs dashboard
2. Create new Conversational AI agent
3. Configure:
   - Name: [Client agent name]
   - Model: claude-sonnet-4-5 (NOT Claude 4 — too expensive for production)
   - Temperature: 0.0
   - Voice: sqskhHdmEWFUgFIrJEuI (default Aria) or client-requested voice
   - Voice settings: stability 0.5, similarity 0.75, speed 1.2
   - Expressive mode: ON
   - Optimize streaming latency: 4
   - Turn timeout: 1.5s
   - Turn eagerness: eager
   - Speculative turn: ON
4. Write system prompt using template (see Section 3)
5. Configure first message greeting
6. Register webhook URL: https://aria-backend-production-ebb5.up.railway.app/webhook/elevenlabs
7. Note the agent_id
```

## Step 3: Connect Twilio to ElevenLabs
```
1. In ElevenLabs agent settings → Phone → Add Twilio
2. Enter Twilio Account SID and Auth Token
3. Assign the provisioned number
4. Test with a call
```

## Step 4: Configure Backend Routing
```
1. In aria-backend/webhook_router.py:
   - Add agent_id to the routing table
   - Map to client's email for post-call summaries
   - Set appropriate summary template
2. Deploy: `railway up` from ~/projects/aria-backend/
3. Verify webhook fires on test call
```

## Step 5: Test Cycle
```
Test 1: Call the number, have a typical conversation
Test 2: Verify post-call email arrives (correct recipient, clean summary)
Test 3: Check Supabase log entry
Test 4: Test edge cases (hang-up, silence, unusual requests)
Test 5: Verify CertusOrdo transaction logged
```

## Step 6: Soft Launch
```
1. Send "Agent Is Live" email (EMAIL-ONB-003)
2. Ask client to test call first
3. Client forwards their business line OR publishes the number
4. Monitor first 24 hours closely
```

---

# 3. SYSTEM PROMPT TEMPLATE

```
You are [Agent Name], the AI phone assistant for [Business Name],
a [business type] located at [address] in [city, state].

YOUR PERSONALITY:
- Warm, friendly, and professional
- Speak naturally — like a real person who works at [Business Name]
- Keep responses concise — callers want quick answers
- Never say "I'm an AI" unless directly asked

BUSINESS INFORMATION:
- Hours: [hours]
- Address: [address]
- Phone: [number]
- Website: [if applicable]

SERVICES & PRICING:
[List all services with prices]

APPOINTMENT BOOKING:
[If applicable: booking rules, available times, booking method]
[If walk-in only: "We're a walk-in [business type]. No appointments needed.
Just come in during business hours. Current wait time is typically [X] minutes."]

CALL HANDLING RULES:
1. Greet the caller warmly
2. Listen to their question
3. Answer using the information above
4. If you can't answer, say: "Let me have [owner name] get back to you.
   Can I get your name and number?"
5. Always be helpful and positive about [Business Name]

THINGS YOU DO NOT DO:
- Do not make promises about specific availability
- Do not discuss employee schedules
- Do not provide medical/legal/financial advice
- Do not argue with callers
- If someone is rude, stay professional and offer to take a message

ESCALATION:
If a caller has an emergency or urgent issue, say:
"I want to make sure this is handled right away. Let me get
your name and number and I'll have [owner name] call you back
within [timeframe]."
```

---

# 4. POST-DEPLOYMENT MONITORING

## First 24 Hours
- Check Railway logs every 2 hours for errors
- Verify every call generates a post-call email
- Listen to at least 3 call recordings
- Check for any prompt issues (wrong info, awkward phrasing)

## First Week
- Daily review of call transcripts (sample 2-3)
- Client check-in at Day 3 (EMAIL-ONB-004)
- Week 1 report (EMAIL-ONB-005)
- Adjust prompt based on real call patterns

## First Month
- Weekly transcript review
- Bi-weekly check-in with client
- Track call volume trend
- Identify common questions not in the prompt → add them
- Month 1 performance report

---

# 5. COMMON DEPLOYMENT ISSUES

| Issue | Cause | Fix |
|-------|-------|-----|
| No post-call email | Webhook not firing | Check ElevenLabs webhook URL matches Railway |
| Email goes to wrong person | Agent routing misconfigured | Check webhook_router.py mapping |
| Agent doesn't answer | Twilio number not connected | Re-link in ElevenLabs Phone settings |
| Agent gives wrong info | Prompt needs updating | Edit system prompt, redeploy |
| Audio quality poor | Latency settings | Increase optimize_streaming_latency to 4 |
| Agent talks too much | Prompt too verbose | Trim system prompt, add "keep responses under 3 sentences" |
| Agent hangs up early | Turn timeout too short | Increase turn_timeout to 2.0 |
| Caller says "I want a real person" | Normal — happens ~15% of calls | Train agent to say "Let me take your info and have [name] call you back" |

---

# 6. DEPLOYMENT TIMELINE

| Phase | Duration | Milestone |
|-------|----------|-----------|
| Contract + Payment | Day 0 | ☐ Signed and paid |
| Intake Call | Day 1-2 | ☐ Completed |
| Agent Build | Day 3-5 | ☐ Built and tested |
| Soft Launch | Day 5-6 | ☐ Client tests |
| Full Launch | Day 7 | ☐ Live with real callers |
| First Check-In | Day 10 | ☐ Feedback collected |
| Week 1 Report | Day 14 | ☐ Sent |
| Pilot Evaluation | Day 30 | ☐ Convert to paid |

# ═══════════════════════════════════════════════════════════════════
# END OF DEPLOYMENT RUNBOOK
# ═══════════════════════════════════════════════════════════════════
