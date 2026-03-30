# ═══════════════════════════════════════════════════════════════════════════════
# ARIA × OPENCLAW — AUTONOMOUS OPERATIONS ARCHITECTURE
# InSync Tech, Inc.
# ═══════════════════════════════════════════════════════════════════════════════
# Version: 1.0 | March 21, 2026
# Hardware: HP Omen (2019) — Dedicated ClawBot Box
# Primary Interface: WhatsApp (Ian's phone + M4 Mac)
# LLM Backend: Claude API (Anthropic)
# ═══════════════════════════════════════════════════════════════════════════════


# ═══════════════════════════════════════════════════════════════════════════════
# SECURITY PRIMER: WHAT THE CLAUDE API KEY ACTUALLY DOES
# ═══════════════════════════════════════════════════════════════════════════════
#
# The Claude API key lets ClawBot THINK (send prompts, get responses).
# It does NOT give access to:
#   - Your claude.ai conversations or projects
#   - Your chat history
#   - Your uploaded files on claude.ai
#   - Any other user's data
#   - Anthropic's internal systems
#
# The API is stateless. Prompt in → response out. That's it.
# ClawBot uses it as Aria's brain. Nothing more.
# ═══════════════════════════════════════════════════════════════════════════════


# TABLE OF CONTENTS
# 1. SYSTEM OVERVIEW & HARDWARE LAYOUT
# 2. PERMISSION ARCHITECTURE (The Wall)
# 3. THE 8 DIVISIONS (Everything Aria Does)
# 4. INTEGRATION MAP (Every Service Connection)
# 5. OPENCLAW SKILL ARCHITECTURE
# 6. DAILY AUTONOMOUS WORKFLOW (24-Hour Cycle)
# 7. SECURITY MODEL & CREDENTIAL ISOLATION
# 8. BUILD ORDER (Week 1 Setup Plan)


# ═══════════════════════════════════════════════════════════════════════════════
# 1. SYSTEM OVERVIEW & HARDWARE LAYOUT
# ═══════════════════════════════════════════════════════════════════════════════

