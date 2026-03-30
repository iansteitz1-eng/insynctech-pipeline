# ═══════════════════════════════════════════════════════════════════════════════
# PRODUCT ROADMAP & TECHNICAL SPECS
# InSync Tech, Inc. — The Features That Turn a Service Into a Platform
# ═══════════════════════════════════════════════════════════════════════════════
# Version: 1.0 | March 22, 2026
# ═══════════════════════════════════════════════════════════════════════════════
#
# This document covers the product capabilities that are MENTIONED in
# other docs but lack build specs, PLUS critical features with zero
# coverage. Each section includes: what it is, why it matters,
# technical architecture, build priority, and Aria's role.
# ═══════════════════════════════════════════════════════════════════════════════


# ═══════════════════════════════════════════════════════════════════════════════
# 1. MULTI-TENANT ARIA DASHBOARD
# ═══════════════════════════════════════════════════════════════════════════════
#
# This is what turns InSync from "Ian manually configures agents"
# into "clients log in and see their business running on AI."
# Without this, you're a service provider. With it, you're SaaS.

## What It Is

A web UI where:
- Ian sees ALL deployed agents in one view (admin)
- Each client sees THEIR agent only (tenant isolation)
- Live metrics, call logs, transcripts, recordings, performance
- Eventually: clients configure their own agents (Phase 3-4)

## Why It's a Billion-Dollar Feature

| Without Dashboard | With Dashboard |
|-------------------|----------------|
| Ian sends monthly reports manually | Client checks their own dashboard anytime |
| Ian monitors health by checking multiple tools | One screen shows all agent health |
| Clients ask "what am I paying for?" | Clients SEE the value daily |
| Onboarding = Ian builds everything | Onboarding = client completes setup wizard |
| Can support ~50 clients before drowning | Can support 500+ with same headcount |
| Service company valuation (2-5x revenue) | SaaS company valuation (10-20x revenue) |

## Technical Architecture

```
┌─────────────────────────────────────────────────────┐
│              ARIA DASHBOARD (Web App)                │
│              dashboard.insynctech.io                 │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌───────────────┐  ┌───────────────────────────┐  │
│  │  ADMIN VIEW   │  │     CLIENT VIEW            │  │
│  │  (Ian only)   │  │     (Per tenant)            │  │
│  │               │  │                             │  │
│  │ All agents    │  │ My agent only               │  │
│  │ All clients   │  │ My calls, my metrics        │  │
│  │ All revenue   │  │ My transcripts              │  │
│  │ System health │  │ My recordings               │  │
│  │ Deploy new    │  │ My invoice/billing          │  │
│  └───────┬───────┘  └──────────┬──────────────────┘  │
│          │                     │                     │
│          └──────────┬──────────┘                     │
│                     │                                │
│              ┌──────▼──────┐                         │
│              │  SUPABASE   │                         │
│              │  (Database) │                         │
│              │             │                         │
│              │ Row-level   │                         │
│              │ security    │                         │
│              │ per tenant  │                         │
│              └──────┬──────┘                         │
│                     │                                │
│          ┌──────────┼──────────┐                     │
│          │          │          │                     │
│     ElevenLabs   Twilio    Railway                   │
│     (metrics)    (logs)    (backend)                 │
└─────────────────────────────────────────────────────┘
```

## Feature Spec (Phased)

### Phase 1: Admin Dashboard (Build at 10+ Clients)
**Pages:**
- **Agent Overview:** All agents in a grid. Status (green/yellow/red), calls today, calls this week.
- **Client List:** Name, agent, tier, MRR, health score, last check-in.
- **Agent Detail:** Click an agent → call log, transcripts, recordings, performance charts.
- **Financial Summary:** Total MRR, MRR by client, growth chart, churn tracking.
- **Deploy New Agent:** Form to create a new agent config (feeds into backend).

**Tech:** Next.js (like existing CertusOrdo dashboard) on Netlify, Supabase backend.

### Phase 2: Client Portal (Build at 25+ Clients)
**Pages (per client):**
- **My Dashboard:** Calls today, calls this week, calls this month. Trend charts.
- **Call Log:** Table of every call. Click for transcript + audio player.
- **Performance:** Resolution rate, avg duration, peak hours, common questions.
- **Settings:** Business hours, escalation rules, greeting preferences.
- **Billing:** Current plan, next invoice, payment history.

