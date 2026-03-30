# ═══════════════════════════════════════════════════════════════════
# FINANCIAL DASHBOARD
# InSync Tech, Inc. — Revenue, Costs, Margins & Projections
# ═══════════════════════════════════════════════════════════════════
# Last Updated: March 21, 2026
# Update monthly or after any significant change.
# ═══════════════════════════════════════════════════════════════════

# 1. CURRENT SNAPSHOT (March 2026)

| Metric | Value |
|--------|-------|
| MRR | $99 |
| ARR | $1,188 |
| Paying Clients | 1 |
| Pipeline Value | $280,000+ |
| Monthly Fixed Costs | ~$75 |
| Monthly Variable Costs (per client) | ~$30 |
| Gross Margin (current) | ~$69/mo (~70% at 1 client) |
| Net Cash Position | [Ian to update] |
| Runway (months at current burn) | [Ian to update] |

---

# 2. REVENUE BREAKDOWN

## Active Revenue Streams
| Source | Monthly | Annual | Status |
|--------|---------|--------|--------|
| Mel — Venice Barbershop | $99 | $1,188 | ✅ Active |
| **Total MRR** | **$99** | **$1,188** | |

## Pipeline Revenue (Not Yet Closed)
| Prospect | Potential MRR | Potential ARR | Stage |
|----------|--------------|---------------|-------|
| Great Clips (26 loc) | $6,500 | $78,000 | Contacted — Pilot offered |
| Auto Dealerships (target) | $2,500-5,000 | $30-60K | Demo ready, no outreach |
| Cole's Postal Center | $149-249 | $1,788-2,988 | Demo built |
| SMB Pipeline (150+ leads) | $15,000-30,000 | $180-360K | Various stages |
| **Total Pipeline** | **$24,349-41,749** | **~$290-500K** | |

## Future Revenue Streams (Not Yet Launched)
| Product | Est. MRR at Scale | Launch Blocker |
|---------|-------------------|----------------|
| AnswrdBy.ai | $1,250+ (50 subs) | Twilio A2P + automation pipeline |
| CertusOrdo SaaS | $1,500+ (3 customers) | Need first paying customer |
| Blueprint PDF | $9,940 one-time (20 copies) | Not launched, not marketed |
| Website Dev | $500-1,000/mo | Not actively sold |

---

# 3. COST STRUCTURE

## Fixed Monthly Costs
| Item | Amount | Vendor | Notes |
|------|--------|--------|-------|
| Railway (aria-backend) | ~$15-20 | Railway | Scales with traffic |
| Railway (CertusOrdo API) | ~$10-15 | Railway | Scales with transactions |
| Twilio (phone numbers) | ~$4 | Twilio | $1/number/mo × ~4 numbers |
| Google Workspace | ~$12 | Google | Single user |
| Domain renewals (amortized) | ~$5 | Cloudflare/Namecheap | Multiple domains |
| Supabase | $0 | Supabase | Free tier currently |
| Netlify | $0 | Netlify | Free tier (5 sites) |
| Resend | $0 | Resend | Free tier (100/day) |
| ElevenLabs platform | $0-22 | ElevenLabs | Usage-based, may need paid tier |
| **Total Fixed** | **~$50-80** | | |

## Variable Costs Per Client
| Item | Amount | Notes |
|------|--------|-------|
| ElevenLabs voice minutes | $0.10-0.30/min | ~$15-25/client/mo at avg volume |
| Twilio voice minutes | $0.0085/min inbound | ~$2-5/client/mo |
| Resend email delivery | $0 | Until exceeding free tier |
| Railway compute (marginal) | ~$2-5 | Shared across clients |
| **Total Variable/Client** | **~$20-35** | |

## Cost Scaling Thresholds
| Clients | Est. Monthly Cost | Trigger |
|---------|-------------------|---------|
| 1-10 | $80-150 | Current infrastructure handles this |
| 11-25 | $150-400 | May need Supabase paid tier ($25/mo) |
| 26-50 | $400-800 | Resend paid tier ($20/mo), Railway scaling |
| 51-100 | $800-1,500 | ElevenLabs enterprise plan, dedicated Railway |
| 100+ | $1,500-3,000 | Full infrastructure review needed |

---

# 4. UNIT ECONOMICS

