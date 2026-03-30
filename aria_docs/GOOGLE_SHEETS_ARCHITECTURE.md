# ═══════════════════════════════════════════════════════════════════════════════
# GOOGLE SHEETS ARCHITECTURE
# InSync Tech, Inc. — Every Data Sheet Aria Maintains
# ═══════════════════════════════════════════════════════════════════════════════
# Last Updated: March 22, 2026
# Share each sheet with the Google Service Account email on the Omen.
# Aria reads/writes via Google Sheets API.
# ═══════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────
# SHEET 1: LEAD DATABASE
# ─────────────────────────────────────────────────────────────
# Purpose: Every scraped lead from Google Places + Yelp

## Columns
| Column | Type | Source | Notes |
|--------|------|--------|-------|
| A: Lead ID | Auto (LEAD-001) | Aria generates | Unique identifier |
| B: Business Name | Text | Google Places | |
| C: Owner/Manager | Text | Website scrape | If found |
| D: Phone | Text | Google Places | |
| E: Email | Text | Website scrape | If found |
| F: Address | Text | Google Places | |
| G: City | Text | Google Places | |
| H: State | Text | Google Places | |
| I: Zip | Text | Google Places | |
| J: Website | URL | Google Places | |
| K: Vertical | Dropdown | Aria assigns | Barbershop, Dental, Vet, etc. |
| L: Review Count | Number | Google Places | |
| M: Rating | Number | Google Places | 1-5 stars |
| N: Score | HOT/WARM/COLD | Aria calculates | See scoring formula below |
| O: Voicemail Test | Yes/No/Untested | Aria calls | Did they go to voicemail? |
| P: Has AI/Service | Yes/No/Unknown | Website scrape | Disqualify if Yes |
| Q: Date Found | Date | Auto | |
| R: Source | Text | Google Places / Yelp | |
| S: Outreach Status | Dropdown | Aria updates | New / Emailed / Responded / Demo / Pilot / Paid / Nurture / Dead |
| T: Last Touch Date | Date | Aria updates | |
| U: Next Action | Text | Aria writes | What to do next |
| V: Notes | Text | Aria writes | Any context |
| W: Assigned To | Ian/Aria | | Who owns the relationship |

## Scoring Formula
```
Base Score = 0
+ Review Count > 20: +3
+ Review Count > 50: +2 more
+ Rating > 4.0: +1
+ Email found: +2
+ Owner name found: +1
+ Went to voicemail on test call: +3
+ No existing AI/service detected: +2
+ High-call vertical (dental, auto, vet, urgent care): +2
+ In target geography: +1

Score >= 10: HOT
Score 5-9: WARM
Score < 5: COLD
```

# ─────────────────────────────────────────────────────────────
# SHEET 2: OUTREACH TRACKER
# ─────────────────────────────────────────────────────────────
# Purpose: Track every email sent, follow-up status, responses

## Columns
| Column | Type | Notes |
|--------|------|-------|
| A: Lead ID | Reference | Links to Lead Database |
| B: Business Name | Text | |
| C: Contact Name | Text | |
| D: Email | Text | |
| E: Vertical | Text | |
| F: Cadence Stage | Dropdown | Day 1 / Day 3 / Day 7 / Day 14 / Day 21 / Nurture / Re-engage |
| G: Last Email Sent | Date | |
| H: Next Email Due | Date | Auto-calculated from cadence |
| I: Subject Line Used | Text | For A/B tracking |
| J: Template Used | Text | Reference to EMAIL_TEMPLATES.md |
| K: Opened | Yes/No | Resend analytics |
| L: Replied | Yes/No | |
| M: Reply Sentiment | Positive/Neutral/Negative | Aria assesses |
| N: Calendly Booked | Yes/No | |
| O: Demo Date | Date | |
| P: Demo Outcome | Hot/Warm/Not Fit | Ian reports |
| Q: Converted | Yes/No | |
| R: Total Emails Sent | Number | Count |
| S: Notes | Text | |

# ─────────────────────────────────────────────────────────────
# SHEET 3: CLIENT HEALTH DASHBOARD
# ─────────────────────────────────────────────────────────────
# Purpose: Real-time health monitoring for every paying client

## Columns
| Column | Type | Notes |
|--------|------|-------|
| A: Client ID | CLT-001 | |
| B: Business Name | Text | |
| C: Contact Name | Text | |
| D: Agent Name | Text | Mel, etc. |
| E: Monthly Rate | Currency | |
| F: Start Date | Date | |
| G: Tier | Starter/Core/Pro/Enterprise | |
| H: Calls This Month | Number | From Supabase |
| I: Calls Last Month | Number | For trend |
| J: Call Volume Trend | Up/Stable/Down | Auto-calculated |
| K: Avg Call Duration | Number (seconds) | From Supabase |
| L: Last Check-In | Date | |
| M: Next Check-In Due | Date | Per cadence |
| N: Email Open Rate | Percentage | Resend analytics |
| O: Last Issue Date | Date | |
| P: Days Since Issue | Number | Auto-calculated |
| Q: Health Score | 0-100 | Formula below |
| R: Risk Level | Green/Yellow/Red | From health score |
| S: Upsell Opportunity | Text | Aria identifies |
| T: Renewal Date | Date | |
| U: LTV To Date | Currency | Total paid so far |
| V: Notes | Text | |