**Auth:** Supabase Auth with Row Level Security (tenant isolation).

### Phase 3: Self-Service Agent Builder (Build at 100+ Clients)
- Client fills out a wizard (business type, hours, services, personality)
- System generates agent config automatically
- Agent deploys without Ian's involvement
- This is the "service → SaaS" transition moment

## Aria's Role
- Tracks dashboard build progress as a project in Google Sheets
- Generates the data that populates the dashboard (call logs, metrics)
- Sends clients links to their portal as part of onboarding (Phase 2)
- Monitors dashboard usage: "Client X hasn't logged in 30 days — churn risk?"

## Build Priority
| Phase | When | Trigger |
|-------|------|---------|
| Admin Dashboard | 10+ clients | Ian spending >2 hours/week on manual reporting |
| Client Portal | 25+ clients | Clients asking "can I see my calls?" |
| Self-Service Builder | 100+ clients | Ian can't build agents fast enough |


# ═══════════════════════════════════════════════════════════════════════════════
# 2. ARIA OUTBOUND — The Revenue Doubler
# ═══════════════════════════════════════════════════════════════════════════════
#
# Everything built so far: ARIA answers INBOUND calls.
# This section: ARIA MAKES outbound calls.
# Same infrastructure. Double the value. Double the pricing.

## What It Is

ARIA proactively calls a business's customers on their behalf:
- Appointment reminders ("Hi, this is [Business]. Confirming your 2 PM tomorrow.")
- No-show follow-ups ("We missed you today. Want to reschedule?")
- Review requests ("Thanks for visiting! Would you leave us a quick review?")
- Payment reminders ("This is a friendly reminder about your balance of $X.")
- Recall campaigns ("It's been 6 months since your last cleaning. Time to book?")
- Waitlist notifications ("A spot just opened up. Want to come in today?")
- Post-service follow-ups ("How was your visit? Anything we can improve?")

## Why This Is a Billion-Dollar Feature

### Revenue Impact Per Vertical

**Dental:**
- Recall campaigns: 30% of patients don't return for next cleaning
- Average practice: 1,500 active patients, 450 lapsed
- ARIA calls 450 patients, 20% rebook = 90 patients × $200 avg = $18,000 recovered
- Annual recall value per practice: $36,000-72,000
- ARIA Outbound price: $500-1,000/mo additional → $6,000-12,000/yr
- Client ROI: 3-12x

**Veterinary:**
- Annual wellness reminders, vaccine reminders, follow-up care
- Similar math: 1,000 active patients, 300 lapsed, 20% rebook = $15,000-30,000 recovered
- ARIA Outbound price: $300-500/mo additional

**Auto Dealer (Service):**
- "Your vehicle is due for service" campaigns
- Recall notice follow-ups (safety + revenue)
- CSI survey calls (manufacturer requires these)
- Value per dealership: $20,000-40,000/yr in recovered service revenue

**Property Management:**
- Lease renewal reminders
- Maintenance follow-up ("Was the repair completed to your satisfaction?")
- Rent reminder calls (reduces late payments by 20-30%)
- Value per 500 units: $50,000-100,000/yr in reduced vacancy + collections

### The Pricing Play
```
CURRENT: ARIA Inbound only
  Starter: $149/mo  |  Core: $249/mo  |  Pro: $499/mo

WITH OUTBOUND ADD-ON:
  Inbound + Outbound: +$200-500/mo depending on volume
  Starter+: $349/mo  |  Core+: $449/mo  |  Pro+: $999/mo

EFFECTIVE ARPU INCREASE: 60-100%
Same infrastructure. Same client. Double the revenue.
```

## Technical Architecture

```
OUTBOUND CALL FLOW:

1. Client uploads contact list (CSV) or connects CRM
   → Stored in Supabase: contact_name, phone, reason, scheduled_time

2. ARIA Outbound Scheduler (Railway cron job)
   → Reads queue from Supabase
   → At scheduled_time: initiates outbound call via Twilio

3. Twilio places call → connects to ElevenLabs agent
   → Agent knows: who they're calling, why, and what to say
   → Dynamic first message: "Hi [Name], this is [Agent] from [Business]..."

4. Call completes → same post-call pipeline as inbound
   → Transcript, summary, recording → email to business owner
   → Outcome logged: reached/voicemail/no-answer/rescheduled/declined

5. Retry logic:
   → No answer: retry in 4 hours, then next day, then mark "unreachable"
   → Voicemail: leave message, mark "voicemail left"
   → Reached + positive: log outcome, update CRM
   → Reached + declined: log, do not retry
```

