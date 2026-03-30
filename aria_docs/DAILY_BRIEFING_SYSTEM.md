# ═══════════════════════════════════════════════════════════════════════════════
# DAILY BRIEFING SYSTEM
# InSync Tech, Inc. — Aria's Three Daily Touchpoints with Ian
# ═══════════════════════════════════════════════════════════════════════════════
# Version: 1.0 | March 22, 2026
#
# THREE TOUCHPOINTS:
#   MORNING (9:00 AM ET)  — Ian's personal checklist for the day
#   AFTERNOON (1:00 PM ET) — Current state of the entire business
#   EVENING (7:00 PM ET)   — Day's summary + what's on deck for tomorrow
#
# FORMAT: WhatsApp messages. Short. Scannable. Actionable.
# Ian should be able to read each one in under 2 minutes.
# ═══════════════════════════════════════════════════════════════════════════════


# ═══════════════════════════════════════════════════════════════════════════════
# 1. MORNING BRIEFING — "Your Day" (9:00 AM ET)
# ═══════════════════════════════════════════════════════════════════════════════

## Purpose
Tell Ian exactly what HE needs to do today. Not what Aria is doing.
Not a status report. A PERSONAL CHECKLIST for a human being.

## Delivery
- WhatsApp message at 9:00 AM ET sharp
- Under 200 words
- Numbered action items Ian must complete
- Starred items = urgent / time-sensitive

## Template

```
☀️ Morning, Ian. Here's your day.

📊 REVENUE
MRR: $[X] | Pipeline: $[X] | Δ from yesterday: [+/-$X]

📋 YOUR CHECKLIST TODAY
⭐ 1. [Most urgent/time-sensitive item]
   2. [Second priority]
   3. [Third priority]
   4. [Fourth if applicable]

📞 YOUR CALLS
[Time] — [Name], [Company], [Purpose]
   Pre-brief: [2-line context + pitch angle]
[Time] — [Name], [Company], [Purpose]
   Pre-brief: [2-line context]
(No calls today — focus time available.)

⚠️ NEEDS YOUR DECISION
- [Yellow Zone item needing approval — 1 line description]
- [Another if applicable]

✅ WHAT I'M HANDLING TODAY
- [Key autonomous actions Aria is running — 2-3 bullets max]

Reply with questions or changes. Otherwise I'll execute.
```

## What Populates Each Section

### Revenue
- MRR: Pull from Stripe read-only API
- Pipeline: Sum of weighted pipeline from Google Sheets Pipeline tab
- Delta: Compare today's Stripe read vs yesterday's cached value

### Your Checklist (Ian's Human Tasks)
Aria builds this from multiple sources:

| Source | Example Ian Task |
|--------|-----------------|
| Calendly bookings | "10 AM demo with Dr. Patel — pre-brief below" |
| Client onboarding queue | "Build agent for [new client] — intake form in your email" |
| Stale prospects | "⭐ Follow up Jack Leaf — no response in 7 days" |
| Twilio/tech blockers | "Check A2P registration status" |
| Content recording | "Record TikTok: barbershop call demo (script in Drive)" |
| Code deployments needed | "Deploy webhook update for new client routing" |
| Contract/legal | "⭐ Send DocuSign to [client] — they said yes yesterday" |
| Financial | "Stripe test mode — verify LIVE before sending payment links" |
| Partner follow-ups | "Reply to [agency] about partnership terms" |
| Overdue items from yesterday | "⭐ Carried over: [task] from yesterday (not completed)" |

### Prioritization Rules
1. Revenue-generating actions first (closing deals, building agents, sending contracts)
2. Time-sensitive items starred (calls, deadlines, carried-over tasks)
3. Max 6 items — if more exist, Aria picks the top 6 and holds the rest for afternoon
4. Each item is ONE sentence. No paragraphs.
5. If Ian has no calls and no urgent items: "Light day. Focus time available. I recommend [specific productive use of time]."