| Metric | Formula | Value |
|--------|---------|-------|
| ARPC (Avg Revenue Per Client) | Sum of MRR / # clients | $250/mo (blended target) |
| COGS Per Client | ElevenLabs + Twilio + Resend + Railway share | ~$30/mo |
| Gross Margin Per Client | ARPC - COGS | ~$220/mo |
| Gross Margin % | Margin / ARPC | ~88% |
| CAC (Current) | Ian's time per close (est. 4 hrs × $75/hr) | ~$300 |
| LTV | ARPC × Margin% × Avg Lifetime (18 mo) | ~$3,960 |
| LTV:CAC | LTV / CAC | 13:1 |
| Payback Period | CAC / Monthly Margin | 1.4 months |
| Break-Even (company) | Fixed costs / Margin per client | <1 client |

---

# 5. GROWTH PROJECTIONS

## Conservative Model (5 new clients/month)
| Month | New | Total | MRR | Monthly Cost | Profit |
|-------|-----|-------|-----|-------------|--------|
| Apr 2026 | 5 | 6 | $1,500 | $260 | $1,240 |
| May 2026 | 5 | 11 | $2,750 | $410 | $2,340 |
| Jun 2026 | 5 | 16 | $4,000 | $560 | $3,440 |
| Jul 2026 | 5 | 21 | $5,250 | $710 | $4,540 |
| Aug 2026 | 5 | 26 | $6,500 | $860 | $5,640 |
| Sep 2026 | 5 | 31 | $7,750 | $1,010 | $6,740 |
| **Q2 Total** | | | | | **$7,020** |
| **Q3 Total** | | | | | **$16,920** |

## Aggressive Model (Great Clips + 5 SMB/month)
| Month | MRR | Notes |
|-------|-----|-------|
| Apr 2026 | $1,849 | 3 GC pilot locations + 5 SMB |
| May 2026 | $3,599 | GC pilot active + 10 SMB |
| Jun 2026 | $10,099 | GC 26-location rollout begins + 15 SMB |
| Jul 2026 | $12,349 | Full GC + 20 SMB |
| **Q2 Exit MRR** | **$10,099-12,349** | |

## Blueprint PDF Revenue (One-Time Injection)
| Scenario | Copies | Revenue |
|----------|--------|---------|
| Low | 10 | $4,970 |
| Medium | 20 | $9,940 |
| High | 50 | $24,850 |

---

# 6. KEY FINANCIAL RATIOS TO TRACK

| Ratio | Target | Current | Status |
|-------|--------|---------|--------|
| Gross Margin | >80% | ~70% | 🟡 Improves with scale |
| LTV:CAC | >3:1 | 13:1 | 🟢 Exceptional |
| MRR Growth Rate | >20% QoQ | N/A (1 client) | 🔴 Need clients |
| Net Revenue Retention | >100% | N/A | Track after 6 months |
| CAC Payback | <3 months | 1.4 months | 🟢 |
| Churn Rate | <5% monthly | 0% | 🟢 (1 client, too early) |
| Revenue per Employee | >$100K/yr | $1,188/yr | 🔴 Need revenue |
| Burn Multiple | <2x | N/A | Track with investment |

---

# 7. FINANCIAL RULES

1. **Never commit spend over $500 without Ian's approval**
2. **Setup fees collected BEFORE work begins (exceptions: pilots only)**
3. **Monthly subscriptions auto-charge on 1st via Stripe**
4. **7-day grace period on failed payments → then pause service**
5. **30 days overdue → escalate to Ian**
6. **Maintain 3-month fixed-cost reserve minimum ($225)**
7. **Every financial transaction logged in CertusOrdo**
8. **Stripe must be switched from TEST to LIVE mode (BLOCKER)**
9. **Track per-client profitability monthly**
10. **Review cost structure when crossing 10, 25, 50, 100 client thresholds**

---

# 8. STRIPE PAYMENT LINKS (Current)

| Product | Link | Mode |
|---------|------|------|
| AI Starter ($799) | https://buy.stripe.com/28E7sKa3c1Yr8EN9jI0ZW04 | ⚠️ Verify LIVE |
| AI Growth ($1,499) | https://buy.stripe.com/4gMdR87V47iLaMV1Rg0ZW03 | ⚠️ Verify LIVE |
| AI Premium ($2,499) | https://buy.stripe.com/aFa5kCfnw0Un1cl53s0ZW02 | ⚠️ Verify LIVE |

**ACTION NEEDED:** Confirm all Stripe links are in LIVE mode, not TEST.

# ═══════════════════════════════════════════════════════════════════
# END OF FINANCIAL DASHBOARD
# ═══════════════════════════════════════════════════════════════════