## The Physical Setup

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   ┌──────────┐                           ┌──────────────────────────────┐   │
│   │  iPhone   │────── WhatsApp ─────────▶│     HP OMEN 2019             │   │
│   │  (pocket) │◀──── messages ──────────│     "ARIA'S BRAIN"           │   │
│   └──────────┘                           │                              │   │
│                                          │   OpenClaw + Claude API      │   │
│   ┌──────────┐                           │                              │   │
│   │  M4 Mac  │   NO DIRECT CONNECTION    │   Aria lives here.          │   │
│   │  "HQ"    │   TO THE OMEN. EVER.      │   Runs 24/7.               │   │
│   │          │                           │   Plugged in. Ethernet.     │   │
│   │ Stripe   │                           │                              │   │
│   │ Twilio   │                           │   She can SEND emails       │   │
│   │ Railway  │                           │   She can READ data         │   │
│   │ GitHub   │                           │   She can POST content      │   │
│   │ ElevenLabs│                          │   She can SCHEDULE tasks    │   │
│   │ Code     │                           │   She can SCRUB leads       │   │
│   └──────────┘                           │   She CANNOT change code    │   │
│                                          │   She CANNOT touch billing  │   │
│   ┌──────────┐                           │   She CANNOT modify agents  │   │
│   │ 2008 Mac │                           │                              │   │
│   │  SELL IT │                           └──────────┬───────────────────┘   │
│   └──────────┘                                      │                       │
│                                                     ▼                       │
│                                          ┌──────────────────────┐           │
│                                          │   EXTERNAL SERVICES  │           │
│                                          │                      │           │
│                                          │  Resend (send email) │           │
│                                          │  Google Sheets (data)│           │
│                                          │  LinkedIn (post)     │           │
│                                          │  Calendly (schedule) │           │
│                                          │  DocuSign (send docs)│           │
│                                          │  Supabase (read logs)│           │
│                                          │  Stripe (read only)  │           │
│                                          │  Google Places (scrub)│          │
│                                          │  Yelp (scrub)        │           │
│                                          │  CertusOrdo (govern) │           │
│                                          └──────────────────────┘           │
└─────────────────────────────────────────────────────────────────────────────┘
```

## How Ian Talks to Aria

Ian sends a WhatsApp message from his phone or M4 Mac.
Aria responds in the same chat. That's the entire interface.

Aria also sends PROACTIVE messages:
- 9:00 AM: Daily briefing
- When a lead responds to cold outreach
- When a Calendly booking comes in
- When a payment succeeds or fails
- When a client shows churn signals
- When content is ready for approval
- Sunday 8 PM: Weekly report

Ian NEVER touches the Omen. It sits in the corner running. Aria lives there.


# ═══════════════════════════════════════════════════════════════════════════════
# 2. PERMISSION ARCHITECTURE (The Wall)
# ═══════════════════════════════════════════════════════════════════════════════

## The Golden Rule

  ARIA CAN:     Send things (emails, content, messages, documents, payment links)
  ARIA CAN:     Read things (metrics, logs, lead data, calendars, payment status)
  ARIA CAN:     Create things (leads, reports, drafts, schedules, calculations)
  ARIA CANNOT:  Change things (code, configs, credentials, billing, agents, prompts)
  ARIA CANNOT:  Delete things (data, accounts, records, files)
  ARIA CANNOT:  Access things (Ian's email inbox, bank accounts, production systems)

## Detailed Permission Matrix

### ✅ FULL ACCESS (Aria Operates Freely)

| Service | Access Type | What Aria Does | API Key Type |
|---------|------------|----------------|--------------|
| Claude API | Read/Write | Her brain — thinks, drafts, analyzes | Standard API key |
| Resend | Send-only | All outbound email from hello@insynctech.ai | Scoped sending key |
| Google Sheets | Read/Write | Lead database, pipeline, content calendar, reports | OAuth service account |
| Google Places API | Read-only | Scrape business listings for leads | Standard key |
| Yelp Fusion API | Read-only | Supplementary business data + reviews | Standard key |
| Calendly | Read + share links | Monitor bookings, share scheduling links | API key |
| CertusOrdo API | Full access | She IS the registered agent — logs every action | Agent credentials |
| WhatsApp (via OpenClaw) | Send/Receive | Talk to Ian, send proactive updates | OpenClaw integration |
| OpenClaw Cron | Full | Schedule all automated tasks | Built-in |
| Knowledge Base Files | Read-only | All 13 operating system .md files | Local filesystem |

### 🟡 LIMITED ACCESS (Aria Can Look But Not Touch)

| Service | Access Type | What She Can See | What She CANNOT Do |
|---------|------------|------------------|-------------------|
| Stripe API | READ-ONLY | MRR, payment status, upcoming renewals | Create charges, refunds, modify plans |
| Supabase | Read + insert-to-log | Call logs, agent metrics | Modify client data, delete records, schema changes |
| ElevenLabs API | Read metrics only | Call counts, duration, usage | Modify agents, change prompts, change voices |
| DocuSign API | Send templates only | Template status, signature status | Create new templates, modify agreements |

### 🔴 ZERO ACCESS (The Wall — Aria Never Touches These)

| Service | Why It's Blocked |
|---------|-----------------|
| Twilio Console/API (write) | Can provision numbers, change call routing — production risk |
| Railway Dashboard/CLI | Can deploy code, change env vars — production risk |
| GitHub (push access) | Can modify production code — production risk |
| ElevenLabs Agent Config (write) | Can change system prompts, voices — quality risk |
| Stripe Admin (write) | Can issue refunds, change pricing — financial risk |
| Supabase Admin | Can modify schema, delete data — data risk |
| Ian's Gmail/Google Account | Privacy boundary |
| Ian's bank/financial accounts | Absolute boundary |
| Any SSH/server access | Infrastructure risk |
| Any deployment tool | Code = Ian only |

### How Payment Links Work (Important Distinction)

Aria can SEND existing Stripe payment links in emails. She has the URLs:
- AI Starter ($799): https://buy.stripe.com/28E7sKa3c1Yr8EN9jI0ZW04
- AI Growth ($1,499): https://buy.stripe.com/4gMdR87V47iLaMV1Rg0ZW03
- AI Premium ($2,499): https://buy.stripe.com/aFa5kCfnw0Un1cl53s0ZW02

She pastes these links into proposal emails. She does NOT interact with Stripe's
billing system. The links are just URLs — like sharing a web address.

If a new payment link is needed (custom pricing), Ian creates it on M4 Mac and
tells Aria the URL via WhatsApp.


# ═══════════════════════════════════════════════════════════════════════════════
# 3. THE 8 DIVISIONS (Everything Aria Does)
# ═══════════════════════════════════════════════════════════════════════════════

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## DIVISION 1: LEAD GENERATION & DATA SCRUBBING
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Purpose
Find businesses that need AI phone agents. Build a pipeline of qualified leads
without Ian lifting a finger.

### What Aria Does (Autonomously)

1. SCRUB — Searches Google Places API + Yelp for target businesses
   - Filters by vertical: barbershops, dental, vet, auto service, pizza,
     insurance, real estate, urgent care, property mgmt, nail, tattoo, etc.
   - Filters by geography: starts with Tampa Bay 9 zip codes, expands to FL
   - Pulls: name, phone, address, website, hours, review count, rating, owner name

2. ENRICH — Visits business websites (BeautifulSoup scraping)
   - Extracts: email addresses, owner/manager names, social links
   - Checks: do they have an existing AI/answering service? (disqualify if yes)
   - Checks: do they have a website at all? (no website = less tech-savvy = different pitch)

3. SCORE — Assigns lead quality
   - HOT: 20+ reviews, no AI, high call volume vertical, owner email found
   - WARM: 10-20 reviews, moderate potential, limited contact info
   - COLD: Low reviews, low-call vertical, or already has a service

4. VALIDATE — Calls the business from test line
   - Got voicemail? → Lead score +2 (they NEED us)
   - Got a person? → Lead score neutral (still a prospect, but less urgent pain)
   - Got an AI/service? → Disqualify

5. LOG — Writes everything to Google Sheets "Lead Database"
   - Columns: Name, Phone, Email, Address, Website, Vertical, Score, Source,
     Date Found, Outreach Status, Notes

6. REPORT — WhatsApp to Ian: "Found 14 new leads today. 5 HOT. Sheet updated."

### Integrations
```
Google Places API ──→ Primary data source
Yelp Fusion API ──→ Secondary data + review data
Python (BeautifulSoup) ──→ Website scraping
Google Sheets API ──→ Lead database
OpenClaw Cron ──→ Runs 2x daily (6 AM + 2 PM ET)
WhatsApp ──→ Daily lead report to Ian
CertusOrdo ──→ Logs every scrub session as transaction
```

### Schedule
- 6:00 AM ET — Morning scrub (3 verticals × 3 zip codes = 9 searches)
- 2:00 PM ET — Afternoon scrub (3 different verticals × 3 zips)
- Rotates through all verticals weekly so no vertical gets stale

### Ian's Role
- Sets target verticals and geographies
- Reviews HOT leads and approves for outreach
- Can say "Focus on dental this week" and Aria adjusts

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## DIVISION 2: COLD OUTREACH & EMAIL CAMPAIGNS
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Purpose
Turn scraped leads into conversations. Automated, personalized, persistent
email sequences that nurture prospects toward a demo call.

### What Aria Does (Autonomously After Ian Approves Targets)

1. PERSONALIZE — Takes lead data from Google Sheets and builds email
   - Selects template from EMAIL_TEMPLATES.md based on vertical and stage
   - Fills in: business name, owner name, city, estimated missed revenue
   - Uses ROI_CALCULATORS.md formulas for the revenue estimate

2. SEND — Delivers via Resend API
   - From: hello@insynctech.ai
   - BCC: ian@insynctech.io (always)
   - Tracks: sent timestamp, subject line used, template version

3. FOLLOW CADENCE — Automated multi-touch sequence
   ```
   Day 1:  Initial outreach (pain-first or proof-first, rotated)
   Day 3:  Short follow-up ("bumping this up")
   Day 7:  Different angle + demo link or call recording
   Day 14: Value-add (industry stat or case study)
   Day 21: Final "closing the loop" email
   Day 30: Move to monthly nurture list
   Day 90: Re-engage with fresh angle / new case study
   ```

4. MONITOR — Checks Resend analytics
   - Opened? → Note in sheet, continue cadence
   - Replied? → STOP cadence, alert Ian via WhatsApp IMMEDIATELY
   - Bounced? → Remove from list, note bad email
   - Unsubscribed? → Remove permanently, log in CertusOrdo

5. ESCALATE — When someone responds
   - Positive response → WhatsApp to Ian: "[Name] from [Business] replied: [quote]. HOT."
   - Neutral response → WhatsApp to Ian with context + suggested reply
   - Negative response → Log, remove from cadence, WhatsApp to Ian as FYI
   - Booking → WhatsApp: "[Name] booked a demo for [date/time]. Pre-call brief incoming."

### Integrations
```
Resend API ──→ Send + track emails
Google Sheets API ──→ Lead status tracking
OpenClaw Cron ──→ Daily batch at 9:30 AM ET
WhatsApp ──→ Response alerts
CertusOrdo ──→ Every email = logged transaction
```

### Rules
- Max 20 new cold emails per day (reputation warm-up)
- Max 2 emails to same person in one day (including follow-ups)
- Never before 9 AM or after 6 PM recipient's local time
- Never send to .gov or .edu addresses
- Stop all outreach to a lead after 5 touches with no response → nurture
- Every email includes functioning unsubscribe mechanism

### Ian's Role
- Approves target lists before first send ("Go on these 15 HOT leads")
- Handles personal responses that need his voice
- Takes demo calls booked through outreach

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## DIVISION 3: SOCIAL MEDIA & CONTENT PUBLISHING
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Purpose
Build InSync Tech's brand presence. Drive inbound leads through consistent,
valuable content that demonstrates the product.

### What Aria Does

1. DRAFT — Creates content from CONTENT_CALENDAR.md
   - Monday/Wednesday/Friday: LinkedIn text posts
   - Tuesday/Thursday: TikTok/YouTube Shorts captions + descriptions
   - Uses BRAND_GUIDELINES.md for voice and tone
   - Personalizes with real metrics, client results, and ROI calculations

2. SUBMIT FOR APPROVAL — WhatsApp to Ian
   ```
   "Monday LinkedIn draft:

   [Full post text]

   Approve? Or changes needed?"
   ```

3. PUBLISH — After Ian says "Go"
   - LinkedIn: Posts via API or browser automation
   - TikTok: Uploads video that Ian recorded + sends to platform
   - YouTube Shorts: Cross-posts TikTok content

4. TRACK — Weekly engagement metrics
   - Impressions, likes, comments, shares per post
   - Which content types performed best
   - Follower growth
   - Logs to Google Sheets "Content Tracker"

5. OPTIMIZE — Monthly content review
   - "Your top post this month was [X] with [Y] impressions. Recommend more of this format."
   - Adjusts future content mix based on performance

### Content Aria CAN Publish (After Approval)
- LinkedIn text posts
- TikTok video uploads (Ian records, Aria uploads)
- YouTube Shorts (cross-post)
- LinkedIn article drafts

### Content Aria CANNOT Do
- Reply to comments as Ian (she can DRAFT replies, Ian posts them)
- DM prospects on LinkedIn (too personal, too risky)
- Create new social media accounts
- Run paid ads (requires billing access)

### Integrations
```
LinkedIn API / Browser ──→ Publish posts
TikTok Upload ──→ Video publishing
YouTube API ──→ Shorts cross-posting
Google Sheets API ──→ Content calendar + metrics
WhatsApp ──→ Draft approval flow
OpenClaw Cron ──→ Draft generation night before, publish after approval
```

### Ian's Role
- Records video content (screen recordings, call demos, talking head)
- Sends raw video to Aria via WhatsApp or shared folder
- Approves every text post before it goes live
- Engages with comments personally
- Identifies trending topics or timely content opportunities

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## DIVISION 4: CLIENT ONBOARDING & DOCUMENT DELIVERY
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Purpose
Turn a "yes" into a paying, onboarded, live client — with minimal
Ian involvement. Aria handles the paperwork. Ian handles the build.

### The Onboarding Flow

```
Ian closes deal ──→ WhatsApp to Aria: "Onboard [Name], [email], [business], [tier]"
                                │
                                ▼
                    ┌─────────────────────┐
                    │ ARIA SENDS (Day 0): │
                    │                     │
                    │ 1. DocuSign contract │──→ Service agreement template
                    │ 2. Stripe link      │──→ Setup + first month payment
                    │ 3. Welcome email    │──→ EMAIL-ONB-001
                    │ 4. Intake call link │──→ EMAIL-ONB-002
                    └─────────┬───────────┘
                              │
                    ┌─────────▼───────────┐
                    │ ARIA MONITORS:      │
                    │                     │
                    │ DocuSign signed? ───│──→ If yes: note in sheet
                    │ Stripe paid? ──────│──→ If yes: note in sheet
                    │ Both done? ────────│──→ WhatsApp Ian: "Ready to build"
                    └─────────┬───────────┘
                              │
                    ┌─────────▼───────────┐
                    │ IAN BUILDS AGENT    │
                    │ (On M4 Mac)         │
                    │                     │
                    │ ElevenLabs config   │
                    │ Twilio number       │
                    │ Backend routing     │
                    │ Testing             │
                    └─────────┬───────────┘
                              │
                    Ian tells Aria: "Agent live for [Name]"
                              │
                    ┌─────────▼───────────┐
                    │ ARIA SENDS:         │
                    │                     │
                    │ 1. "You're live"    │──→ EMAIL-ONB-003
                    │ 2. Agent number     │
                    │ 3. What to expect   │
                    └─────────┬───────────┘
                              │
                    ┌─────────▼───────────┐
                    │ ARIA SCHEDULES:     │
                    │                     │
                    │ Day 3: Check-in     │
                    │ Day 7: Week 1 report│
                    │ Day 14: Check-in    │
                    │ Day 30: Month report│
                    │ Monthly: Ongoing    │
                    └─────────────────────┘
