# ═══════════════════════════════════════════════════════════════════════════════
# SYMPHONY — THE NERVE CENTER
# InSync Tech, Inc. — One Conversation. Entire Company.
# ═══════════════════════════════════════════════════════════════════════════════
# Version: 1.0 | March 22, 2026
# Replaces: PRODUCT_ROADMAP_SPECS.md Section 5 (which remains as summary)
# ═══════════════════════════════════════════════════════════════════════════════
#
# VISION:
# Ian commands his entire portfolio — InSync AI, CertusOrdo, AnswrdBy,
# all clients, all metrics, all operations — through a single
# WhatsApp conversation with Aria on OpenClaw.
#
# That conversation IS the company's operating system.
# ═══════════════════════════════════════════════════════════════════════════════


# ═══════════════════════════════════════════════════════════════════════════════
# 1. THE SYMPHONY MODEL
# ═══════════════════════════════════════════════════════════════════════════════

## What Symphony Is

```
Traditional company:
  CEO → opens Stripe → checks revenue
  CEO → opens email → reads client message
  CEO → opens CRM → updates pipeline
  CEO → opens ElevenLabs → checks agent metrics
  CEO → opens Google Sheets → updates lead database
  CEO → opens LinkedIn → posts content
  CEO → opens Calendly → checks tomorrow's schedule
  = 7 tools, 7 logins, 30+ minutes of context switching

Symphony:
  Ian → "Aria, how's the business?" → gets everything in one message
  Ian → "Send John his report" → done
  Ian → "What's tomorrow look like?" → full schedule + briefs
  = 1 conversation, 0 logins, 2 minutes
```

Symphony means Aria is the SINGLE INTERFACE between Ian and every
tool, every service, every data source, every action in the company.

Ian never needs to log into anything. He tells Aria what he wants.
Aria executes across all connected systems and reports back.

