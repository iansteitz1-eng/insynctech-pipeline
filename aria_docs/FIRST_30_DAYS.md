# ═══════════════════════════════════════════════════════════════════════════════
# FIRST 30 DAYS — ARIA DEPLOYMENT EXECUTION PLAN
# InSync Tech, Inc. — From Install to Autonomous Operations
# ═══════════════════════════════════════════════════════════════════════════════
# Last Updated: March 22, 2026
# ═══════════════════════════════════════════════════════════════════════════════

# WEEK 1: FOUNDATION (Days 1-7)
# Goal: Aria alive, talking, and reading her knowledge base

## Day 1: Hardware + Install
- [ ] Fresh Windows 11 profile on Omen (or Ubuntu 24 if preferred)
- [ ] Connect Omen to ethernet (not WiFi)
- [ ] Install Node.js LTS
- [ ] Install OpenClaw: curl -fsSL https://openclaw.ai/install.sh | bash
- [ ] Enter Claude API key (from CREDENTIALS_VAULT.md on M4)
- [ ] Connect WhatsApp
- [ ] TEST: Send "Hello Aria" from phone → get response
- [ ] Set Omen to never sleep (power settings → always on)

## Day 2: Upload Knowledge Base
- [ ] Upload all 21 .md files to OpenClaw workspace
- [ ] Load ARIA_SYSTEM_PROMPT.md as the system prompt
- [ ] TEST: "What is our pricing for SMB clients?" → answers from MASTER_OS
- [ ] TEST: "Draft a cold email for a dental office in Tampa" → uses SALES_PLAYBOOKS
- [ ] TEST: "What's our MRR?" → answers from FINANCIAL_DASHBOARD
- [ ] TEST: "Who is our paying client?" → answers from CLIENT_REGISTRY
- [ ] TEST: "What should I post on LinkedIn today?" → references CONTENT_CALENDAR
- [ ] Fix any knowledge retrieval issues

## Day 3: Connect Core APIs
- [ ] Create Resend sending API key → add to .env
- [ ] Create Google Sheets service account → share sheets → add to .env
- [ ] Create Stripe RESTRICTED (read-only) key → add to .env
- [ ] Create Google Places API key → add to .env
- [ ] TEST: "Send a test email to ian@insynctech.io" → email arrives
- [ ] TEST: "Read row 1 of the Lead Database" → reads from sheets
- [ ] TEST: "What's our current MRR from Stripe?" → reads Stripe

## Day 4: Build Core Sheets
- [ ] Create all 11 Google Sheets per GOOGLE_SHEETS_ARCHITECTURE.md
- [ ] Populate Lead Database with existing 150+ leads from Sales Machine
- [ ] Populate Client Health with Venice Barbershop data
- [ ] Populate Financial Tracker with current numbers
- [ ] Populate Outreach Tracker with any existing sequences
- [ ] Share all sheets with service account email

## Day 5: Connect Remaining APIs
- [ ] Calendly API token → add to .env
- [ ] Supabase anon key → add to .env
- [ ] ElevenLabs API key (metrics) → add to .env
- [ ] CertusOrdo credentials → add to .env
- [ ] TEST: "Check Calendly for today's bookings"
- [ ] TEST: "How many calls did Mel handle this week?" (Supabase read)
- [ ] TEST: "Log this conversation as a CertusOrdo transaction"

## Day 6: Set Up Cron Schedule
- [ ] Configure OpenClaw scheduled tasks:
  - 6:00 AM: Lead scrub
  - 6:30 AM: Health checks (ERROR_RECOVERY_PLAYBOOK)
  - 8:00 AM: Stripe financial check
  - 8:30 AM: Content draft + approval request
  - 9:00 AM: Daily briefing to Ian
  - 9:30 AM: Outreach batch
  - 2:00 PM: Afternoon scrub
- [ ] TEST: Trigger daily briefing manually → verify WhatsApp delivery
- [ ] TEST: Trigger health check → verify all APIs responding

## Day 7: Full Day Simulation
- [ ] Let Aria run the ENTIRE daily schedule from 6 AM to 5 PM
- [ ] Monitor every action she takes
- [ ] Check every email before it sends (override to approval-required for Day 7)
- [ ] Verify CertusOrdo is logging every transaction
- [ ] Fix any issues
- [ ] Sunday evening: Aria generates her FIRST weekly report

---

# WEEK 2: LEAD GEN + OUTREACH (Days 8-14)
# Goal: Pipeline growing, first cold emails sending

## Day 8: First Live Lead Scrub
- [ ] Aria runs morning scrub: barbershops + dental + vet in 3 Tampa zip codes
- [ ] Review results in Lead Database — check data quality
- [ ] Aria scores leads (HOT/WARM/COLD)
- [ ] Ian selects first 10 HOT leads for outreach approval

## Day 9: First Cold Emails
- [ ] Aria personalizes 10 emails from SALES_PLAYBOOKS.md templates
- [ ] Ian reviews and approves each email via WhatsApp
- [ ] Aria sends via Resend
- [ ] Verify: BCC to ian@insynctech.io working
- [ ] Verify: CertusOrdo logging each send

## Day 10: Content Engine Start
- [ ] Aria drafts first LinkedIn post from CONTENT_CALENDAR.md
- [ ] Ian reviews via WhatsApp → approves or edits
- [ ] Aria publishes (or Ian publishes from M4 if LinkedIn API not yet connected)
- [ ] Aria drafts first TikTok script → Ian records video