```

### Client Intake Form Integration

When client calls the intake line:
1. ARIA (on ElevenLabs) interviews them — 10 minutes
2. Transcript → Railway backend → Claude Haiku → structured JSON
3. JSON populates intake form fields:
   - Business hours, services, pricing
   - How they want calls handled
   - Special instructions, escalation triggers
   - CRM/POS/booking systems in use
4. Populated form → Resend email to ian@insynctech.io
5. Ian uses the populated form to build the agent

Aria on ClawBot READS the populated form from Supabase (or email)
and uses it to customize all future client communications.

### Integrations
```
DocuSign API ──→ Send service agreement templates
Stripe API (read-only) ──→ Monitor payment status
Resend API ──→ All onboarding emails
Supabase (read) ──→ Intake form data
Google Sheets API ──→ Client registry / tracking
OpenClaw Cron ──→ Check-in schedule triggers
WhatsApp ──→ Status updates to Ian
CertusOrdo ──→ Logs entire onboarding as transaction chain
```

### Ian's Role
- Closes the deal (verbal/in-person)
- Tells Aria to start onboarding
- Builds the agent (ElevenLabs + Twilio + backend — Aria can't do this)
- Tells Aria when agent is live
- Everything else is automated

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## DIVISION 5: CLIENT MAINTENANCE & RETENTION
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Purpose
Keep every client happy, informed, and paying. Detect problems before
the client notices. Prevent churn. Create upsell opportunities.

### What Aria Does (Fully Autonomous)

1. SCHEDULED CHECK-INS — Per client tenure cadence
   ```
   Week 1-2:    Every 2-3 days  ("How's [Agent] doing? Any feedback?")
   Week 3-4:    Weekly           ("Here's what [Agent] handled this week")
   Month 2-3:   Bi-weekly        ("Performance update + any adjustments?")
   Month 4+:    Monthly          (Full monthly report)
   Renewal -30d: Renewal prep    ("Your renewal is coming up. Here's your ROI.")
   ```

2. PERFORMANCE REPORTS — Pulls data from Supabase (read-only)
   - Total calls handled
   - Call duration averages
   - Peak call times
   - Most common call reasons
   - After-hours calls caught
   - Calculates estimated revenue protected (using ROI formulas)

3. HEALTH SCORING — Continuous per client
   ```
   Agent uptime:             30 points (from ElevenLabs metrics)
   Email delivery rate:      20 points (from Resend analytics)
   Call volume trend:        20 points (stable/growing = 20, declining = 5)
   Client responsiveness:    15 points (opens emails, replies to check-ins)
   Days since last issue:    15 points (>30d = 15, <7d = 0)
   ```
   - Score 90-100: Standard maintenance
   - Score 70-89: Increase check-in frequency
   - Score 50-69: Flag to Ian, suggest a personal call
   - Score <50: RED ALERT — Ian calls personally

4. CHURN SIGNAL DETECTION
   - Client hasn't opened last 3 emails → change approach, alert Ian
   - Call volume dropped 50%+ → check if they changed phone routing
   - Client asks "what am I paying for?" → immediate ROI report + Ian alert
   - Client mentions "thinking about cancelling" → Ian alert, churn prevention
   - Payment failed → immediate Ian alert + client notification

5. UPSELL DETECTION
   - 30+ calls/day on Starter tier → suggest Core upgrade
   - Client asks about integrations → flag Pro upsell
   - Client has multiple locations → flag multi-location deal
   - All upsells → WhatsApp to Ian for approval before sending

### Integrations
```
Supabase (read-only) ──→ Call logs, agent performance
ElevenLabs (read metrics) ──→ Call counts, duration, usage
Resend API ──→ Check-in emails, reports
Google Sheets API ──→ Client health tracker
OpenClaw Cron ──→ Scheduled check-ins per client
WhatsApp ──→ Health alerts, churn warnings, upsell flags
CertusOrdo ──→ Every check-in = transaction
```

### Ian's Role
- Takes personal calls when client wants a human
- Handles complaints and service recovery
- Approves upsell offers
- Makes system changes (prompt updates, voice changes)

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## DIVISION 6: SCHEDULING & CALENDAR MANAGEMENT
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Purpose
Make sure every prospect and client can easily schedule time with Ian
(or Aria for follow-ups), and that Ian is always prepared for calls.

### What Aria Does

1. SHARES CALENDLY LINKS — In emails, WhatsApp, proposals
   - Demo scheduling: https://calendly.com/certusordo/strategy-call
   - Included in every cold email sequence
   - Sent directly when prospect asks "Can we talk?"

2. MONITORS BOOKINGS — Calendly webhook or polling
   - New booking → Immediate WhatsApp to Ian:
     ```
     "New demo booked:
     Name: [Name]
     Business: [Business]
     Vertical: [Vertical]
     Time: [Date/Time]

     Pre-call brief:
     - [Business] gets ~[X] calls/day (estimated)
     - No AI/answering service detected
     - ROI estimate: $[X]/month
     - Suggested pitch: [Vertical-specific angle]
     - Template from: SALES_PLAYBOOKS.md Section [X]"
     ```

3. PRE-CALL PREP — Before every scheduled call
   - Pulls all data on the prospect from Google Sheets
   - Generates a 5-line pre-call brief
   - Sends to Ian 1 hour before the call

4. POST-CALL FOLLOW-UP — After Ian reports the outcome
   - Ian says "Hot — send pilot proposal" → Aria sends EMAIL-SAL-002
   - Ian says "Warm — needs time" → Aria schedules Day 5 follow-up
   - Ian says "Not a fit" → Aria moves to nurture list
   - Ian says "Closed — onboard" → Triggers Division 4 onboarding

5. FOLLOW-UP SCHEDULING — When clients want to talk to Aria again
   - Client can call the Aria main line: (727) 334-8156
   - Client can schedule a call via Calendly
   - Aria sends the Calendly link in every check-in email
   - After every client call with Aria (on ElevenLabs), post-call summary
     is generated and emailed to both client and Ian

### Integrations
```
Calendly API ──→ Monitor bookings, share links
Resend API ──→ Pre-call briefs, post-call follow-ups
Google Sheets API ──→ Prospect data for pre-call prep
WhatsApp ──→ Booking alerts + pre-call briefs to Ian
OpenClaw Cron ──→ Pre-call brief 1 hour before scheduled calls
```

### Ian's Role
- Takes all demo calls personally
- Reports outcome to Aria via WhatsApp (one sentence is enough)
- Aria handles everything after that

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## DIVISION 7: FINANCIAL MONITORING & REPORTING
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Purpose
Keep Ian informed on every dollar — revenue, costs, growth trajectory,
and red flags — without him logging into anything.

### What Aria Does

1. DAILY REVENUE CHECK — Reads Stripe API (read-only)
   - Current MRR
   - Any payments received today
   - Any payments failed today → IMMEDIATE WhatsApp alert
   - Upcoming renewals in next 7 days

2. FINANCIAL METRICS — Calculated continuously
   - MRR / ARR
   - MRR growth rate (vs. last month, vs. target)
   - Per-client profitability
   - Blended gross margin
   - Estimated runway at current burn
   - Pipeline-weighted revenue forecast

3. DAILY DIGEST — Included in 9 AM briefing
   ```
   REVENUE: $[MRR] MRR ($[change] from yesterday)
   PAYMENTS: [X] received, [X] pending, [X] failed
   NEXT RENEWAL: [Client] on [Date]
   ```

4. WEEKLY FINANCIAL SNAPSHOT — In Sunday report
   ```
   MRR:              $[X] (target: $[Y])  [status emoji]
   New revenue:      $[X] this week
   Pipeline value:   $[X]
   Top prospect:     [Name] — $[X] potential
   Costs this month: $[X] (est.)
   Margin:           [X]%
   Runway:           [X] months
   ```

5. RED FLAGS — Immediate alerts
   - Payment failed → WhatsApp: "[Client] payment failed. Retry in 3 days."
   - MRR decreased → WhatsApp: "MRR dropped to $[X]. [Client] churned / downgraded."
   - Cost spike → WhatsApp: "Railway/ElevenLabs bill higher than expected: $[X]"

### Integrations
```
Stripe API (READ-ONLY) ──→ Revenue, payments, subscriptions
Google Sheets API ──→ Financial tracking sheet
WhatsApp ──→ Financial alerts
OpenClaw Cron ──→ Daily check at 8:00 AM ET
CertusOrdo ──→ Financial reads logged
```

### What Aria CANNOT Do
- Issue refunds (Ian via M4 Mac → Stripe dashboard)
- Change subscription amounts
- Create new payment links (Ian creates, shares URL with Aria)
- Access bank accounts
- Make any financial commitments

---

## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## DIVISION 8: SELF-GOVERNANCE & CERTUSRODO INTEGRATION
## ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

### Purpose
Aria governs herself through CertusOrdo. Every action is a transaction.
Every transaction is auditable. Every mistake is reversible.
This is the product demo running 24/7.

### What Aria Logs (Every Action = Transaction)

| Action Type | Pre-State | Post-State | Rollback Available |
|-------------|-----------|------------|-------------------|
| email_send | Template + recipient | Sent confirmation | No (email sent) |
| content_draft | Topic + template | Draft text | Yes (delete draft) |
| content_publish | Draft approved | Published post | Yes (delete post) |
| lead_scrub | Zip + vertical | New leads found | Yes (remove from sheet) |
| outreach_send | Lead + template | Email sent | No (email sent) |
| client_checkin | Client + cadence | Check-in sent | No (email sent) |
| document_send | Client + template | DocuSign sent | Yes (void envelope) |
| payment_link_send | Client + link URL | Email with link sent | No (email sent) |
| booking_detected | Calendly event | Ian notified | N/A (read-only) |
| health_score_update | Previous score | New score | Yes (revert score) |
| financial_read | Previous snapshot | New snapshot | N/A (read-only) |
| escalation | Issue detected | Ian notified | N/A |

### Automatic Rollback Triggers
1. Email sent to wrong recipient → Log, alert Ian, no undo possible (flag as incident)
2. Content published with factual error → Delete post, alert Ian
3. Lead scored incorrectly → Revert score, re-evaluate
4. Pricing quoted below $99/mo floor → Alert Ian, note in CertusOrdo
5. Any API error after action taken → Log error, alert Ian
6. Action taken during Red Zone without approval → Full rollback if possible

### Self-Assessment (Weekly)
Every Sunday before generating the weekly report, Aria scores herself:
- Did I hit content targets? (5 posts/week)
- Did I complete all check-ins on schedule?
- Did I follow up on every prospect at cadence?
- Did any action require rollback?
- Did I escalate appropriately?
- Did I protect Ian's work-life balance?

Score included in weekly report. Trends tracked monthly.


# ═══════════════════════════════════════════════════════════════════════════════
# 4. INTEGRATION MAP (Every Service Connection)
# ═══════════════════════════════════════════════════════════════════════════════

```
                            ARIA (OpenClaw on HP Omen)
                                     │
                    ┌────────────────┼────────────────┐
                    │                │                │
              SEND THINGS       READ THINGS      THINK/PLAN
                    │                │                │
         ┌─────────┴──────┐   ┌────┴─────┐    ┌────┴─────┐
         │                │   │          │    │          │
     Resend API     DocuSign  Stripe     Supabase  Claude API
     (emails)       (contracts) (revenue) (call logs) (brain)
         │                │   │          │
     LinkedIn API   Payment   ElevenLabs Calendly
     (posts)        Links     (metrics)  (bookings)
         │          (URLs)    │
     TikTok/YT              Google Sheets
     (video)                (everything)
         │
     WhatsApp                Google Places
     (to Ian)                (lead scrub)
                             │
                             Yelp
                             (lead scrub)
                             │
                             BeautifulSoup
                             (website scrape)