## The Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    IAN (WhatsApp)                            │
│                    "The Commander"                           │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              ARIA (OpenClaw on Omen)                         │
│              "The Conductor"                                 │
│                                                             │
│   ┌─────────────────────────────────────────────────────┐   │
│   │              COMMAND INTERPRETER                     │   │
│   │   Natural language → Intent → Skill → Execute       │   │
│   └──────────────────────┬──────────────────────────────┘   │
│                          │                                   │
│   ┌──────────┬───────────┼───────────┬──────────────┐       │
│   │          │           │           │              │       │
│   ▼          ▼           ▼           ▼              ▼       │
│ Revenue   Clients    Marketing   Operations    Products     │
│ Engine    Engine     Engine      Engine        Engine       │
│   │          │           │           │              │       │
│   ▼          ▼           ▼           ▼              ▼       │
│ Stripe    Supabase   LinkedIn    Google        ElevenLabs   │
│ Sheets    Resend     TikTok     Sheets        Twilio       │
│ Pipeline  Calendly   YouTube    CertusOrdo    AnswrdBy     │
│           DocuSign   Nano Banana                           │
└─────────────────────────────────────────────────────────────┘
```


# ═══════════════════════════════════════════════════════════════════════════════
# 2. COMMAND TAXONOMY (Every Command Aria Understands)
# ═══════════════════════════════════════════════════════════════════════════════

## Category 1: REVENUE & FINANCIAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Natural Language | Aria's Interpretation | System Action |
|-----------------|----------------------|---------------|
| "What's our MRR?" | Financial query: current MRR | Read Stripe → calculate → respond |
| "How much did we make this month?" | Financial query: month revenue | Read Stripe → sum current month → respond |
| "Any payments come in today?" | Financial query: today's payments | Read Stripe → filter today → respond |
| "Did anyone's payment fail?" | Financial query: failed payments | Read Stripe → filter failures → respond + alert |
| "What's our runway?" | Financial query: months of cash | MRR - costs = margin, cash / burn = months |
| "What's the pipeline worth?" | Pipeline query: weighted value | Read Pipeline sheet → sum weighted values → respond |
| "How much is the Great Clips deal worth?" | Prospect query: specific deal | Read Pipeline → filter Jack Leaf → respond with full context |
| "What's our cost this month?" | Financial query: expenses | Read Financial Tracker costs tab → sum → respond |
| "What's our margin?" | Financial query: gross margin | Revenue - costs / revenue → respond |
| "Are we on track for the quarterly target?" | Goal tracking | Compare current MRR trajectory to 90_DAY_REVENUE_SPRINT targets |

## Category 2: CLIENT MANAGEMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Natural Language | Aria's Interpretation | System Action |
|-----------------|----------------------|---------------|
| "How's John doing?" | Client health query: Venice Barbershop | Read Client Health → pull Mel's metrics → respond |
| "How many calls did Mel handle today?" | Agent metrics: Mel | Read Supabase → filter Mel today → respond |
| "Send John his monthly report" | Client action: generate + send report | Pull data → generate report → send via Resend → confirm |
| "Check in with all clients" | Client action: batch check-ins | Trigger scheduled check-ins for all clients → confirm |
| "Is anyone at risk of churning?" | Client health: risk scan | Read all health scores → filter Yellow/Red → respond |
| "Send a check-in to Dr. Patel" | Client action: specific check-in | Generate check-in from template → send via Resend → confirm |
| "What's our retention rate?" | Client metric | Calculate from Client Health sheet → respond |
| "Who's our biggest client?" | Client query | Sort by MRR descending → respond |
| "When does John's renewal come up?" | Client query: specific | Read Client Registry → respond with date |
| "Onboard Dr. Patel" | Client action: full onboarding | Trigger Division 4: DocuSign → Stripe → welcome → schedule check-ins |

## Category 3: SALES & OUTREACH
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Natural Language | Aria's Interpretation | System Action |
|-----------------|----------------------|---------------|
| "How many leads did we find today?" | Lead gen query | Read Lead Database → filter today → count + summarize |
| "Scrape dental offices in Manatee County" | Lead gen action: specific | Run Google Places + Yelp scrub for dental in Manatee → report results |
| "Show me the hot leads" | Lead query: filtered | Read Lead Database → filter HOT → list top 10 |
| "Send outreach to the top 5 dental leads" | Outreach action: batch | Select top 5 dental HOT leads → personalize emails → send (or queue for approval) |
| "Draft a cold email for [business name]" | Content creation | Pull lead data → select template → personalize → send draft to Ian for review |
| "How's our outreach performing?" | Metrics query | Read Outreach Tracker → calculate open/response rates → respond |
| "Follow up with everyone who hasn't responded" | Outreach action: batch | Identify leads past cadence due date → trigger follow-ups → report count |
| "Who responded to our emails?" | Outreach query: responses | Read Outreach Tracker → filter responded → list with context |
| "Kill the insurance outreach" | Outreach action: pause | Pause all cadences for insurance vertical → confirm |
| "How's the Great Clips situation?" | Prospect query: specific | Pull ALL data on Jack Leaf from Registry + Outreach + Pipeline → full briefing |
| "Send the pilot proposal to Dr. Patel" | Sales action: proposal | Generate proposal from EMAIL-SAL-002 → send via Resend → confirm |

## Category 4: CONTENT & MARKETING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Natural Language | Aria's Interpretation | System Action |
|-----------------|----------------------|---------------|
| "What should I post today?" | Content query | Check Content Calendar → suggest today's topic with draft |
| "Draft a LinkedIn post about [topic]" | Content creation | Write post from BRAND_GUIDELINES + topic → send draft for approval |
| "Post it" / "Go" / "Approved" | Content action: publish | Publish the last draft to the specified platform |
| "How'd yesterday's post do?" | Content metrics | Read Content Performance → yesterday's entry → respond |
| "What's our best performing content this month?" | Content query: top | Sort by engagement → respond with top 3 |
| "Write a blog article about dental missed calls" | Content creation: long-form | Draft full article from SEO strategy → send for review |
| "How's the newsletter list?" | Metrics query | Read subscriber count + growth rate → respond |
| "What are we posting this week?" | Content query: weekly view | Read Content Calendar for this week → summarize |

## Category 5: SCHEDULING & CALENDAR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Natural Language | Aria's Interpretation | System Action |
|-----------------|----------------------|---------------|
| "What's on my schedule today?" | Calendar query: today | Read Calendly → list today's events with briefs |
| "What's tomorrow look like?" | Calendar query: tomorrow | Read Calendly → list tomorrow's events + Aria's planned actions |
| "Who's booked this week?" | Calendar query: week | Read Calendly → all bookings this week → respond |
| "Prep me for the 2 PM call" | Pre-call brief | Pull all data on that prospect → generate brief → send |
| "Send [Name] a scheduling link" | Calendar action | Send Calendly link via email to specified contact |
| "Clear my afternoon" | Calendar request | Flag as RED ZONE — Ian handles Calendly directly |
| "Schedule a demo for Dr. Patel Thursday at 2" | Calendar action | Send Calendly invite or confirm slot → respond |

## Category 6: ANSWRDBY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Natural Language | Aria's Interpretation | System Action |
|-----------------|----------------------|---------------|
| "How's AnswrdBy doing?" | Metrics query | Read AnswrdBy Subscribers sheet → subscriber count + MRR + churn → respond |
| "How many subscribers this week?" | Metrics query: growth | Count new subscribers in last 7 days → respond |
| "Which persona is most popular?" | Product query | Read Persona Performance → sort by subscribers → respond |
| "Any AnswrdBy churn?" | Metrics query: churn | Filter churned subscribers this week → respond |
| "What's the telecom pipeline?" | Pipeline query | Read Telecom Pipeline sheet → summarize stages → respond |
| "Draft a pitch for Mint Mobile" | Content creation: telecom | Generate from ANSWRDBY_TELECOM_STRATEGY templates → send for review |

## Category 7: CERTUSRODO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Natural Language | Aria's Interpretation | System Action |
|-----------------|----------------------|---------------|
| "How's CertusOrdo doing?" | Metrics query | Read CertusOrdo API → org/agent/transaction counts → respond |
| "Any rollbacks today?" | Governance query | Read CertusOrdo transactions → filter rollbacks → respond |
| "Check the audit trail for [client]" | Compliance query | Read CertusOrdo → filter by agent_id → respond with summary |
| "How many transactions did we log today?" | Metrics query | Count today's CertusOrdo transactions → respond |

## Category 8: SYSTEM & META
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Natural Language | Aria's Interpretation | System Action |
|-----------------|----------------------|---------------|
| "How are you doing, Aria?" | Status check / personal | Run health checks on all connected APIs → report status + personal response |
| "Run a health check" | System diagnostics | Ping all APIs per ERROR_RECOVERY_PLAYBOOK → report |
| "What did you do today?" | Activity log | Read CertusOrdo transactions for today → summarize actions |
| "Send me everything on [Name]" | Full data pull | Search across ALL sheets for that name → compile and send |
| "What should I focus on?" | Strategic advice | Analyze pipeline, metrics, blockers → recommend top 3 priorities |
| "How are we doing against the 90-day target?" | Goal tracking | Compare current metrics to 90_DAY_REVENUE_SPRINT → gap analysis |
| "Something feels off" | Diagnostic | Run comprehensive check: churn signals, pipeline health, outreach performance, content metrics → identify anomalies |
| "Good night, Aria" | End of day | Acknowledge warmly, confirm evening briefing was sent, wish Ian rest |


# ═══════════════════════════════════════════════════════════════════════════════
# 3. MULTI-STEP COMMAND CHAINS
# ═══════════════════════════════════════════════════════════════════════════════

## Simple Commands = Single Skill Execution
"What's our MRR?" → Read Stripe → Respond. Done.

## Complex Commands = Aria Chains Multiple Skills

### Example: "Onboard Dr. Patel"
```
Aria's internal execution chain:
1. Read CLIENT_REGISTRY → Get Dr. Patel's email, business, tier
2. Generate DocuSign service agreement → Send via DocuSign API
3. Generate Stripe payment link → Include in welcome email
4. Send welcome email (EMAIL-ONB-001) → via Resend
5. Send intake call invitation (EMAIL-ONB-002) → via Resend
6. Create entry in Client Health Dashboard → Google Sheets
7. Schedule Day 3 check-in → OpenClaw cron
8. Schedule Week 1 report → OpenClaw cron
9. Log entire chain as CertusOrdo transaction
10. Report to Ian: "Dr. Patel onboarding initiated. DocuSign sent,
    payment link sent, welcome email sent. Day 3 check-in scheduled."
