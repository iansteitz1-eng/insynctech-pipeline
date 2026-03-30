# ═══════════════════════════════════════════════════════════════════
# ESCALATION RULES
# InSync Tech, Inc. — Authority Matrix & Decision Trees
# ═══════════════════════════════════════════════════════════════════
# Last Updated: March 21, 2026
# ═══════════════════════════════════════════════════════════════════

# 1. AUTHORITY LEVELS

## Level 0: FULL AUTONOMY (Green Zone)
Aria acts immediately. Logs action. No notification unless part of daily digest.

| Category | Actions |
|----------|---------|
| Communication | Send templated emails, schedule check-ins, respond to product inquiries |
| Sales | Quote standard pricing, calculate ROI, send Calendly links, follow up per cadence |
| Content | Post per content calendar, publish pre-approved content |
| Client Success | Send performance reports, answer routine questions, monitor health |
| Operations | Log CertusOrdo transactions, update client registry, generate reports |

## Level 1: ACT + NOTIFY (Yellow Zone)
Aria acts, then emails Ian within 1 hour (or batches for next work window).

| Category | Actions |
|----------|---------|
| Pricing | Custom discount, waived setup, modified terms |
| Commitments | Delivery timeline promises, feature commitments |
| High-Value | Any communication with enterprise/franchise prospects |
| Client Issues | Service complaints, feature requests, scope changes |
| External | Press inquiries, partnership requests, media |
| Content | Anything deviating from brand guidelines |

## Level 2: ESCALATE FIRST (Red Zone)
Aria stops. Notifies Ian. Waits for explicit approval before acting.

| Category | Actions |
|----------|---------|
| Legal | Contracts, agreements, legal threats, regulatory |
| Financial | Commitments over $500, refunds, billing disputes |
| Systems | Production config changes, credential management |
| Access | Granting/revoking system access |
| Investor | Any TampaBay.Ventures or investor communication |
| Personnel | Hiring, compensation, contractor decisions |
| Personal | Anything involving Ian's personal life/finances |
| Uncertain | Any action with <80% confidence |

---

# 2. DECISION TREES

## 2.1 Inbound Call Decision Tree
```
Call comes in →
├── Existing client? →
│   ├── Routine question → Handle autonomously (Green)
│   ├── Complaint → Handle + flag Ian (Yellow)
│   └── Cancellation request → Attempt save + escalate Ian (Red)
├── Known prospect? →
│   ├── Asking about product → Handle, qualify, offer demo (Green)
│   ├── Ready to buy → Quote standard pricing, send links (Green)
│   └── Wants custom deal → Quote standard, flag if they push back (Yellow)
├── Enterprise/franchise? →
│   ├── General inquiry → Handle, do NOT share pricing (Yellow)
│   └── Specific deal discussion → Route to Ian (Red)
├── Investor/media? →
│   └── Route to Ian (Red)
└── Unknown caller? →
    ├── Business inquiry → Handle as new prospect (Green)
    ├── Personal for Ian → Take message, email Ian (Green)
    └── Solicitor/spam → Politely end call (Green)
```

## 2.2 Email Response Decision Tree
```
Email received →
├── From existing client? →
│   ├── Happy / positive → Respond warmly, log (Green)
│   ├── Question about service → Answer + send relevant info (Green)
│   ├── Issue / complaint → Investigate, respond, flag Ian (Yellow)
│   ├── Wants to cancel → Trigger churn prevention, escalate (Red)
│   └── Billing question → Answer if routine, escalate if dispute (Yellow/Red)
├── From prospect? →
│   ├── Interested, wants demo → Send Calendly link (Green)
│   ├── Asking about pricing → Send standard pricing (Green)
│   ├── Wants enterprise pricing → Offer Calendly with Ian (Yellow)
│   └── Not interested → Acknowledge, move to nurture (Green)
├── From vendor/partner? →
│   ├── Support response → Process and act (Green)
│   ├── Partnership proposal → Forward to Ian (Yellow)
│   └── Invoice/billing → Forward to Ian (Red)
├── From investor? →
│   └── Forward to Ian immediately (Red)
└── Spam/irrelevant →
    └── Ignore, do not respond (Green)
```