## Health Score Formula
```
Agent uptime (30 pts):
  100% = 30, 99% = 25, 95-98% = 15, <95% = 0

Email delivery rate (20 pts):
  100% = 20, 95-99% = 15, 90-94% = 10, <90% = 0

Call volume trend (20 pts):
  Growing = 20, Stable = 15, Declining <25% = 10, Declining >25% = 0

Client responsiveness (15 pts):
  Replies to check-ins = 15, Opens but no reply = 10, Not opening = 0

Days since last issue (15 pts):
  >60 days = 15, 30-60 = 12, 14-30 = 8, 7-14 = 4, <7 = 0

TOTAL = sum of all categories (0-100)
90-100 = Green | 70-89 = Yellow | <70 = Red
```

# ─────────────────────────────────────────────────────────────
# SHEET 4: FINANCIAL TRACKER
# ─────────────────────────────────────────────────────────────
# Purpose: Monthly P&L, MRR tracking, growth metrics

## Tab: Monthly Revenue
| Column | Notes |
|--------|-------|
| A: Month | Jan 2026, Feb 2026, etc. |
| B: Total MRR | Sum of all client payments |
| C: New MRR | From new clients this month |
| D: Expansion MRR | From upsells |
| E: Churned MRR | Lost from cancellations |
| F: Net New MRR | C + D - E |
| G: MRR Growth % | F / previous month B |
| H: Total Clients | Count |
| I: New Clients | Count |
| J: Churned Clients | Count |
| K: ARPC | B / H |
| L: Churn Rate | J / previous H |
| M: Net Revenue Retention | (B - E + D) / previous B |

## Tab: Monthly Costs
| Column | Notes |
|--------|-------|
| A: Month | |
| B: Railway | Hosting costs |
| C: Twilio | Phone + minutes |
| D: ElevenLabs | Voice AI usage |
| E: Supabase | Database |
| F: Resend | Email |
| G: Google Workspace | Email + Drive |
| H: Domains | Amortized |
| I: Other | Miscellaneous |
| J: Total Costs | Sum |
| K: Gross Profit | Revenue - Costs |
| L: Gross Margin % | K / Revenue |

## Tab: Pipeline
| Column | Notes |
|--------|-------|
| A: Prospect | Name |
| B: Stage | Lead/Contacted/Engaged/Demo/Pilot/Negotiation |
| C: Potential MRR | Estimated |
| D: Probability | % chance of closing |
| E: Weighted Value | C × D |
| F: Expected Close | Date |
| G: Owner | Ian / Aria |
| H: Last Activity | Date |
| I: Next Step | Text |

# ─────────────────────────────────────────────────────────────
# SHEET 5: CONTENT PERFORMANCE
# ─────────────────────────────────────────────────────────────

## Columns
| Column | Notes |
|--------|-------|
| A: Date | Published date |
| B: Platform | LinkedIn / TikTok / YouTube / Instagram |
| C: Content Type | Text / Image / Video / Carousel |
| D: Topic | Brief description |
| E: Pillar | Demo / ROI / BTS / Thought Leadership |
| F: Hook Used | First line or first 3 seconds |
| G: CTA | What action was requested |
| H: Impressions | Views |
| I: Engagements | Likes + comments + shares |
| J: Engagement Rate | I / H |
| K: Link Clicks | If applicable |
| L: Click Rate | K / H |
| M: Signups Attributed | Tracked conversions |
| N: Revenue Attributed | From signups |
| O: Score | Aria rates 1-10 based on metrics vs targets |
| P: Notes | What worked / what didn't |
| Q: Repurpose? | Yes/No — flag top performers for repurposing |

# ─────────────────────────────────────────────────────────────
# SHEET 6: ANSWRDBY SUBSCRIBERS
# ─────────────────────────────────────────────────────────────

## Columns
| Column | Notes |
|--------|-------|
| A: Subscriber ID | SUB-001 |
| B: Name | |
| C: Email | |
| D: Phone (personal) | |
| E: Assigned Number | AnswrdBy Twilio number |
| F: Persona | Captain Flint, Chase, etc. |
| G: Tier | Starter / Pro / Elite |
| H: Monthly Rate | |
| I: Start Date | |
| J: Status | Active / Paused / Churned |
| K: Calls This Month | |
| L: Total Calls | Lifetime |
| M: Last Call Date | |
| N: Forwarding Active | Yes/No (are they actually using it?) |
| O: Last Check-In | |
| P: Referral Source | How they found us |
| Q: Referred By | If referral, who |
| R: Churn Risk | Low/Medium/High |
| S: Notes | |