## Outbound Campaign Types (Pre-Built Templates)

### Campaign: Appointment Reminder
```
Trigger: 24 hours before scheduled appointment
Script: "Hi [Name], this is [Agent] from [Business]. I'm calling to
confirm your appointment tomorrow at [time]. Will you be able to make it?
[If yes:] Great, we'll see you then.
[If no:] No problem. Would you like to reschedule?
[If voicemail:] Hi [Name], this is [Agent] from [Business] confirming
your appointment tomorrow at [time]. If you need to reschedule,
please call us at [number]. We look forward to seeing you."
```

### Campaign: No-Show Follow-Up
```
Trigger: 2 hours after missed appointment
Script: "Hi [Name], this is [Agent] from [Business]. We noticed you
weren't able to make your appointment today. No worries — would you
like to reschedule? We have availability [suggest times]."
```

### Campaign: Recall / Reactivation
```
Trigger: X days/months since last visit (configurable)
Script: "Hi [Name], this is [Agent] from [Business]. It's been
[timeframe] since your last [service]. We'd love to get you back
on the schedule. Do you have a moment to book an appointment?"
```

### Campaign: Review Request
```
Trigger: 24-48 hours after completed appointment
Script: "Hi [Name], this is [Agent] from [Business]. We hope
you enjoyed your visit. If you have a moment, we'd really appreciate
a quick Google review. I can text you the link right now.
Would that be okay?"
→ If yes: send SMS with Google Review link (requires A2P)
```

### Campaign: Payment Reminder
```
Trigger: X days after invoice due date (configurable)
Script: "Hi [Name], this is [Agent] from [Business]. I'm calling
about your balance of $[amount]. Would you like to take care of
that over the phone, or would you prefer I send you a payment link?
[If phone:] Great, let me transfer you to our billing line.
[If link:] Perfect, I'll text that to you right now."
```

## TCPA / Compliance Requirements

⚠️ CRITICAL — Outbound AI calls have strict legal requirements:

1. **Prior express consent required** for non-emergency calls to cell phones
   → Client must have customer consent on file (intake form, booking form)
   → Aria does NOT call anyone without documented consent

2. **Caller ID must display business number** (not a generic/blocked number)
   → Configure Twilio to display client's business number

3. **AI disclosure** — Some states require "This call uses AI technology"
   → Include in agent prompt: disclose if asked, or proactively in first message

4. **Do-Not-Call compliance**
   → Maintain opt-out list per client
   → If customer says "don't call me" → immediately add to DNC, never retry

5. **Time restrictions**
   → No calls before 8 AM or after 9 PM local time of the recipient
   → ARIA Outbound Scheduler must calculate recipient timezone

6. **Recording disclosure**
   → Two-party consent states: "This call may be recorded for quality purposes"
   → Include in every outbound call greeting

## Aria's Role (Division 19 — Outbound Campaigns)

Aria manages the outbound campaign engine:
- Helps clients set up campaigns (via check-in emails or dashboard)
- Monitors campaign performance (reach rate, rebook rate, review completion)
- Generates outbound-specific reports for clients
- Flags compliance issues (calling too early/late, missing consent)
- Recommends campaign optimizations based on data
- Tracks outbound revenue separately in FINANCIAL_DASHBOARD

## Sales Pitch for Outbound

```
"Right now, ARIA answers your phone. But what if she could also
MAKE calls for you?

Imagine: every patient who's overdue for a cleaning gets a personal
call from your AI. 'Hi Sarah, it's been 6 months since your last
visit. Want to schedule?' No staff time. No phone tag. Just patients
rebooking automatically.

We're seeing practices recover $36,000-72,000 per year in lapsed
patient revenue with outbound recall campaigns alone.

It's an add-on to your existing plan. Same AI. Same voice. Same
trust. Just now she works for you in both directions."
```