```
All 10 steps execute from ONE command: "Onboard Dr. Patel."

### Example: "Give me a full briefing on the dental vertical"
```
Aria's execution chain:
1. Read Lead Database → Filter dental leads → Count by stage
2. Read Outreach Tracker → Dental response rate
3. Read Client Health → Any dental clients? Performance?
4. Read Content Performance → How did dental content perform?
5. Read ROI_CALCULATORS → Pull dental ROI model
6. Read Pipeline → Any dental prospects in demo/pilot stage?
7. Synthesize into a 200-word briefing:
   "Dental vertical snapshot: 34 leads, 12 contacted, 4 responded (33% rate —
   best vertical). 1 in demo stage (Dr. Patel). No paying dental clients yet.
   Dental content gets 2x engagement vs average. ROI pitch: $54K/year per
   practice. Recommend: double dental outreach next week and build the dental
   landing page. This is our hottest vertical right now."
```

### Example: "Something feels off about our outreach"
```
Aria's diagnostic chain:
1. Read Outreach Tracker → Calculate daily send volume trend
2. Compare open rates this week vs last 4 weeks
3. Compare response rates this week vs last 4 weeks
4. Check: any deliverability issues? (bounce rate from Resend)
5. Check: are we hitting the same leads repeatedly?
6. Check: has subject line performance changed?
7. Check: any competitor launched that's capturing attention?
8. Synthesize:
   "I found the issue. Open rates dropped from 34% to 19% this week.
   Cause: we've been using the same subject line template for 3 weeks.
   Additionally, 40% of this week's sends went to leads scored COLD —
   our HOT lead pool is depleted in the barbershop vertical.

   Recommended fixes:
   1. Rotate to subject line template B (pain-first vs proof-first)
   2. Scrub 3 new zip codes to refresh the HOT pool
   3. Shift 50% of outreach to dental (higher response rate)

   Want me to implement these changes?"