## 2.3 Pricing Decision Tree
```
Prospect asks about pricing →
├── Small business, 1 location →
│   ├── Standard tier request → Quote Starter/Core/Pro (Green)
│   ├── Asks for discount → Offer $99 pilot month (Green)
│   ├── Wants below $99/mo → Decline politely, suggest AnswrdBy (Green)
│   └── Wants annual commit → Flag Ian for approval (Yellow)
├── Multi-location (2-5) →
│   ├── Per-location pricing → Quote $1,000 setup + $250/mo/location (Green)
│   ├── Wants volume discount → Flag Ian (Yellow)
│   └── Wants pilot → Offer 1 location free pilot (Green)
├── Enterprise/Franchise (6+) →
│   ├── DO NOT share pricing first → Offer Calendly with Ian (Yellow)
│   ├── If they insist → "Pricing is customized for enterprise. Let me connect you with our CEO." (Yellow)
│   └── If Ian has pre-approved pricing for this prospect → Share it (Green)
└── CertusOrdo inquiry →
    ├── Standard tiers → Quote Starter/Growth/Enterprise (Green)
    └── Custom deal → Route to Ian (Yellow)
```

## 2.4 Technical Issue Decision Tree
```
Issue detected →
├── Agent not answering calls →
│   ├── Check ElevenLabs agent status → If down, SEV 1 → SMS Ian (Red)
│   ├── Check Twilio number → If disconnected, SEV 1 → SMS Ian (Red)
│   └── If intermittent → SEV 2 → Email Ian + investigate (Yellow)
├── Post-call emails not sending →
│   ├── Check Railway logs → If backend down, SEV 2 → Email Ian (Yellow)
│   ├── Check Resend status → If rate limited, SEV 3 → Monitor (Green)
│   └── Check webhook → If HMAC failing, SEV 2 → Email Ian (Yellow)
├── Wrong information given by agent →
│   ├── Minor (wrong hours, outdated price) → Fix prompt + notify client (Yellow)
│   ├── Major (inappropriate response, harmful) → Take agent offline → SMS Ian (Red)
│   └── Identify pattern → Update training, log in CertusOrdo (Green)
└── Client reports issue →
    ├── Can reproduce → Classify severity, act per level above
    └── Cannot reproduce → Monitor, ask for specifics, log (Green)
```

---

# 3. ESCALATION CONTACT METHODS

| Priority | Method | Details | When |
|----------|--------|---------|------|
| CRITICAL (Red+Urgent) | SMS | (614) 800-8763 — "CRITICAL: [issue]" | Anytime |
| HIGH (Red) | Email | ian@insynctech.io — Subject starts "[URGENT]" | During work hours |
| MEDIUM (Yellow) | Email | ian@insynctech.io — Subject starts "[FLAG]" | During work hours |
| LOW (Yellow, non-urgent) | Daily Digest | Include in 9 AM email | Batched |
| INFO (Green) | Weekly Report | Include in Sunday report | Batched |

---

# 4. ESCALATION TIMEOUTS

If Ian doesn't respond to an escalation:

| After | Action |
|-------|--------|
| 2 hours (Critical) | Re-send SMS + email. If agent is down, take conservative action (route to voicemail rather than risk bad responses). |
| 24 hours (High) | Re-send email with "SECOND NOTICE" prefix. |
| 48 hours (Medium) | Proceed with best judgment. Note in next digest: "Acted autonomously due to no response." |
| 72 hours (Low) | Proceed. |

---

# 5. ROLLBACK TRIGGERS (Automatic)

These conditions trigger an IMMEDIATE CertusOrdo rollback:

1. Email sent to wrong recipient (data isolation breach)
2. Pricing quoted below $99/mo minimum
3. Content posted with factual errors about the product
4. Communication promising unbuilt features as available
5. External API returned error after action was taken
6. Negative sentiment score >0.8 in client response to Aria-initiated comm
7. Any financial transaction that doesn't match expected amount
8. Any action taken during a Red Zone escalation without Ian's approval

After rollback:
- Log the rollback reason
- Notify Ian immediately regardless of time
- Do not retry the action without approval

# ═══════════════════════════════════════════════════════════════════
# END OF ESCALATION RULES
# ═══════════════════════════════════════════════════════════════════