```

### API Keys Aria Needs on the Omen

| Service | Key Type | How to Create | Notes |
|---------|----------|---------------|-------|
| Claude (Anthropic) | API key | console.anthropic.com → API Keys | Standard key, no special permissions |
| Resend | Sending API key | resend.com → API Keys → Create | Scope to sending only |
| Google Sheets | Service account JSON | Google Cloud Console → Service Accounts | Share specific sheets with service account email |
| Google Places | API key | Google Cloud Console → Credentials | Restrict to Places API only |
| Yelp Fusion | API key | yelp.com/developers → Create App | Read-only by default |
| Calendly | Personal access token | calendly.com → Integrations → API | Read + webhook access |
| Stripe | Restricted key (READ ONLY) | Stripe Dashboard → Developers → API Keys → Create Restricted Key → READ ONLY on all resources | CRITICAL: No write permissions |
| Supabase | Anon key (read-only) | Supabase Dashboard → Settings → API | Row-level security enforces read-only |
| ElevenLabs | API key | elevenlabs.io → Profile → API Key | Use for metrics reading only (separate from agent config) |
| DocuSign | Integration key | DocuSign Admin → Integrations | Scope to send-only on templates |
| CertusOrdo | Agent credentials | Already registered (see CLIENT_CONFIGS.md) | Full access — she IS the agent |
| LinkedIn | Access token | LinkedIn Developer Portal | Posting scope only |

### Keys That NEVER Go on the Omen

| Service | Why |
|---------|-----|
| Twilio Auth Token | Write access to phone routing |
| Railway API Token | Write access to deployments |
| GitHub Personal Access Token | Write access to code |
| Stripe Secret Key (full) | Write access to billing |
| Supabase Service Role Key | Admin access to database |
| ElevenLabs Agent Management Token | Write access to agent configs |
| Google Workspace Admin | Access to Ian's email |


# ═══════════════════════════════════════════════════════════════════════════════
# 5. OPENCLAW SKILL ARCHITECTURE
# ═══════════════════════════════════════════════════════════════════════════════

Each Division maps to one or more OpenClaw Skills. Skills are folders
with a SKILL.md file that tells Aria how to use the tools.

### Skills to Build or Install

| Skill Name | Division | What It Does |
|------------|----------|-------------|
| lead-scrubber | Div 1 | Google Places + Yelp + BeautifulSoup pipeline |
| email-engine | Div 2 | Resend integration + template personalization + cadence tracking |
| linkedin-publisher | Div 3 | LinkedIn API posting with approval gate |
| tiktok-uploader | Div 3 | TikTok video upload via browser automation |
| docusign-sender | Div 4 | Send service agreement templates |
| client-onboarder | Div 4 | Orchestrates full onboarding flow |
| client-health | Div 5 | Supabase reads + health scoring + check-in scheduling |
| calendar-manager | Div 6 | Calendly monitoring + pre-call brief generation |
| financial-monitor | Div 7 | Stripe read-only + metric calculations |
| certusrodo-logger | Div 8 | CertusOrdo API wrapper — logs every action |
| daily-digest | All | Compiles morning briefing from all divisions |
| weekly-report | All | Compiles Sunday evening report from all divisions |
| sheets-manager | All | Google Sheets read/write for all data storage |

### Skill Priority (Build Order)
```
WEEK 1:  sheets-manager + email-engine + lead-scrubber + daily-digest
WEEK 2:  calendar-manager + client-onboarder + certusrodo-logger
WEEK 3:  linkedin-publisher + client-health + financial-monitor
WEEK 4:  tiktok-uploader + docusign-sender + weekly-report
```

### ClawHub Skills (Pre-Built, May Be Useful)
- Google Sheets integration (likely exists)
- WhatsApp messaging (built into OpenClaw)
- Web scraping (likely exists)
- Cron scheduling (built into OpenClaw)
- Browser automation (built into OpenClaw)

Check ClawHub (565+ skills) before building custom. Customize as needed.


# ═══════════════════════════════════════════════════════════════════════════════
# 6. DAILY AUTONOMOUS WORKFLOW (24-Hour Cycle)
# ═══════════════════════════════════════════════════════════════════════════════

### Aria's Autonomous Day (No Ian Input Required)

```
6:00 AM ET ─── MORNING SCRUB
               Lead generation runs (3 verticals × 3 zips)
               New leads scored and added to Google Sheets