# ─────────────────────────────────────────────────────────────
# SHEET 7: TELECOM PIPELINE
# ─────────────────────────────────────────────────────────────

## Columns
| Column | Notes |
|--------|-------|
| A: Company | Carrier name |
| B: Type | National / Regional / MVNO / VoIP |
| C: Subscribers | Estimated subscriber count |
| D: Contact Name | Decision-maker |
| E: Title | VP Product, etc. |
| F: Email | |
| G: LinkedIn | |
| H: Stage | Research / Outreach / Conversation / Demo / Pilot / Negotiation |
| I: Last Touch | Date |
| J: Next Step | |
| K: Potential ARR | Based on subscriber count × adoption × share |
| L: Notes | |

# ─────────────────────────────────────────────────────────────
# SHEET 8: PARTNER TRACKER
# ─────────────────────────────────────────────────────────────

## Columns
| Column | Notes |
|--------|-------|
| A: Partner ID | PTR-001 |
| B: Company | Agency/MSP name |
| C: Contact | |
| D: Email | |
| E: Type | Agency / MSP / Franchise Consultant |
| F: Revenue Share % | 20-25% |
| G: Status | Active / Pending / Inactive |
| H: Clients Referred | Count |
| I: Active Clients | Count (still paying) |
| J: MRR Attributed | Sum of referred client MRR |
| K: Share Owed This Month | J × F |
| L: Total Paid | Lifetime share paid |
| M: Last Activity | Date |
| N: Notes | |

# ─────────────────────────────────────────────────────────────
# SHEET 9: A/B TEST LOG
# ─────────────────────────────────────────────────────────────

## Columns
| Column | Notes |
|--------|-------|
| A: Test ID | ABT-001 |
| B: Hypothesis | "[Change] will increase [metric] by [amount]" |
| C: Variable Tested | Hook / CTA / Format / Visual / Copy / Time |
| D: Version A | Description |
| E: Version B | Description |
| F: Platform | Where tested |
| G: Start Date | |
| H: End Date | |
| I: Metric A | Result for version A |
| J: Metric B | Result for version B |
| K: Winner | A / B / Inconclusive |
| L: Lift | % improvement |
| M: Action Taken | What changed as a result |
| N: Applied To | Which templates/processes updated |

# ─────────────────────────────────────────────────────────────
# SHEET 10: INVESTOR CRM
# ─────────────────────────────────────────────────────────────

## Columns
| Column | Notes |
|--------|-------|
| A: Investor/Fund | Name |
| B: Type | Angel / Micro-VC / VC / Accelerator |
| C: Contact | Partner/person name |
| D: Email | |
| E: LinkedIn | |
| F: Check Size | Typical investment |
| G: Thesis Fit | Why they'd invest in InSync |
| H: Stage | Research / Outreach / Conversation / Meeting / Due Diligence / Term Sheet |
| I: Last Touch | Date |
| J: Next Step | |
| K: Warm Intro Available | Yes/No + through whom |
| L: Notes | |

# ─────────────────────────────────────────────────────────────
# SHEET 11: MILESTONE TRACKER
# ─────────────────────────────────────────────────────────────

## Columns
| Column | Notes |
|--------|-------|
| A: Milestone ID | MS-001 |
| B: Trigger | What metric/event triggers this |
| C: Threshold | Specific number or condition |
| D: Action | What Aria does when triggered |
| E: Status | Pending / Triggered / Completed |
| F: Date Triggered | When threshold was crossed |
| G: Date Completed | When action was executed |
| H: Notes | |

Pre-populate with ALL milestone triggers from:
- MASTER_OPERATING_SYSTEM.md
- BILLION_DOLLAR_PLAYBOOK.md
- ANSWRDBY_TELECOM_STRATEGY.md
- CREATIVE_PRODUCTION_ENGINE.md

# ─────────────────────────────────────────────────────────────
# SETUP INSTRUCTIONS
# ─────────────────────────────────────────────────────────────
#
# 1. Create a Google Sheet called "InSync Tech — Operations"
# 2. Create tabs for each sheet above (11 tabs)
# 3. Add column headers per the specs above
# 4. Share the sheet with the Google Service Account email
# 5. Note the Sheet ID from the URL
# 6. Add to Omen's .env: GOOGLE_SHEETS_ID=[sheet ID]
# 7. Test: Have Aria read row 1 of Lead Database
#
# OR: Create separate sheets per function for cleaner access:
# - InSync — Lead Database
# - InSync — Outreach Tracker
# - InSync — Client Health
# - InSync — Financials
# - InSync — Content Performance
# - InSync — AnswrdBy
# - InSync — Telecom Pipeline
# - InSync — Partners
# - InSync — A/B Tests
# - InSync — Investors
# - InSync — Milestones
# ═══════════════════════════════════════════════════════════════