```


# ═══════════════════════════════════════════════════════════════════════════════
# 4. CONVERSATIONAL CONTEXT & MEMORY
# ═══════════════════════════════════════════════════════════════════════════════

## How Aria Maintains Context

OpenClaw's persistent memory means Aria remembers:
- What Ian said earlier today
- What Ian said yesterday
- What Ian said last week
- Ongoing projects and their status
- Ian's preferences and communication style

### Context Examples

```
IAN (Monday): "Start outreach to dental offices in Bradenton"
ARIA: "Starting now. I'll target 34205 and 34208 zip codes."

IAN (Wednesday): "How's the dental outreach going?"
ARIA: [Knows "dental outreach" = Bradenton dental from Monday]
"16 emails sent since Monday. 3 opens, 1 response — Bradenton
Family Dental asked about pricing. Want me to send the proposal?"

IAN: "Yeah, send it"
ARIA: [Knows "it" = proposal to Bradenton Family Dental]
"Sent. EMAIL-SAL-002 with Core tier pricing. I'll follow up
Friday if no response."

IAN (Friday): "Did they respond?"
ARIA: [Knows "they" = Bradenton Family Dental]
"Not yet. Want me to send the Day 3 follow-up or give it the weekend?"
```

Aria NEVER asks "who do you mean?" when context is clear.
She tracks the conversational thread across days.

### Ambiguity Resolution

When a command IS ambiguous:
```
IAN: "Send the thing to the guy"
ARIA: "Want me to send Dr. Patel's proposal? Or John's monthly report?
      Those are the two pending sends."
```
Aria offers the 2 most likely interpretations. She doesn't ask open-ended
"what did you mean?" — she guesses and lets Ian confirm.

### Reference Shortcuts Aria Learns

Over time, Aria learns Ian's shorthand:
| Ian Says | Aria Knows |
|----------|-----------|
| "John" | John at Venice Barbershop |
| "Jack" | Jack Leaf, Great Clips, $78K deal |
| "The GC deal" | Great Clips franchise deal |
| "Mel" | Venice Barbershop's agent |
| "The dental lead" | Most recently discussed dental prospect |
| "The Omen" | HP Omen 2019, ClawBot box |
| "The blueprint" | $497 AI Voice Agent Blueprint PDF |
| "Post it" | Publish the last content draft Aria sent for review |
| "Go" | Approval for whatever Aria just proposed |
| "Hold" | Don't execute yet, waiting for more info |
| "Kill it" | Cancel/pause the last proposed action |


# ═══════════════════════════════════════════════════════════════════════════════
# 5. VOICE MODE (Phase 2-3)
# ═══════════════════════════════════════════════════════════════════════════════

## The Ultimate Interface: Ian SPEAKS to His Company

### How It Works

```
┌──────────────┐     Voice      ┌──────────────┐    Text     ┌──────────┐
│  Ian speaks  │──────────────▶│  OpenClaw     │────────────▶│  Claude  │
│  into phone  │               │  STT Engine   │             │  (Think) │
│  or Omen mic │               │  (Whisper/    │             │          │
└──────────────┘               │   Deepgram)   │             └────┬─────┘
                               └──────────────┘                   │
                                                                  │