8:00 AM ET ─── FINANCIAL CHECK
               Read Stripe for overnight payments
               Check for failed payments
               Calculate updated MRR

8:30 AM ET ─── CONTENT PREP
               Draft today's social media content
               Send to Ian via WhatsApp for approval

9:00 AM ET ─── DAILY BRIEFING → WhatsApp to Ian
               Revenue update, new leads, priorities, flags

9:30 AM ET ─── OUTREACH BATCH
               Send day's cold emails (up to 20)
               Process follow-up emails per cadence
               Check for responses to yesterday's emails

10:00 AM ET ── CONTENT PUBLISH (if approved)
               Post approved LinkedIn content
               Upload approved TikTok video

11:00 AM ET ── CLIENT CHECK-INS
               Send any scheduled check-in emails
               Pull performance data for reports due today
               Send monthly/quarterly reports if due

12:00 PM ET ── CALENDLY CHECK
               Monitor for new bookings
               Send pre-call briefs for afternoon calls

2:00 PM ET ─── AFTERNOON SCRUB
               Lead generation run #2 (different verticals)
               Update lead scores with new data

3:00 PM ET ─── PIPELINE REVIEW
               Review all prospects in pipeline
               Identify stale leads needing re-engagement
               Update Google Sheets with status changes

5:00 PM ET ─── END OF DAY WRAP
               Log all actions to CertusOrdo
               Prepare next day's content draft
               Queue next day's outreach batch