### Pre-Call Briefs (Inline, Not Separate)
For every call on the schedule, include a 2-line brief RIGHT IN the morning message:
```
📞 10:00 AM — Dr. Patel, Bradenton Family Dental, Demo
   Pre-brief: 6-chair practice, losing ~5 new patients/week to VM.
   Comparing us to Ruby. Lead with price ($149 vs $240). Mention HIPAA audit trail.
```
Ian doesn't need to open a separate document. Everything he needs is in the WhatsApp message.

### Carried-Over Items
If Ian didn't complete a task from yesterday's checklist:
```
⭐ 3. Follow up Jack Leaf (carried over from yesterday — Day 9 of 21 cadence)
```
No guilt. No nagging. Just factual. Starred because it's now more urgent.


# ═══════════════════════════════════════════════════════════════════════════════
# 2. AFTERNOON BRIEFING — "State of the Business" (1:00 PM ET)
# ═══════════════════════════════════════════════════════════════════════════════

## Purpose
Snapshot of the entire business operation at midday. Where things stand
across all divisions. What's working. What's stuck. No action items —
this is AWARENESS, not a to-do list.

## Delivery
- WhatsApp message at 1:00 PM ET
- Under 250 words
- Dashboard-style format — scan in 90 seconds
- Only surfaces things that CHANGED or MATTER

## Template

```
🕐 Afternoon check-in. Here's where we stand.

💰 REVENUE & PIPELINE
MRR: $[X] | Clients: [X] | AnswrdBy Subs: [X]
Pipeline: [X] leads → [X] contacted → [X] responded → [X] demo → [X] pilot
Hottest prospect: [Name] — [status/next step]

📧 OUTREACH TODAY
Sent: [X] emails | Follow-ups: [X] | Responses: [X]
[If response:] 🔥 [Name] from [Business] replied: "[brief quote or sentiment]"

📱 CONTENT
Published: [what, where]
Performance: [yesterday's post got X views / X engagement]

👥 CLIENTS
[Agent Name]: [X] calls today | All healthy ✅
[Or: ⚠️ [Client] — [issue description]]

📅 UPCOMING
- [Tomorrow's key item]
- [This week's key milestone]

🤖 WHAT I COMPLETED THIS MORNING
- [Autonomous action + result]
- [Autonomous action + result]

[If nothing notable:] All systems nominal. Operations running per schedule.
```

## What Populates Each Section

### Revenue & Pipeline
- Same Stripe pull as morning (may have changed if payment came in)
- Pipeline funnel counts from Google Sheets Outreach Tracker
- Hottest prospect = highest-score lead in "Responded" or "Demo" stage

### Outreach Today
- Count of emails sent from today's batch
- Count of follow-ups triggered by cadence
- ANY response = highlighted with fire emoji and brief context
- If zero responses: "No responses yet today. Cadence continuing."

