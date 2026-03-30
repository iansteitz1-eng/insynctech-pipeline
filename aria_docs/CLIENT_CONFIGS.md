# ═══════════════════════════════════════════════════════════════════
# CLIENT CONFIGS
# InSync Tech, Inc. — Agent Technical Configurations
# ═══════════════════════════════════════════════════════════════════
# Last Updated: March 21, 2026
# ═══════════════════════════════════════════════════════════════════

# 1. DEFAULT AGENT SETTINGS (Apply Unless Overridden)

| Setting | Default Value |
|---------|--------------|
| LLM Model | claude-sonnet-4-5 |
| Temperature | 0.0 |
| Voice ID | sqskhHdmEWFUgFIrJEuI (Aria standard) |
| Stability | 0.5 |
| Similarity Boost | 0.75 |
| Speed | 1.2 |
| Expressive Mode | true |
| Optimize Streaming Latency | 4 |
| Turn Timeout | 1.5s |
| Turn Eagerness | eager |
| Speculative Turn | true |
| Webhook URL | https://aria-backend-production-ebb5.up.railway.app/webhook/elevenlabs |

---

# 2. LIVE AGENTS

## Agent: Aria — InSync Tech (Sales/Demo)
| Field | Value |
|-------|-------|
| Agent ID | agent_5301kh0dggavef5ty3cqpn04j6bb |
| Phone | (727) 334-8156 |
| Voice | sqskhHdmEWFUgFIrJEuI (standard) |
| Purpose | Inbound sales, product demos, general inquiries |
| Post-Call Email | ian@insynctech.io |
| Overrides | None — uses all defaults |

## Agent: Mel — Venice Barbershop
| Field | Value |
|-------|-------|
| Agent ID | agent_6501kkabjkvbfg6vr91q5aer133k |
| Phone | (941) 390-1732 |
| Voice | NmpxQl3ZUbfh8HgoNCGM (male) |
| Voice Stability | 0.4 (override — lower for more natural male sound) |
| Purpose | Walk-in barbershop receptionist — hours, wait times, services, pricing |
| Post-Call Email | veniceflbarbershop@gmail.com + ian@insynctech.io |
| Special Config | NO appointment booking (walk-in only) |
| Client | John, Torchwood Barbers LLC |

## Agent: Great Clips Demo
| Field | Value |
|-------|-------|
| Agent ID | agent_5301khf4wfmded0are41vwvrjexk |
| Phone | (941) 222-2160 |
| Voice | sqskhHdmEWFUgFIrJEuI (standard) |
| Purpose | Demo for Jack Leaf / Great Clips franchise pitch |
| Post-Call Email | ian@insynctech.io |
| Overrides | None |

## Agent: Auto Dealership Demo
| Field | Value |
|-------|-------|
| Agent ID | agent_6201kkysjbb2fprtxpne36c258j3 |
| Phone | (941) 294-3348 — ⚠️ BLOCKED |
| Voice | sqskhHdmEWFUgFIrJEuI (standard) |
| Purpose | Demo for auto dealership service dept vertical |
| Status | Phone number blocked — Twilio auth token issue, support ticket open |
| Post-Call Email | ian@insynctech.io |

## Agent: AnswrdBy Widget
| Field | Value |
|-------|-------|
| Agent ID | agent_6101khp554czec9anpe6es8fy0yn |
| Phone | N/A (widget only) |
| Purpose | AnswrdBy.ai website chat widget |
| Post-Call Email | N/A |

## Agent: Aria Docs Assistant
| Field | Value |
|-------|-------|
| Agent ID | agent_8101km6nf23te9bv96899yvxkahj |
| Phone | N/A (widget) |
| Purpose | Documentation assistant for Aria product |

## Agent: Aria API Assistant
| Field | Value |
|-------|-------|
| Agent ID | agent_4001km6nf34rfvdt6rsbfhfdte1m |
| Phone | N/A (widget) |
| Purpose | API documentation assistant |

## Agent: CertusOrdo Docs Assistant
| Field | Value |
|-------|-------|
| Agent ID | agent_0101km6nf43pf4db2v8he1nfn6b1 |
| Phone | N/A (widget) |
| Purpose | CertusOrdo documentation assistant |

---

# 3. WEBHOOK ROUTING TABLE

```
webhook_router.py mapping:

agent_5301kh0dggavef5ty3cqpn04j6bb → ian@insynctech.io (Aria)
agent_6501kkabjkvbfg6vr91q5aer133k → veniceflbarbershop@gmail.com + ian@insynctech.io (Mel)
agent_5301khf4wfmded0are41vwvrjexk → ian@insynctech.io (GC Demo)
agent_6201kkysjbb2fprtxpne36c258j3 → ian@insynctech.io (Auto Demo)

DEFAULT: Unknown agent_id → ian@insynctech.io (safety catch)
```

---

# 4. CERTUSRODO REGISTRATION (Aria-COO)

| Field | Value |
|-------|-------|
| Org ID | [STORED IN .ENV ON OMEN] |
| API Key | [STORED IN .ENV ON OMEN] |
| Agent ID | [STORED IN .ENV ON OMEN] |
| Agent Secret | [STORED IN .ENV ON OMEN] |
| Private Key | [STORED ON M4 MAC ONLY] |

---

# 5. INFRASTRUCTURE ENDPOINTS

| Service | URL | Purpose |
|---------|-----|---------|
| Aria Backend | https://aria-backend-production-ebb5.up.railway.app | Webhook processing, post-call pipeline |
| CertusOrdo API | https://web-production-b910f.up.railway.app | Trust layer API |
| CertusOrdo Swagger | https://web-production-b910f.up.railway.app/docs | API documentation |
| CertusOrdo Docs | https://certusrodo-docs-site.netlify.app | Public docs |
| CertusOrdo Dashboard | https://certusrodo-dashboard.netlify.app | Customer dashboard |
| Operations Tracker | https://co-db-tracker.netlify.app | Internal operations |
| Metrics Dashboard | https://certusordo-metrics.netlify.app | Performance metrics |
| InSync Website | https://insynctech.io | Company website |
| AnswrdBy Website | https://answrdby.ai | Consumer product |
| Aria Portal | https://aria-insynctech.ai | Aria product site |

---

# 6. ADDING A NEW CLIENT

When deploying a new client agent, update this file with:
1. Agent name, ID, phone number
2. Voice ID and any overrides
3. Post-call email routing
4. Special configuration notes
5. Add to webhook_router.py mapping
6. Add to CLIENT_REGISTRY.md

# ═══════════════════════════════════════════════════════════════════
# END OF CLIENT CONFIGS
# ═══════════════════════════════════════════════════════════════════