## Day 11-12: Cadence + Monitoring
- [ ] Day 3 follow-ups send for Day 9 emails
- [ ] Aria monitors for responses
- [ ] Daily briefings refining (Ian gives feedback on format/content)
- [ ] Second lead scrub batch: 3 new verticals
- [ ] 10 more outreach emails approved and sent

## Day 13: Client Check-In Test
- [ ] Aria sends scheduled check-in to John (Venice Barbershop)
- [ ] Aria pulls Mel's call data from Supabase
- [ ] Aria generates mini performance report
- [ ] Ian reviews before sending
- [ ] Verify: Check-in schedule working for all cadences

## Day 14: Week 2 Review
- [ ] Aria generates second weekly report
- [ ] Compare to Week 1 — what improved?
- [ ] Leads generated: [count] → target: 20+
- [ ] Emails sent: [count] → target: 20+
- [ ] Content published: [count] → target: 3+
- [ ] Issues encountered and resolved: [list]
- [ ] Adjust any cadences or templates based on early data

---

# WEEK 3: EXPAND + OPTIMIZE (Days 15-21)
# Goal: Outreach machine humming, content rhythm established

## Day 15-17: Scale Outreach
- [ ] Increase to 15-20 emails/day (if no deliverability issues)
- [ ] Aria handles follow-up cadence fully autonomously (Day 3, 7, 14, 21)
- [ ] Ian only reviews RESPONSES, not every outreach email
- [ ] First "Go/No-Go" on Aria sending approved-template emails without per-email approval

## Day 18-19: AnswrdBy Prep (If Blockers Cleared)
- [ ] If A2P cleared: Begin AnswrdBy launch per ANSWRDBY_TELECOM_STRATEGY.md
- [ ] If not: Continue InSync B2B focus, prep AnswrdBy website copy with Aria

## Day 20: Content Optimization
- [ ] Review first 2 weeks of content performance
- [ ] Which posts got engagement? Which flopped?
- [ ] Aria recommends content mix adjustment
- [ ] Begin A/B testing: Hook A vs Hook B on same format
- [ ] Start Nano Banana persona renders for AnswrdBy marketing prep

## Day 21: Week 3 Review
- [ ] Third weekly report
- [ ] Pipeline value: $ [target: $5,000+]
- [ ] Demos booked from outreach: [target: 2+]
- [ ] Content engagement trending up?
- [ ] Any prospects in "Responded" or "Demo" stage?
- [ ] Transition plan: Which Yellow Zone items can move to Green?

---

# WEEK 4: AUTONOMOUS MODE (Days 22-30)
# Goal: Aria running independently with minimal Ian oversight

## Day 22-25: Trust Expansion
- [ ] Approved-template emails: Move to GREEN (Aria sends without per-email approval)
- [ ] Scheduled check-ins: Move to GREEN (Aria sends autonomously)
- [ ] Daily briefing: Confirmed working, no longer needs review
- [ ] Content: Pre-approved formats move to GREEN (Aria publishes directly)
- [ ] Ian's daily time with Aria drops from ~2 hours to ~30 minutes

## Day 26-28: Revenue Focus
- [ ] Review entire pipeline — which prospects are closest to closing?
- [ ] Aria generates personalized proposals for top 3 prospects
- [ ] Aria schedules follow-ups for all demo-stage prospects
- [ ] If Great Clips responsive: Aria prepares full pre-call package for Ian
- [ ] Begin partner outreach (1-2 agencies) if MRR trajectory supports it

## Day 29: Full Autonomy Checkpoint
- [ ] Aria has been operating for 4 weeks
- [ ] Score against targets:

| Metric | Target | Actual |
|--------|--------|--------|
| Leads generated | 100+ | |
| Outreach emails sent | 60+ | |
| Responses received | 5+ | |
| Demos booked | 3+ | |
| Content published | 15+ | |
| Client check-ins completed | 100% on schedule | |
| Daily briefings delivered | 100% | |
| Weekly reports delivered | 4/4 | |
| CertusOrdo transactions logged | 100% | |
| Errors requiring Ian intervention | <5 | |
| MRR | Still $99 minimum (no churn) | |

## Day 30: Month 1 Report + Month 2 Plan
- [ ] Aria generates comprehensive Month 1 report
- [ ] Ian and Aria (via WhatsApp) discuss Month 2 priorities
- [ ] Activate any Phase 2 triggers that were hit
- [ ] Expand autonomous authority based on performance
- [ ] Celebrate: You've been running a company with an AI COO for 30 days

---

# POST-30 DAYS: SELF-SUSTAINING OPERATIONS

After Day 30, Aria's daily rhythm runs without Ian initiating anything:
- Leads flow in automatically
- Outreach sequences fire automatically
- Content publishes on schedule (approved formats = autonomous)
- Client check-ins happen on cadence
- Financial monitoring runs daily
- Weekly reports compile automatically
- CertusOrdo logs everything

Ian's daily involvement: ~30 minutes
- Review daily briefing (5 min)
- Approve/reject any Yellow Zone items (10 min)
- Take scheduled demo calls (as needed)
- Record video content (as needed)
- Build new client agents (as needed)

Aria handles the other 23.5 hours.

# ═══════════════════════════════════════════════════════════════
# END OF FIRST 30 DAYS
# ═══════════════════════════════════════════════════════════════