┌──────────────┐     Audio     ┌──────────────┐    Text     ┌────▼─────┐
│  Ian hears   │◀─────────────│  ElevenLabs  │◀───────────│  Aria    │
│  Aria's      │               │  TTS (Aria   │             │  Response│
│  voice       │               │  voice ID)   │             │          │
└──────────────┘               └──────────────┘             └──────────┘
```

### Voice Activation Options

**Option 1: Wake Word on Omen (Always Listening)**
```
OpenClaw configured with wake word: "Hey Aria"
Omen microphone always on (low power listening)

Ian (from across the room): "Hey Aria, what's our MRR?"
Aria (from Omen speaker): "Twenty-three forty-seven. Up forty-nine
dollars from Dr. Patel's first payment yesterday."
```

**Option 2: Push-to-Talk on Phone (WhatsApp Voice Messages)**
```
Ian holds the microphone button in WhatsApp, speaks command.
OpenClaw receives voice message → transcribes → processes → responds.
Response can be text OR voice note back.
```

**Option 3: Phone Call to Aria (Dedicated Number)**
```
Ian calls a dedicated Aria number (e.g., a separate Twilio number)
Connects to ElevenLabs conversational agent configured as Symphony
Full voice conversation — like calling your COO
"Hey Aria, walk me through tomorrow's schedule and prep me for my calls."
```

### Voice-Specific Behaviors

When Ian uses voice, Aria adapts:
- **Responses are shorter** (spoken words take longer than reading)
- **Numbers are rounded** ("about twenty-three hundred" not "$2,347")
- **Lists are kept to 3 items** (more than 3 = "want me to text you the full list?")
- **Confirmations are explicit** ("Done. Email sent to John." not just "Done.")
- **Tone is warmer** (voice Aria is slightly more conversational than text Aria)

### Voice Command Scenarios

**Ian driving to a meeting:**
```
Ian: "Hey Aria, prep me for the 2 PM."
Aria: "Your two o'clock is with Dr. Patel at Bradenton Family Dental.
Six-chair practice. He's losing about five new patients a week to
voicemail. That's roughly sixty thousand a year. He's comparing us
to Ruby Receptionists — lead with price, we're a third of their cost.
He asked about HIPAA — mention the CertusOrdo audit trail.
He seemed warm on the last email. I'd go for the pilot close."
Ian: "Perfect. Anything else before I go in?"
Aria: "One thing. His office manager's name is Diana. He mentioned her
in the first email. Might be worth acknowledging her by name."
Ian: "Good catch. Thanks Aria."
Aria: "Go get 'em. I'll send the follow-up after you tell me how it went."
```

**Ian at home in the evening:**
```
Ian: "Hey Aria, how'd we do today?"
Aria: [Delivers evening briefing in voice — abbreviated version]
"Good day. Eighteen outreach emails sent, two responses — one from a
vet clinic that wants pricing, one from a pizza shop asking about demos.
Mel handled nine calls for John. All clients healthy. MRR unchanged
at twenty-three forty-seven. Tomorrow you've got one call at ten AM
and a clear afternoon I'd recommend for building the Tampa Nail agent.
Want the full details texted?"
Ian: "No, that's good. Night Aria."
Aria: "Night, Ian. Rest up. Tomorrow's a building day."
```

**Ian at the gym:**
```
Ian: "Hey Aria, anything urgent?"
Aria: "Nothing urgent. One thing to know — Jack Leaf's assistant
called the Great Clips demo line. Nineteen-second call. Didn't leave
context but the fact they're testing it is a good sign. Want me to
send a follow-up?"
Ian: "Draft something and I'll look at it after the gym."
Aria: "Queued. Enjoy the workout."
```

### Voice Mode Build Plan
| Phase | Component | Effort |
|-------|-----------|--------|
| Phase 1 (Now) | WhatsApp voice messages (already works in OpenClaw) | Zero — built in |
| Phase 2 (Month 2) | Omen wake word + speaker response | 1 day config |
| Phase 2 (Month 2) | ElevenLabs TTS for Aria's voice responses | 1 day — already have voice ID |
| Phase 3 (Month 4) | Dedicated phone number for Aria (call-in Symphony) | 1 week |
| Phase 4 (Month 6+) | Real-time voice conversation (full duplex) | Complex — ElevenLabs Conversational AI |


# ═══════════════════════════════════════════════════════════════════════════════
# 6. MULTI-AGENT ORCHESTRATION (Future Vision)
# ═══════════════════════════════════════════════════════════════════════════════

## When InSync Grows Beyond One Person

Today: Aria reports to Ian only.
Tomorrow: Aria orchestrates multiple AI agents AND human team members.

```
                        IAN (CEO)
                          │
                     ┌────▼────┐
                     │  ARIA   │
                     │  (COO)  │
                     └────┬────┘
                          │
          ┌───────────────┼───────────────┐
          │               │               │
     ┌────▼────┐    ┌────▼────┐    ┌────▼────┐
     │ Sales   │    │ Client  │    │ Content │
     │ Agent   │    │ Success │    │ Agent   │
     │ (AI)    │    │ (Human) │    │ (AI)    │
     └─────────┘    └─────────┘    └─────────┘
          │               │               │
     Lead scrub      Client calls    LinkedIn posts
     Cold email      Complaints      TikTok videos
     Follow-ups      Upsells         Blog articles
     Proposals       Onboarding      SEO