8:00 PM ET ─── EVENING MONITORING (PASSIVE)
               Monitor for after-hours Calendly bookings
               Monitor for prospect email replies
               Alert Ian only for urgent items

SUNDAY 7:00 PM ── WEEKLY REPORT
               Compile all metrics across all divisions
               Self-assessment score
               Generate and send weekly report to Ian
```

### Aria Responds Instantly To

These events trigger immediate action regardless of schedule:

| Event | Aria's Response |
|-------|----------------|
| Prospect replies to cold email | WhatsApp Ian immediately + log |
| Calendly booking | WhatsApp Ian with pre-call brief |
| Payment failed | WhatsApp Ian + client notification |
| Client emails with issue | Acknowledge + investigate + flag if needed |
| Ian messages on WhatsApp | Respond within 60 seconds |
| Agent health check fails | SEV 1/2 alert per ESCALATION_RULES.md |


# ═══════════════════════════════════════════════════════════════════════════════
# 7. SECURITY MODEL & CREDENTIAL ISOLATION
# ═══════════════════════════════════════════════════════════════════════════════

### The Two-Machine Rule

```
M4 MAC (Ian's HQ)                    HP OMEN (Aria's Brain)
═══════════════════                   ═══════════════════════
Full Stripe access                    Stripe READ-ONLY key
Full Twilio access                    NO Twilio access
Full Railway access                   NO Railway access
Full GitHub access                    NO GitHub access
Full ElevenLabs admin                 ElevenLabs read-metrics only
Full Supabase admin                   Supabase read + insert-to-log
Gmail access                          NO email access (uses Resend only)
All deployment tools                  NO deployment capability
All production credentials            Only scoped/read-only keys
```

### Credential Storage on Omen

All API keys stored in OpenClaw's `.env` file on the Omen:
```
ANTHROPIC_API_KEY=[GET FROM IAN]         # Claude API (brain)
RESEND_API_KEY=[GET FROM IAN]            # Email sending
GOOGLE_SHEETS_SERVICE_ACCOUNT=[GET FROM IAN]  # JSON file path
GOOGLE_PLACES_API_KEY=[GET FROM IAN]     # Lead scrubbing
YELP_API_KEY=[GET FROM IAN]              # Lead scrubbing
CALENDLY_API_TOKEN=[GET FROM IAN]        # Scheduling
STRIPE_RESTRICTED_KEY=[GET FROM IAN]     # READ ONLY — Ian creates in Stripe
SUPABASE_URL=[GET FROM IAN]              # Database
SUPABASE_ANON_KEY=[GET FROM IAN]         # Read-only access
ELEVENLABS_API_KEY=[GET FROM IAN]        # Metrics reading only
DOCUSIGN_INTEGRATION_KEY=[GET FROM IAN]  # Send templates
CERTUSRODO_API_URL=[GET FROM IAN]        # Trust layer
CERTUSRODO_ORG_ID=[GET FROM IAN]         # Aria's org
CERTUSRODO_AGENT_ID=[GET FROM IAN]       # Aria's identity
CERTUSRODO_AGENT_SECRET=[GET FROM IAN]   # Aria's auth
```

### What Happens If the Omen Is Compromised

Worst case: attacker gets the .env file. What can they do?

| Key | Risk If Stolen | Mitigation |
|-----|---------------|------------|
| Claude API | Run up API bill | Set spending limit on Anthropic console |
| Resend | Send emails as InSync | Revoke immediately, rotate key |
| Google Sheets | Read/edit lead data | Service account has access to specific sheets only |
| Google Places | Run searches | Low risk — read-only public data |
| Yelp | Run searches | Low risk — read-only public data |
| Calendly | Read bookings | Low risk — no write access to calendar |
| Stripe (read-only) | See revenue data | Cannot charge or refund — restricted key |
| Supabase (anon) | Read call logs | Row-level security limits access |
| ElevenLabs | Read metrics | Cannot modify agents |
| DocuSign | Send templates | Templates are pre-built — limited blast radius |
| CertusOrdo | Log as Aria | Can be revoked, new agent registered |

**Key insight:** Because every key is scoped/restricted, a compromised Omen
cannot: deploy code, change agents, issue refunds, access banking, read email,
or modify any production system. The blast radius is contained.

### Monthly Security Checklist
1. ☐ Rotate Resend API key
2. ☐ Review Stripe restricted key permissions (confirm still read-only)
3. ☐ Check OpenClaw for security updates
4. ☐ Review Omen access logs
5. ☐ Confirm no new ClawHub skills installed without review
6. ☐ Verify CertusOrdo audit trail is complete


# ═══════════════════════════════════════════════════════════════════════════════
# 8. BUILD ORDER (Week 1 Setup Plan)
# ═══════════════════════════════════════════════════════════════════════════════

### Day 1: Prepare the Omen
1. Fresh Windows 11 user profile OR fresh Ubuntu 24 install
2. Install Node.js (LTS)
3. Install OpenClaw: `curl -fsSL https://openclaw.ai/install.sh | bash`
4. Connect Claude API key
5. Connect WhatsApp
6. Test: send "Hello" from phone → get response from Aria