## Build Priority
| When | Trigger |
|------|---------|
| Phase 2 (25+ clients) | Clients asking "can ARIA do reminders?" |
| Start with: Appointment reminders (simplest, highest value) |
| Then add: Recall campaigns (biggest revenue impact) |
| Then add: Review requests (helps client's Google ranking) |
| Last: Payment reminders (sensitive, needs careful compliance) |


# ═══════════════════════════════════════════════════════════════════════════════
# 3. CERTUSRODO × ARIA CALL INTEGRATION
# ═══════════════════════════════════════════════════════════════════════════════
#
# Every ARIA call transcript is already captured.
# CertusOrdo already has an immutable audit trail.
# Connecting them creates a compliance moat no competitor can replicate.

## What It Is

Every call ARIA handles becomes a CertusOrdo transaction:
- SHA256 hash of the full transcript (tamper-evident)
- Timestamp (when the call started, ended)
- Caller ID (who called)
- Agent ID (which ARIA agent handled it)
- Outcome (appointment booked, message taken, escalated, etc.)
- Recording hash (proves the audio hasn't been altered)
- Full transcript (stored in the transaction pre/post state)

## Why This Matters for Healthcare / Regulated Verticals

### HIPAA-Adjacent Value
Dental, vet, and urgent care clients handle PHI (Protected Health Information)
on calls — patient names, appointment details, insurance info.

CertusOrdo integration provides:
- **Tamper-evident transcript storage** — proves the AI said exactly what it said
- **Immutable call logs** — can't be deleted or modified after the fact
- **Audit trail for regulatory review** — "Show us every call from March" → one API call
- **Data retention compliance** — automated retention policies with provable deletion
- **Incident forensics** — if an AI says something wrong, the exact transcript is preserved

### Enterprise Sales Differentiator
```
ENTERPRISE PITCH:
"Every call your AI handles generates a tamper-evident audit record
in CertusOrdo. SHA256 hash chain, timestamped, immutable. When a
regulator or compliance officer asks 'what did your AI say to that
patient?' — you hand them a cryptographically verified transcript.

No other AI voice provider can offer this."
```

## Technical Implementation

```
CURRENT FLOW:
Call ends → ElevenLabs webhook → Railway backend →
Claude Haiku summary → Resend email → Supabase log

ENHANCED FLOW (Add CertusOrdo):
Call ends → ElevenLabs webhook → Railway backend →
├── Claude Haiku summary → Resend email → Supabase log
└── CertusOrdo transaction:
    ├── BEGIN: agent_id, caller_number, timestamp
    ├── PRE-STATE: call_initiated
    ├── POST-STATE: {
    │     transcript_hash: SHA256(full_transcript),
    │     recording_hash: SHA256(mp3_bytes),
    │     summary: claude_summary,
    │     outcome: "appointment_booked" | "message_taken" | "escalated",
    │     duration_seconds: X,
    │     caller_id: "redacted_or_hashed"
    │   }
    └── COMMIT

One additional API call per call. ~10ms latency. Zero user-facing impact.
```

## Implementation on Railway Backend

Add to `webhook_router.py` post-call processing:
```python
# After existing summary generation and email send:
import hashlib
import requests

# Hash transcript and recording
transcript_hash = hashlib.sha256(transcript.encode()).hexdigest()
recording_hash = hashlib.sha256(mp3_bytes).hexdigest()

# Log to CertusOrdo
certusrodo_payload = {
    "action_type": "voice_call_completed",
    "pre_state": {"status": "call_initiated", "agent_id": agent_id},
    "post_state": {
        "transcript_hash": transcript_hash,
        "recording_hash": recording_hash,
        "summary": summary,
        "outcome": outcome,
        "duration": duration,
        "caller_hash": hashlib.sha256(caller_number.encode()).hexdigest()
    },
    "confidence": 100
}
# POST to CertusOrdo API
```

## Build Priority
| When | Trigger |
|------|---------|
| Phase 1 (NOW) | Add to webhook_router.py — one afternoon of coding |
| Immediate value | Every existing call gets audit trail retroactively |
| Sales value | "HIPAA-adjacent compliance" opens healthcare vertical |
| Investor value | "Our audit trail is cryptographically verified" |

**This should be one of the FIRST things Ian builds.** It's 50 lines of code
and it transforms every call from a log entry into a compliance asset.


# ═══════════════════════════════════════════════════════════════════════════════
# 4. WARM TRANSFER PROTOCOL
# ═══════════════════════════════════════════════════════════════════════════════
#
# When ARIA can't handle a call and needs to transfer to a human,
# the human currently gets a cold handoff — "hello?" with zero context.
# This feature changes everything.

## What It Is

When ARIA escalates a call to a human, she:
1. Tells the caller: "Let me connect you with [Name]. One moment."
2. Bridges the human into the call
3. BEFORE connecting: whispers a context brief to the human:

```
"Transferring Maria. She's asking about a two-bedroom apartment.
She has a sixty-pound lab. She needs a March move-in date.
She's interested in covered parking. She sounds friendly but
is comparing multiple properties."
```

4. Human picks up already knowing everything. Caller never repeats themselves.

## Why This Closes Deals

### The Client Pitch
```
"When our AI transfers a call to you, you won't hear 'hello, how
can I help you?' You'll hear: 'Transferring Sarah. She wants a
root canal consultation. She has Delta Dental insurance. She's
available Tuesday or Thursday mornings. She's nervous about the
procedure.' You walk into that conversation like you already know her.

Because you do. ARIA briefed you."
```

### The Competitive Moat
No AI phone service does this. Smith.ai's humans take notes but don't
whisper-brief. Ruby's receptionists announce the caller's name only.
Goodcall, Dialzara, Bland — none have warm transfer with context synthesis.

This single feature can be the reason a prospect chooses InSync over
every competitor: "Their AI doesn't just transfer calls. It PREPARES you."

## Technical Implementation

### Method A: Whisper Bridge (Preferred)
```
1. ARIA determines escalation is needed
2. ARIA to caller: "Let me connect you with [Name]. One moment please."
3. ARIA places caller on brief hold (music or silence)
4. Twilio initiates call to business owner/manager
5. When human answers, ARIA speaks the context brief (human hears it, caller doesn't)
6. After brief (5-10 seconds), Twilio bridges the calls together
7. Human and caller are now connected
8. ARIA drops off the call

TWILIO IMPLEMENTATION:
- Use Twilio's <Dial> with whisper parameter
- Or: Conference call with mute/unmute control
- Whisper content generated by Claude from call transcript in real-time
```

### Method B: SMS Brief + Transfer (Simpler Fallback)
```
1. ARIA determines escalation is needed
2. ARIA to caller: "Let me connect you with [Name]. One moment."
3. ARIA sends SMS to business owner with context brief
4. Simultaneously transfers call via Twilio
5. Human sees SMS, answers phone with context

ADVANTAGE: Simpler to implement
DISADVANTAGE: Human might not read SMS fast enough
```

### Method C: Push Notification Brief (Future)
```
If dashboard/app exists:
1. Push notification to client's phone with context card
2. Client swipes, sees full brief, taps "Accept Transfer"
3. Call connects
```

## Context Brief Generation

ARIA uses the conversation transcript + Claude to generate a brief:

```python
brief_prompt = f"""
Summarize this phone conversation into a 15-second spoken brief
for the business owner who is about to take over the call.

Include:
- Caller's name (if given)
- What they're calling about (specific, not vague)
- Any key details (insurance, budget, timeline, preferences)
- Caller's emotional state (friendly, frustrated, urgent, casual)
- What the caller is expecting next

Keep it under 40 words. Speak naturally, not like a report.

Transcript:
{transcript_so_far}
"""
```

**Example outputs:**
- "Transferring Mike. Oil change for a 2019 Camry. Wants to know if you have synthetic. Available this afternoon. Relaxed, easy conversation."
- "Transferring Jennifer. New patient, needs a cleaning and consultation. Has Aetna PPO. Prefers morning appointments. She's comparing two offices."
- "Transferring David. His AC isn't cooling. Has been waiting since yesterday. He's frustrated but polite. Wants a same-day tech if possible."

## Build Priority
| When | Trigger |
|------|---------|
| Phase 1-2 (10+ clients) | Start with Method B (SMS brief) — simplest |
| Phase 2 (25+ clients) | Upgrade to Method A (whisper bridge) |
| Phase 3 | Add Method C (push notification via dashboard) |

**Method B can be built in a day.** When ARIA decides to escalate:
send an SMS to the business owner with context, then transfer the call.
That alone is a feature nobody else offers.


# ═══════════════════════════════════════════════════════════════════════════════
# 5. SYMPHONY — OpenClaw as the Nerve Center
# ═══════════════════════════════════════════════════════════════════════════════
#
# This is the ultimate vision. The thing nobody else is building.
# Ian, sitting anywhere in the world, commanding his entire company
# through a WhatsApp conversation with Aria on OpenClaw.

## The Vision

```
Ian (WhatsApp, 7:03 AM, from bed):
  "Morning Aria. How'd we do overnight?"

Aria:
  "Good morning. Mel handled 4 after-hours calls for Venice Barbershop.
  One new lead from the dental campaign responded — Dr. Patel in
  Bradenton, wants a demo Thursday. AnswrdBy got 3 new signups
  overnight, all Starter tier. MRR is $2,347 as of this morning.
  Your first call is at 10 AM with the Sarasota Vet Group.
  I prepared your pre-call brief. Want me to send it?"

Ian:
  "Send the brief. Also scrape dental offices in Manatee County today."

Aria:
  "Brief sent. Starting Manatee County dental scrub now.
  Anything else before your 10 AM?"

Ian:
  "How's the Great Clips pilot going?"

Aria:
  "Week 2 of 4. Three locations active. 847 calls handled total.
  Average 41 calls per location per day. Zero escalations.
  Most common question: wait time. GM hasn't provided feedback
  yet — I have a check-in scheduled for tomorrow. Want me to
  move it up?"

Ian:
  "Yeah, check in today. And send John his monthly report."

Aria:
  "Done. John's report sent. Great Clips GM check-in moved to
  this afternoon. I'll send you the outcome.

  One flag: our ElevenLabs usage is trending 15% over last month.
  At this rate we'll need to upgrade the plan by May. Want me
  to apply for the grants program again?"

Ian:
  "Yes, draft the email. I'll review tonight."

Aria:
  "Drafted and queued for your review. Have a good morning."
```

**That's Symphony. One conversation. Entire company.**

## What Makes This More Than a Chatbot

Most AI assistants ANSWER questions. Symphony EXECUTES commands:

| Input | What Aria Does |
|-------|---------------|
| "How many calls did Mel handle today?" | Queries Supabase → returns number |
| "Send John his monthly report" | Generates report from data → sends via Resend |
| "Scrape dental offices in 34205" | Runs Google Places scrub → adds to Lead Database |
| "Draft a cold email for Dr. Patel" | Pulls from SALES_PLAYBOOKS → personalizes → queues for review |
| "What's our MRR?" | Queries Stripe read-only → calculates → responds |
| "Check in with all clients this week" | Triggers check-in emails for all clients on this week's cadence |
| "How's the content performing?" | Pulls Google Sheets Content Performance → summarizes |
| "Post the LinkedIn draft you wrote this morning" | Publishes to LinkedIn (if pre-approved format) |
| "What's in the pipeline?" | Reads Pipeline sheet → summarizes by stage |
| "Apply for 5 podcasts this week" | Researches, drafts pitches, queues for Ian's review |
| "Start onboarding Dr. Patel" | Triggers Division 4: DocuSign + Stripe + welcome sequence |
| "Kill the insurance vertical outreach" | Pauses all outreach to insurance leads, notes in sheet |
| "How much runway do we have?" | Calculates from Stripe + cost data → responds |
| "Send me everything on Jack Leaf" | Pulls CLIENT_REGISTRY + OUTREACH_TRACKER → sends summary |

## Technical Implementation on OpenClaw

This is already mostly built. OpenClaw + Claude API + the 25 knowledge files +
connected APIs = Symphony. The key additions:

### OpenClaw Skills That Enable Symphony

| Skill | What It Does | Status |
|-------|-------------|--------|
| sheets-manager | Read/write Google Sheets | Build Week 1 |
| email-engine | Send emails via Resend | Build Week 1 |
| lead-scrubber | Run Google Places + Yelp scrubs | Build Week 1 |
| stripe-reader | Query Stripe for financial data | Build Week 1 |
| supabase-reader | Query call logs and agent metrics | Build Week 2 |
| calendly-manager | Read bookings, share links | Build Week 2 |
| linkedin-poster | Publish to LinkedIn | Build Week 3 |
| certusrodo-logger | Log every action to CertusOrdo | Build Week 2 |
| report-generator | Compile data from multiple sources into formatted reports | Build Week 2 |
| client-onboarder | Orchestrate full onboarding flow from a single command | Build Week 2 |

### The Command Language

Ian doesn't need to learn special syntax. He just talks naturally:
- "How's the business?" → Daily briefing
- "Send the thing to the guy" → Aria asks: "Send John's monthly report?"
- "That dental lead from yesterday" → Aria knows: Dr. Patel from Outreach Tracker
- "Do the scrub" → Aria knows: run the lead generation scrub per current targets

Aria maintains CONTEXT across the conversation. OpenClaw's persistent memory
means she remembers what Ian said 3 messages ago, yesterday, and last week.

### Voice Command (Future — OpenClaw Supports This)

OpenClaw supports voice input. When Voice Wake is configured:
- Ian says "Hey Aria" → Omen wakes up
- Ian speaks his command naturally
- Aria processes and responds via WhatsApp (or voice via ElevenLabs TTS)

This means Ian can literally TALK to his company while driving, walking,
or doing anything. No screen. No keyboard. Just voice.

```
[Ian, driving to a meeting]
"Hey Aria, give me a 30-second prep for my call with Dr. Patel."

[Aria, via ElevenLabs voice through phone speaker]
"Dr. Patel runs a general dentistry practice in Bradenton.
Six operatories, three hygienists. He responded to your email
about missed patient calls. He's losing an estimated 5 new patients
per week to voicemail. At $1,200 lifetime value per patient,
that's $312,000 per year. He asked about HIPAA compliance —
mention our CertusOrdo audit trail. He's comparing us to Ruby
Receptionists. Lead with price: we're a third of their cost."
```

**That's the nerve center. That's Symphony.**

## Why This Is Unfair Competitive Advantage

No competitor is building this because no competitor has:
- An AI that runs their own company (Aria)
- A trust layer that governs AI actions (CertusOrdo)
- A voice agent platform that serves customers (InSync AI)
- A consumer AI product with viral potential (AnswrdBy)
- All of it commanded from one interface (OpenClaw)

The typical AI agent company has ONE product. InSync has an ECOSYSTEM
controlled from a single nerve center. That's the pitch to investors.
That's the pitch to telecoms. That's the pitch to acquirers.

"We didn't build an AI phone agent. We built the operating system
for AI-powered business operations. And we're our own first customer."

## Build Priority
| Component | When | Notes |
|-----------|------|-------|
| Basic Symphony (text commands via WhatsApp) | Week 1-4 (FIRST_30_DAYS) | This is literally what we're deploying |
| Advanced Symphony (multi-step commands) | Month 2-3 | Aria chains multiple skills per request |
| Voice Symphony (spoken commands) | Month 4-6 | OpenClaw voice wake + ElevenLabs TTS |
| Full Nerve Center (all products, all data) | Month 6-12 | Every metric, every action, one conversation |


# ═══════════════════════════════════════════════════════════════════════════════
# SUMMARY: WHAT THIS DOCUMENT ADDS
# ═══════════════════════════════════════════════════════════════════════════════
#
# 5 features that were missing or underspecified:
#
# 1. MULTI-TENANT DASHBOARD — turns service into SaaS (10-20x valuation)
# 2. ARIA OUTBOUND — doubles revenue per client with same infrastructure
# 3. CERTUSRODO × CALLS — 50 lines of code creates a compliance moat
# 4. WARM TRANSFER — the feature that closes deals vs every competitor
# 5. SYMPHONY — the nerve center vision that makes InSync uncloneable
#
# New Aria Division: 19 (Outbound Campaign Management)
# New Sales Angles: Outbound pitch, warm transfer pitch, compliance pitch
# New Revenue Streams: Outbound add-on ($200-500/mo per client)
# New Competitive Moat: CertusOrdo-verified call transcripts
#
# "The company that owns the operating system for small business AI
#  doesn't just answer phones. It runs the entire business."
#
# ═══════════════════════════════════════════════════════════════════════════════
# END OF PRODUCT ROADMAP & TECHNICAL SPECS
# ═══════════════════════════════════════════════════════════════════════════════