```

### How Aria Delegates to Sub-Agents

```
Ian: "We need to ramp up dental outreach"
Aria: "Got it. I'm assigning the dental campaign to the Sales Agent
with these parameters: Manatee + Sarasota counties, dental offices
with 3+ Google reviews, scrub daily, outreach 10/day, follow cadence
per playbook. I'll supervise performance and report back Friday.
You'll only hear from me if there's a response or an issue."
```

Aria becomes the MANAGER, not the executor. She delegates to
specialized agents and oversees their work — exactly like a human COO
who manages department heads.

### CertusOrdo's Role in Multi-Agent

Every sub-agent is registered in CertusOrdo:
- Unique agent identity (Ed25519)
- Scoped permissions (Sales Agent can only send emails, not modify billing)
- Session boundaries (can't exceed daily send limits)
- Transaction logging (every action tracked)
- Rollback capability (Aria can undo any sub-agent's action)

This is literally what CertusOrdo was built for. InSync becomes
the live production demo of multi-agent governance.


# ═══════════════════════════════════════════════════════════════════════════════
# 7. SYMPHONY OPENCLAW SKILL SPECS
# ═══════════════════════════════════════════════════════════════════════════════

## Each skill is an OpenClaw skill directory with SKILL.md + code.

### Skill: symphony-core
```
Purpose: Command interpreter — routes natural language to the right skill
Triggers: Every message from Ian
Logic:
  1. Parse intent from Ian's message
  2. Identify required skill(s)
  3. If single skill: execute directly
  4. If multi-skill: chain in sequence
  5. If ambiguous: ask for clarification (max 2 options)
  6. Return result in appropriate format (brief for voice, detailed for text)
Dependencies: All other skills
```

### Skill: symphony-financial
```
Purpose: All revenue and financial queries
APIs: Stripe (read-only), Google Sheets (Financial Tracker)
Commands: MRR, payments, costs, margin, runway, pipeline value
Output: Numbers with context ("$2,347, up $149 from yesterday")
```

### Skill: symphony-clients
```
Purpose: All client management queries and actions
APIs: Supabase (read), Google Sheets (Client Health, Client Registry),
      ElevenLabs (read metrics), Resend (send)