### Content
- What was published today (platform + topic)
- Yesterday's post performance (gives 24-hour data window)
- Any notable engagement (comments that need Ian's reply)

### Clients
- Per-client call count from Supabase (if readable midday)
- Health status: Green ✅ / Yellow ⚠️ / Red 🔴
- Only surface issues — if everyone's healthy, one line: "All clients healthy ✅"

### What Aria Completed
- 2-3 most significant autonomous actions from the morning
- Shows Ian that the machine is running without him
- Builds trust over time: "Aria handled 14 actions before I woke up"

### Selective Reporting Rule
**Do NOT dump every metric every day.** Only surface:
1. Things that CHANGED since morning
2. Things that NEED ATTENTION
3. Wins worth celebrating
4. If nothing changed: "All systems nominal" is a valid afternoon briefing


# ═══════════════════════════════════════════════════════════════════════════════
# 3. EVENING BRIEFING — "Day's Wrap + Tomorrow" (7:00 PM ET)
# ═══════════════════════════════════════════════════════════════════════════════

## Purpose
Close the loop on today. Set up tomorrow. Let Ian go into the evening
knowing exactly where things stand and what's ahead.

## Delivery
- WhatsApp message at 7:00 PM ET
- Under 250 words
- Tone: Closing out. Warm. "We had a good day. Rest up."
- Do NOT send after 7:30 PM — respect Ian's evening

## Template

```
🌙 Day's wrap. Here's how we did.

📊 TODAY'S SCORECARD
| Metric | Target | Actual |
|--------|--------|--------|
| Outreach sent | [X] | [X] ✅/⚠️ |
| Responses | [X] | [X] ✅/⚠️ |
| Content published | [X] | [X] ✅/⚠️ |
| Client check-ins | [X] | [X] ✅/⚠️ |
| Calls handled (all agents) | — | [X] |

💰 REVENUE UPDATE
MRR: $[X] (no change / +$[X] — [reason])

🏆 TODAY'S WIN
[Single biggest positive thing that happened today]

📌 CARRIED TO TOMORROW
[Any of Ian's checklist items not completed — factual, not judgmental]

🔮 TOMORROW'S PREVIEW
- [Ian's top priority for tomorrow]
- [Any calls/meetings on schedule]
- [Key autonomous action Aria will run]

💡 RECOMMENDATION
[One strategic suggestion from Aria based on today's data]
"Based on today's response rate, I recommend we shift Tuesday's
outreach from insurance to dental — dental is converting 3x better."

Rest up. Tomorrow we [brief motivational close tied to current goal].
```

## What Populates Each Section

### Today's Scorecard
Track daily targets vs actuals across core metrics.
Uses targets from 90_DAY_REVENUE_SPRINT.md:
- Week 1-4: 10 outreach/day, 1 response/day, 1 content piece, 100% check-ins
- Week 5-8: 15-20 outreach/day, 2 responses, 1+ content
- Week 9-13: 20 outreach/day, 3 responses, 1+ content

✅ = hit or exceeded target
⚠️ = missed target (include brief reason)

### Revenue Update
- Final Stripe read of the day
- Note any new payments, failed payments, or MRR changes
- "No change" is fine — don't manufacture excitement

### Today's Win
Always find ONE positive thing. Even on bad days.
- "Dr. Patel opened our email twice — high interest signal"
- "Mel handled 12 calls today — new record for Venice Barbershop"
- "LinkedIn post got 47 impressions — 3x our average"
- "We survived a Resend outage with zero client impact"

If genuinely nothing happened: "Quiet day. Systems ran clean. Sometimes that's the win."

### Carried to Tomorrow
Any items from the morning checklist Ian didn't complete:
- "Follow up Jack Leaf (Day 10 — moving to priority 1 tomorrow)"
- No judgment. No passive aggression. Just tracking.

### Tomorrow's Preview
Give Ian a mental picture of what tomorrow looks like:
- "Tomorrow: 2 demos scheduled (10 AM + 2 PM). I'll have briefs ready by 9 AM."
- "Tomorrow: No calls. Good day to build [client]'s agent and record content."
- "Tomorrow: Jack Leaf follow-up is Day 10. Recommend in-person visit."

### Recommendation
This is Aria's STRATEGIC BRAIN showing up. One insight per day:
- Pattern recognition: "Insurance outreach: 0/15 responses. Dental: 4/12. Recommend pausing insurance."
- Opportunity spotting: "3 clients now in dental vertical. Enough for a case study."
- Risk flagging: "John hasn't opened last 2 check-in emails. Consider a personal call."
- Resource allocation: "Content is outperforming outreach for leads. Recommend 2 posts/day next week."
- Timing insights: "Tuesday emails get 2x open rate vs Monday. Shifting batch day."

This recommendation should IMPROVE over time as Aria accumulates data.


# ═══════════════════════════════════════════════════════════════════════════════
# 4. WEEKLY REPORT (Sunday 8:00 PM ET) — No Changes Needed
# ═══════════════════════════════════════════════════════════════════════════════

## Already Specified In:
- MASTER_OPERATING_SYSTEM.md Section 4.4
- ARIA_OPENCLAW_ARCHITECTURE.md Section 6

## Enhancement: Include Weekly Trend Data

Add to existing weekly report:

```
📈 WEEKLY TRENDS (vs Last Week)
| Metric | Last Week | This Week | Trend |
|--------|----------|-----------|-------|
| Outreach sent | [X] | [X] | ↑/↓/→ |
| Response rate | [X]% | [X]% | ↑/↓/→ |
| Demos booked | [X] | [X] | ↑/↓/→ |
| Content published | [X] | [X] | ↑/↓/→ |
| Content engagement | [X] | [X] | ↑/↓/→ |
| Client calls handled | [X] | [X] | ↑/↓/→ |
| MRR | $[X] | $[X] | ↑/↓/→ |

🧠 ARIA'S WEEKLY INSIGHT
[One strategic observation from the week's data — something that
isn't obvious from individual daily briefings but emerges from
the weekly view]
```


# ═══════════════════════════════════════════════════════════════════════════════
# 5. MONTHLY REPORT (1st of Each Month, 9:00 AM) — New
# ═══════════════════════════════════════════════════════════════════════════════

## Template

```
📅 MONTH [X] REPORT — [Month Year]

🎯 NORTH STAR
MRR: $[X] → Target was $[X] → [Hit/Missed by $X]

📊 MONTHLY SCORECARD
| Metric | Target | Actual | Grade |
|--------|--------|--------|-------|
| New clients | [X] | [X] | A/B/C/D/F |
| MRR growth | [X]% | [X]% | A/B/C/D/F |
| Churn | <[X]% | [X]% | A/B/C/D/F |
| Outreach sent | [X] | [X] | A/B/C/D/F |
| Response rate | [X]% | [X]% | A/B/C/D/F |
| Demos | [X] | [X] | A/B/C/D/F |
| Content published | [X] | [X] | A/B/C/D/F |
| Inbound leads | [X] | [X] | A/B/C/D/F |
| Client health avg | [X] | [X] | A/B/C/D/F |

💰 FINANCIAL SUMMARY
Revenue: $[X] | Costs: $[X] | Profit: $[X] | Margin: [X]%
vs Last Month: [+/-$X] ([X]% change)

🏆 TOP 3 WINS
1. [Biggest win]
2. [Second win]
3. [Third win]

📉 TOP 3 MISSES
1. [Biggest miss + root cause + fix]
2. [Second miss]
3. [Third miss]

🔮 NEXT MONTH PRIORITIES
1. [#1 priority — specific and measurable]
2. [#2]
3. [#3]

💡 ARIA'S MONTHLY RECOMMENDATION
[One major strategic recommendation based on 30 days of data.
This should be something Ian hasn't thought of — a pattern
Aria noticed from operating the business every day.]

📊 ARIA SELF-ASSESSMENT: [X]/100
[Brief explanation of score]
```

## Grading Scale
- A: Exceeded target by 20%+
- B: Hit target or exceeded by <20%
- C: Missed target by <20%
- D: Missed target by 20-50%
- F: Missed target by 50%+


# ═══════════════════════════════════════════════════════════════════════════════
# 6. BRIEFING RULES
# ═══════════════════════════════════════════════════════════════════════════════

## Timing Rules
- Morning: 9:00 AM ET sharp. Never earlier (Ian's focus time). Never later.
- Afternoon: 1:00 PM ET. Can shift to 1:30 if Ian is on a call at 1:00.
- Evening: 7:00 PM ET. NEVER after 7:30 PM. If Aria missed 7:00, skip to morning.
- Weekly: Sunday 8:00 PM ET.
- Monthly: 1st of each month, 9:00 AM (combined with morning briefing).

## Tone Rules
- Morning: Energetic. Let's go. Here's your mission.
- Afternoon: Calm. Here's where things stand. Awareness, not urgency.
- Evening: Warm. Good work today. Here's what matters. Rest up.
- NEVER: Panicked, apologetic, or overwhelming.

## Length Rules
- Morning: Under 200 words (scannable in 60 seconds)
- Afternoon: Under 250 words (scannable in 90 seconds)
- Evening: Under 250 words (scannable in 90 seconds)
- Weekly: Under 500 words
- Monthly: Under 700 words

## Content Rules
- NEVER pad with filler ("As you know..." / "Just wanted to update...")
- NEVER repeat information from an earlier briefing unless it changed
- ALWAYS lead with the most important item
- ALWAYS include at least one number (revenue, calls, leads, responses)
- ALWAYS make Ian's action items crystal clear (verb + object + deadline)
- NEVER include more than 6 action items in morning checklist
- ALWAYS find a win for the evening briefing (even small ones)
- ALWAYS include one recommendation in the evening briefing

## Skip Rules
- If Ian is traveling (he tells Aria): consolidate to morning + evening only
- If it's a holiday: morning briefing only (abbreviated), skip afternoon + evening
- If nothing changed since morning: afternoon can be "All nominal. No updates."
- NEVER skip the morning briefing. Ever. That's Ian's compass for the day.

## Feedback Integration
- If Ian says "too long" → shorten by 20% and hold for 1 week
- If Ian says "more detail on [X]" → add that section, trim elsewhere
- If Ian stops reading afternoon briefings → ask: "Want me to drop to 2/day?"
- Track which sections Ian replies to — those are the ones he values most


# ═══════════════════════════════════════════════════════════════════════════════
# 7. DATA SOURCES PER BRIEFING
# ═══════════════════════════════════════════════════════════════════════════════

## Morning Briefing Pulls From:
| Data | Source |
|------|--------|
| MRR | Stripe API (read-only) |
| Pipeline | Google Sheets — Pipeline tab |
| Today's calls | Calendly API |
| Ian's incomplete tasks | Google Sheets — Ian's Checklist (or yesterday's evening) |
| Client issues | Google Sheets — Client Health Dashboard |
| Yellow Zone items | CertusOrdo transaction log (flagged items) |
| Aria's planned actions | OpenClaw cron schedule |

## Afternoon Briefing Pulls From:
| Data | Source |
|------|--------|
| Outreach stats | Google Sheets — Outreach Tracker |
| Responses | Resend API analytics + Google Sheets |
| Content published | Google Sheets — Content Performance |
| Client calls | Supabase (read-only) |
| Aria's completed actions | CertusOrdo transaction log |

## Evening Briefing Pulls From:
| Data | Source |
|------|--------|
| Daily targets vs actuals | Google Sheets — all tabs |
| Final MRR | Stripe API |
| Ian's completed checklist | Compare morning list to actual completions |
| Tomorrow's schedule | Calendly API + planned outreach |
| Weekly trend data | Google Sheets — computed from daily entries |
| Recommendation | Aria's analysis of conversion data, patterns, anomalies |


# ═══════════════════════════════════════════════════════════════════════════════
# 8. EXAMPLE DAY (What This Looks Like in Practice)
# ═══════════════════════════════════════════════════════════════════════════════

## MORNING (9:00 AM)

```
☀️ Morning, Ian. Here's your day.

📊 REVENUE
MRR: $1,247 | Pipeline: $18,400 | +$0 overnight

📋 YOUR CHECKLIST TODAY
⭐ 1. 10 AM — Demo with Dr. Patel, Bradenton Family Dental
      Pre-brief: 6 chairs, losing ~5 new patients/week to VM.
      Comparing to Ruby. Lead with price. Mention HIPAA audit trail.
   2. Build agent for Tampa Nail Spa (intake form in your email)
   3. Record TikTok: "I called 10 dentists" video (script in Drive)
   4. Reply to ElevenLabs grants team — Jonathan followed up yesterday

⚠️ NEEDS YOUR DECISION
- Agency partner (Digital Boost Tampa) wants 25% rev share instead of 20%.
  Recommend: Accept. Their pipeline justifies the extra 5%.

✅ WHAT I'M HANDLING TODAY
- Sending 18 outreach emails (dental + vet batch)
- Day 7 follow-ups for last week's barbershop outreach
- Publishing LinkedIn post (approved yesterday)

Reply with questions or changes. Otherwise I'll execute.
```

## AFTERNOON (1:00 PM)

```
🕐 Afternoon check-in.

💰 REVENUE & PIPELINE
MRR: $1,247 | Clients: 7 | AnswrdBy: 12 subs
Pipeline: 147 leads → 62 contacted → 8 responded → 3 demo → 1 pilot
Hottest: Dr. Patel — how'd the demo go?

📧 OUTREACH TODAY
Sent: 18 | Follow-ups: 7 | Responses: 2
🔥 Tampa Pet Hospital replied: "Interested, send pricing"
🔥 Sunrise Dental opened email 3x — likely interested, no reply yet

📱 CONTENT
Published: LinkedIn post on dental missed calls (10:02 AM)
Yesterday's post: 89 impressions, 4 likes, 1 comment ("how much?")

👥 CLIENTS
All 7 agents healthy ✅ | 34 total calls today across all agents

🤖 WHAT I COMPLETED THIS MORNING
- Scraped 22 new dental leads in Manatee County
- Sent Tampa Pet Hospital pricing proposal (EMAIL-SAL-002)
- Scheduled Dr. Patel's onboarding emails (pending demo outcome)
```

## EVENING (7:00 PM)

```
🌙 Day's wrap.

📊 TODAY'S SCORECARD
| Metric | Target | Actual |
|--------|--------|--------|
| Outreach sent | 15 | 18 ✅ |
| Responses | 1 | 2 ✅ |
| Content | 1 | 1 ✅ |
| Check-ins | 2 | 2 ✅ |
| Calls (all agents) | — | 41 |

💰 MRR: $1,247 (no change)

🏆 TODAY'S WIN
Dr. Patel demo went well (you told me "hot — send pilot").
His onboarding sequence starts tomorrow morning.
If he converts: MRR goes to $1,396 (+$149).

📌 CARRIED TO TOMORROW
- Record TikTok video (moved from today)
- ElevenLabs grants reply (still pending)

🔮 TOMORROW'S PREVIEW
- No calls scheduled — great day to build Tampa Nail Spa agent + record content
- I'll send Dr. Patel's DocuSign + Stripe link at 9:30 AM
- 20 more dental outreach emails queued

💡 RECOMMENDATION
Dental is our hottest vertical right now: 4 responses from 30 emails (13% rate)
vs barbershop at 2 from 45 (4%). I recommend shifting 60% of next week's
outreach to dental and building a dental-specific landing page this weekend.

Good day today. Two hot responses + a pilot incoming. Rest up. 🌙
```


# ═══════════════════════════════════════════════════════════════════════════════
# 9. IAN'S CHECKLIST TRACKING (Google Sheets)
# ═══════════════════════════════════════════════════════════════════════════════

## Add to GOOGLE_SHEETS_ARCHITECTURE: Sheet 12

### IAN'S DAILY CHECKLIST
| Column | Type | Notes |
|--------|------|-------|
| A: Date | Date | |
| B: Item # | Number | 1-6 |
| C: Task | Text | From morning briefing |
| D: Priority | ⭐/Normal | |
| E: Status | Complete/Incomplete/Carried | |
| F: Carried To | Date | If not completed |
| G: Times Carried | Number | How many days this task has been carried |
| H: Notes | Text | |

## Carry-Over Rules
- Task carried 1 day: Normal mention in tomorrow's briefing
- Task carried 2 days: Starred in tomorrow's briefing
- Task carried 3+ days: Aria asks Ian directly: "This has been on your list for [X] days. Should I remove it, delegate it, or is today the day?"
- Task carried 5+ days: Aria escalates in evening briefing: "This item may be blocking revenue. Recommend prioritizing or deliberately deprioritizing."

This is not nagging. This is a COO making sure nothing falls through the cracks.


# ═══════════════════════════════════════════════════════════════════════════════
# END OF DAILY BRIEFING SYSTEM
#
# "Ian's day starts with clarity and ends with closure.
#  Everything in between, Aria handles."
# ═══════════════════════════════════════════════════════════════════════════════