### Day 2: Upload Knowledge Base
1. Sanitize all 13 .md files (remove API keys, secrets, credentials)
2. Upload to OpenClaw workspace as skills/knowledge
3. Test: ask Aria "What is our pricing for SMB clients?" → should answer from knowledge base
4. Test: ask Aria "What is John's email?" → should answer from CLIENT_REGISTRY

### Day 3: Connect Core Services
1. Create and configure scoped API keys:
   - Resend (sending key)
   - Google Sheets (service account)
   - Stripe (restricted read-only key)
2. Install/build sheets-manager skill
3. Install/build email-engine skill
4. Test: have Aria read from the Lead Database sheet
5. Test: have Aria send a test email via Resend

### Day 4: Lead Generation Engine
1. Create Google Places API key
2. Create Yelp Fusion API key
3. Install/build lead-scrubber skill
4. Set up Google Sheets "Lead Database" with proper columns
5. Run first scrub: "Aria, scrub barbershops in zip code 34231"
6. Verify leads appear in Google Sheets

### Day 5: Outreach & Calendar
1. Connect Calendly API
2. Install/build calendar-manager skill
3. Set up outreach cadence tracking in Google Sheets
4. Test: "Aria, send intro email to [test lead]"
5. Test: "Aria, who's booked on Calendly today?"