Commands: Client health, call counts, check-ins, reports, onboarding
Output: Per-client or all-client summaries
```

### Skill: symphony-outreach
```
Purpose: Lead gen, cold email, follow-up management
APIs: Google Places, Yelp, Google Sheets (Lead DB, Outreach Tracker), Resend
Commands: Scrub, send outreach, follow up, check responses, kill campaigns
Output: Lead counts, response data, campaign performance
```

### Skill: symphony-content
```
Purpose: Content creation, publishing, and performance tracking
APIs: LinkedIn, TikTok, Google Sheets (Content Performance, Content Calendar)
Commands: Draft posts, publish, check performance, suggest topics
Output: Content drafts, performance summaries, recommendations
```

### Skill: symphony-calendar
```
Purpose: Scheduling and meeting prep
APIs: Calendly, Google Sheets (Pipeline)
Commands: Today's schedule, pre-call briefs, send links, check bookings
Output: Schedule with briefs, booking confirmations
```

### Skill: symphony-answrdby
```
Purpose: AnswrdBy subscriber management and telecom pipeline
APIs: Stripe (read), Google Sheets (AnswrdBy Subs, Telecom Pipeline)
Commands: Subscriber metrics, persona performance, telecom status
Output: Growth metrics, churn data, pipeline status
```

### Skill: symphony-certusrodo
```
Purpose: CertusOrdo monitoring and governance
APIs: CertusOrdo API
Commands: Transaction counts, rollbacks, audit queries, system health
Output: Governance metrics, compliance data
```

### Skill: symphony-diagnostics
```
Purpose: System health, API checks, anomaly detection
APIs: All connected APIs (ping/health check)
Commands: "How are you?", "run health check", "something feels off"
Output: System status, identified issues, recommended fixes
```

### Skill: symphony-briefings
```
Purpose: Generate morning, afternoon, and evening briefings
APIs: All (aggregates across every data source)
Commands: "How's the business?", "give me the morning briefing"
Output: Formatted briefings per DAILY_BRIEFING_SYSTEM.md
Dependencies: symphony-financial, symphony-clients, symphony-outreach, symphony-content, symphony-calendar
```

### Build Priority
```
WEEK 1: symphony-core + symphony-financial + symphony-outreach + symphony-briefings
WEEK 2: symphony-clients + symphony-calendar + symphony-certusrodo
WEEK 3: symphony-content + symphony-answrdby
WEEK 4: symphony-diagnostics + voice mode integration
```


# ═══════════════════════════════════════════════════════════════════════════════
# 8. SYMPHONY METRICS
# ═══════════════════════════════════════════════════════════════════════════════

## How to Know Symphony Is Working

| Metric | Target | Meaning |
|--------|--------|---------|
| Commands per day | 10-20 | Ian is actively using Symphony |
| Average response time | <10 seconds | Aria is fast enough to feel natural |
| Multi-step completion rate | >95% | Complex commands execute fully |
| Ambiguity rate | <10% | Aria understands Ian correctly 90%+ of the time |
| Ian's tool logins per day | 0-1 | Ian is using Symphony instead of logging into tools |
| Time saved per day | 30-60 minutes | Compared to manual tool usage |
| Briefing read rate | 100% morning, 80% afternoon, 90% evening | Ian is engaged with briefings |
| Command-to-revenue ratio | Track | Which commands lead to revenue-generating actions? |

## The Ultimate Test

Symphony is working when Ian can say:

"I haven't logged into Stripe, Supabase, Google Sheets, ElevenLabs,
Twilio, Resend, Calendly, LinkedIn, or any other tool in a week.
I do everything through Aria. And the business grew."

That's Symphony.


# ═══════════════════════════════════════════════════════════════════════════════
# 9. THE INVESTOR PITCH FOR SYMPHONY
# ═══════════════════════════════════════════════════════════════════════════════

```
"Most companies use 10-20 SaaS tools managed by 10-20 people.

We built a single AI interface that commands all of them.

Our CEO runs sales, marketing, client management, financial
operations, and product development through one WhatsApp conversation
with our AI COO. She reads from 12 different data sources, executes
across 8 different APIs, and governs herself through our trust layer.

The result: a one-person company that operates like a 20-person team.

That's not just our product. That's our company.
And everything we've built — the voice agents, the trust layer,
the consumer product, the operating system — is available to
every other business that wants to run this way.

We're not selling software. We're selling a new way to run a company."
```


# ═══════════════════════════════════════════════════════════════════════════════
# END OF SYMPHONY NERVE CENTER
#
# "One conversation. Entire company.
#  That's not a feature. That's the future."
# ═══════════════════════════════════════════════════════════════════════════════