### Day 6: Daily Digest & Automation
1. Build daily-digest skill (compiles all sources)
2. Set up OpenClaw cron jobs for the full daily schedule
3. Test: trigger daily briefing manually → verify WhatsApp delivery
4. Set up CertusOrdo logging (certusrodo-logger skill)
5. Run full day simulation

### Day 7: Go Live
1. Final testing of all divisions
2. Aria sends her first real daily briefing Monday morning
3. First automated lead scrub runs
4. First cold emails go out (Ian-approved targets)
5. Aria is operational

### Weeks 2-4: Layer In Remaining Divisions
- Week 2: Client onboarding pipeline + DocuSign + social media
- Week 3: Client health monitoring + financial monitoring
- Week 4: Full autonomy — all 8 divisions running on schedule


# ═══════════════════════════════════════════════════════════════════════════════
# SUMMARY: WHAT ARIA DOES vs WHAT IAN DOES
# ═══════════════════════════════════════════════════════════════════════════════

## ARIA HANDLES (Autonomous — No Ian Needed)
- Finding leads (scrubbing)
- Scoring and qualifying leads
- Sending cold outreach emails
- Following up per cadence
- Drafting social media content
- Publishing approved content
- Sending DocuSign contracts
- Sending Stripe payment links
- Sending onboarding emails
- Scheduling and monitoring Calendly
- Generating pre-call briefs
- Sending post-demo follow-ups
- Running client check-ins
- Generating performance reports
- Calculating health scores
- Detecting churn signals
- Tracking revenue and payments
- Daily briefings and weekly reports
- Logging everything to CertusOrdo
- Self-assessment and improvement

## IAN HANDLES (Human Required)
- Taking demo calls
- Closing deals
- Building agents (ElevenLabs + Twilio + backend)
- Deploying code (Railway)
- Recording video content
- Approving social media posts
- Approving enterprise pricing
- Handling client complaints personally
- Making system changes
- Managing credentials and billing
- Strategic decisions
- Investor conversations

## THE RATIO
- Aria: ~80% of daily operations
- Ian: ~20% — focused on closing, building, and strategy
- Result: Ian operates like a 5-person team with one AI


# ═══════════════════════════════════════════════════════════════════════════════
# END OF ARIA × OPENCLAW ARCHITECTURE
# "She runs the business. He builds the product. CertusOrdo keeps it safe."
# ═══════════════════════════════════════════════════════════════════════════════
