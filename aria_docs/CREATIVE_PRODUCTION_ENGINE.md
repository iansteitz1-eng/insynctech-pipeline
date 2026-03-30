# ═══════════════════════════════════════════════════════════════════════════════
# CREATIVE PRODUCTION ENGINE
# InSync Tech, Inc. — Aria's AI-Native Marketing Production System
# ═══════════════════════════════════════════════════════════════════════════════
# Version: 1.0 | March 22, 2026
# Aria Division: 16 — Creative Production
# ═══════════════════════════════════════════════════════════════════════════════
#
# PHILOSOPHY:
# Every piece of content Aria creates must do ONE thing: CONVERT.
# Beautiful content that doesn't convert is a hobby, not a business.
#
# The production stack:
#   Nano Banana Pro (via ElevenLabs) → Images, character renders, thumbnails
#   Veo 3.1 / Sora 2 / Kling 2.5 (via ElevenLabs) → Video generation
#   ElevenLabs Voice → Voiceovers, persona demos, narration
#   ElevenLabs OmniHuman → Talking avatar lip-sync
#   ElevenLabs Studio → Full production assembly
#   Claude (via OpenClaw) → Scripts, copy, strategy, optimization
#
# This is NOT a content calendar. The CONTENT_CALENDAR.md tells Aria
# WHAT to post and WHEN. This document tells Aria HOW to produce it
# at studio quality and HOW to make it convert.
# ═══════════════════════════════════════════════════════════════════════════════


# TABLE OF CONTENTS
# 1.  THE PRODUCTION STACK (Tools & Pipeline)
# 2.  VISUAL IDENTITY SYSTEM (Nano Banana Character Bible)
# 3.  VIDEO PRODUCTION PLAYBOOK
# 4.  ANSWRDBY PERSONA VISUAL SYSTEM
# 5.  INSYNC B2B VISUAL SYSTEM
# 6.  CERTUSRODO VISUAL SYSTEM
# 7.  CONVERSION FRAMEWORK (Every Asset Must Convert)
# 8.  A/B TESTING & OPTIMIZATION ENGINE
# 9.  PLATFORM-SPECIFIC PRODUCTION SPECS
# 10. ARIA'S CREATIVE WORKFLOW (Division 16)
# 11. PROMPT LIBRARY (Nano Banana + Video)


# ═══════════════════════════════════════════════════════════════════════════════
# 1. THE PRODUCTION STACK
# ═══════════════════════════════════════════════════════════════════════════════

## The Full Pipeline (All Inside ElevenLabs Ecosystem)

```
STEP 1: CONCEPT (Claude on OpenClaw)
   Aria writes the script, selects the content type,
   chooses the visual direction, drafts the CTA.
        │
        ▼
STEP 2: VISUALS (Nano Banana Pro via ElevenLabs)
   Generate character renders, product mockups,
   thumbnail images, scene backgrounds.
   ───→ Character consistency via identity tokens
   ───→ 4K resolution for quality scaling
   ───→ Precise text rendering for overlays
        │
        ▼
STEP 3: MOTION (Veo 3.1 / Sora 2 / Kling via ElevenLabs)
   Animate Nano Banana stills into video clips.
   ───→ Image-to-video for character animation
   ───→ Text-to-video for scene generation
   ───→ Camera movements (zoom, pan, dolly)
        │
        ▼
STEP 4: VOICE (ElevenLabs Voice AI)
   Add voiceover narration or persona voice demos.
   ───→ Aria's voice (sqskhHdmEWFUgFIrJEuI) for brand narration
   ───→ Persona voices for AnswrdBy demos
   ───→ Ian's cloned voice for founder content (if cloned)
        │
        ▼
STEP 5: LIP-SYNC (OmniHuman 1.5 via ElevenLabs)
   Sync voice to character face for talking-head content.
   ───→ Persona avatars speaking with their actual voice
   ───→ "Meet Captain Flint" showcase videos
        │
        ▼
STEP 6: ASSEMBLY (ElevenLabs Studio)
   Combine video + voice + music + SFX + captions.
   ───→ Background music (ElevenMusic)
   ───→ Sound effects (AI-generated)
   ───→ Caption overlay
   ───→ Export in platform-specific formats
        │
        ▼
STEP 7: OPTIMIZE (Claude on OpenClaw)
   Aria writes platform-specific copy, hashtags, CTAs.
   Schedules posting per CONTENT_CALENDAR.md.
   Tracks performance. Iterates.
```

## Tool Access for Aria on the Omen

| Tool | Access Method | API Available? | Notes |
|------|-------------|---------------|-------|
| Nano Banana Pro | ElevenLabs platform (browser) | Yes — via ElevenLabs API | Requires paid ElevenLabs plan |
| Veo 3.1 / Sora 2 | ElevenLabs Image & Video | Yes — via ElevenLabs API | Credit-based |
| ElevenLabs Voice | Already connected (Aria backend) | Yes | Already have API key |
| OmniHuman 1.5 | ElevenLabs platform | Yes — via API | Lip-sync from image + audio |
| ElevenLabs Studio | Browser-based | Export via API | Full timeline editing |
| Claude | OpenClaw native | Yes | Scripts, copy, strategy |

### OpenClaw Integration Approach
Aria uses ElevenLabs' API to:
1. Generate images via Nano Banana (text-to-image endpoint)
2. Generate video clips via supported models (image-to-video endpoint)
3. Generate voice audio (already integrated)
4. Apply lip-sync via OmniHuman
5. Export assembled content

For complex productions, Aria generates all assets via API, then Ian
does final assembly in ElevenLabs Studio on the M4 Mac if needed.
For simple posts (image + text overlay), Aria handles everything autonomously.


# ═══════════════════════════════════════════════════════════════════════════════
# 2. VISUAL IDENTITY SYSTEM (Nano Banana Character Bible)
# ═══════════════════════════════════════════════════════════════════════════════

## Why Character Consistency Matters

Nano Banana Pro's identity tokens maintain character consistency across scenes.
This means Aria, AnswrdBy personas, and InSync's visual identity stay
EXACTLY THE SAME across every piece of content. No random variation.
This builds brand recognition faster than anything else.

## InSync Tech Brand Characters

### Aria (The AI COO)
```
NANO BANANA IDENTITY PROMPT:
"Professional AI assistant woman, sleek modern design, soft blue
holographic glow, clean minimal aesthetic, dark navy background,
confident warm expression, business-casual attire, subtle technology
elements integrated into design — circuit patterns in jewelry,
holographic interface reflections in eyes. Photorealistic style
with slight futuristic enhancement. Consistent identity token."

COLOR PALETTE:
- Primary: Deep navy (#1a1a2e)
- Accent: Electric blue (#4361ee)
- Glow: Soft cyan (#00d4ff)
- Skin: Warm natural tones

USE FOR:
- LinkedIn post thumbnails
- Daily briefing header images
- Website hero images
- Presentation slides
- "Aria says..." social content
```

### Ian (The Founder)
```
USE REAL PHOTOS OF IAN — not AI-generated.
For content that needs Ian's face, use actual photos or video.
AI-generated Ian = uncanny valley = hurts trust.
Exception: Stylized illustrations or abstract representations are OK.
```

### The InSync Brand Mark
```
NANO BANANA PROMPT:
"Sleek modern tech company logo environment, dark navy and electric
blue color scheme, clean lines, subtle AI circuit patterns, minimal
and professional, premium SaaS aesthetic. No text."

USE FOR:
- Social media backgrounds
- Video intro/outro frames
- Presentation templates
- Email header graphics
```

## AnswrdBy Persona Characters (CRITICAL — These Sell the Product)

Each AnswrdBy persona needs a CONSISTENT visual identity that appears
across every piece of marketing. Nano Banana's identity tokens make this possible.

### Captain Flint (The Pirate)
```
NANO BANANA IDENTITY PROMPT:
"Charismatic AI pirate character, weathered leather tricorn hat,
confident smirk, gold tooth glint, dark beard neatly trimmed,
rich crimson and gold color palette, warm atmospheric lighting,
vintage nautical elements — compass, ship wheel, old maps.
Photorealistic with cinematic depth of field. Character portrait
for marketing materials. Consistent identity token."

VOICE: Deep, warm, playful authority with subtle pirate inflection
PERSONALITY: Charming rogue. Takes messages like a captain taking orders.
TAGLINE: "Your calls are in good hands, matey."
```

### Chase Sterling (The Bodyguard)
```
NANO BANANA IDENTITY PROMPT:
"Professional AI bodyguard character, sharp black suit, dark
sunglasses, earpiece visible, strong jawline, calm composed
expression, standing in luxury environment — marble lobby, black
SUV in background. Photorealistic, moody cinematic lighting,
deep shadows. Consistent identity token."

VOICE: Low, calm, authoritative. No wasted words.
PERSONALITY: Screens every call like he's screening threats.
TAGLINE: "This line is protected. State your business."
```

### Dr. Marcus Webb (The Physician)
```
NANO BANANA IDENTITY PROMPT:
"Distinguished AI doctor character, salt-and-pepper hair, warm
knowing smile, white coat over professional attire, stethoscope,
warm wood-paneled office background with medical books, soft warm
lighting. Photorealistic, trustworthy, approachable. Consistent
identity token."

VOICE: Warm, measured, reassuring. Like a doctor with all the time in the world.
PERSONALITY: Takes every call seriously. Makes callers feel heard.
TAGLINE: "The doctor will see your call now."
```

### Reginald (The Butler)
```
NANO BANANA IDENTITY PROMPT:
"Refined AI butler character, silver hair perfectly groomed,
impeccable three-piece suit, subtle bow tie, distinguished posture,
standing in grand manor entrance — dark wood, brass fixtures,
subtle luxury. Photorealistic, warm but formal. Consistent
identity token."

VOICE: Refined British accent, unhurried, supremely capable.
PERSONALITY: Treats every caller as a distinguished guest.
TAGLINE: "How may I be of service?"
```

### RULE: Generate Each Persona 10+ Times Before Locking Identity
Use Nano Banana to generate each character in multiple poses, angles,
and scenarios. Pick the BEST rendition. Lock the identity token.
All future content uses that locked identity for consistency.


# ═══════════════════════════════════════════════════════════════════════════════
# 3. VIDEO PRODUCTION PLAYBOOK
# ═══════════════════════════════════════════════════════════════════════════════

## Video Types by Product

### AnswrdBy Videos (Highest Priority — Viral Potential)

**Type 1: Persona Introduction (15-30s)**
```
PRODUCTION:
1. Nano Banana: Generate persona portrait (locked identity)
2. OmniHuman: Animate portrait with persona voice speaking intro
3. Voice: "I'm Captain Flint. When your phone rings, I answer."
4. Video model: Slow cinematic zoom into portrait
5. Text overlay: Persona name + "Your AI. Your Personality."
6. End card: AnswrdBy logo + "answrdby.ai"

CONVERSION ELEMENT: "Pick your persona → link in bio"
```

**Type 2: Live Call Demo (30-60s)**
```
PRODUCTION:
1. Screen recording of phone calling AnswrdBy number (Ian records on M4)
2. Split screen: Phone screen + AI persona image
3. Persona voice plays live from the call
4. Text overlay: Captions of the conversation
5. Post-call: Show text summary arriving
6. End card: "Never answer your phone again."

CONVERSION ELEMENT: "Comment PERSONA to try it free"
```

**Type 3: Persona Comparison (30-45s)**
```
PRODUCTION:
1. Same incoming call scenario
2. Split into 4 quadrants: Flint, Chase, Marcus, Reginald
3. Each answers the SAME call in their style
4. Show how different each conversation is
5. End card: "Which one are you?"

CONVERSION ELEMENT: Poll in comments → drives engagement + link in bio
```

**Type 4: Reaction Content (30-60s)**
```
PRODUCTION:
1. Real person calls an AnswrdBy number (not knowing what to expect)
2. Film their face as the persona answers
3. Their genuine reaction IS the content
4. End: reveal it's AI + show the product
5. CTA: "Try it yourself"

CONVERSION ELEMENT: Authenticity drives shares → organic reach
```

### InSync B2B Videos

**Type 1: Before/After Call Demo (30s)**
```
PRODUCTION:
1. Scene 1: Phone rings → voicemail → sad trombone SFX
2. Scene 2: Phone rings → AI answers → smooth conversation
3. Text overlay: "Same call. Different outcome."
4. Revenue math overlay: "$5,280/month in missed revenue"
5. End card: InSync logo + "(727) 334-8156 — Call our demo"

CONVERSION ELEMENT: Demo phone number = direct action
```

**Type 2: ROI Calculator Walkthrough (45-60s)**
```
PRODUCTION:
1. Nano Banana: Generate clean calculator/dashboard graphic
2. Animate numbers filling in (step by step)
3. Voice (Aria): Walks through the math
4. Final number reveal with emphasis animation
5. End: "Your ROI → calendly link"

CONVERSION ELEMENT: Specific dollar amount = urgency
```

**Type 3: Client Testimonial (30-60s)**
```
PRODUCTION:
1. Real video of client (John from Venice Barbershop)
2. Or: Stylized quote card with Nano Banana background
3. Voice: Client quote read by Aria or shown as text
4. Stats overlay: calls handled, revenue protected
5. End card: "Join [X] businesses using InSync AI"

CONVERSION ELEMENT: Social proof → trust → book a demo
```

### CertusOrdo Videos (Developer/Enterprise)

**Type 1: "The Gap" Explainer (60s)**
```
PRODUCTION:
1. Nano Banana: Dark, moody tech backgrounds
2. Text animation: "$130M invested in agent identity"
3. Visual: Grid of competitor logos
4. Dramatic reveal: "ZERO invested in agent rollback"
5. CertusOrdo logo appears: "Until now."
6. Quick Swagger UI demo montage

CONVERSION ELEMENT: "pip install certusrodo" → developer action
```


# ═══════════════════════════════════════════════════════════════════════════════
# 4. CONVERSION FRAMEWORK — EVERY ASSET MUST CONVERT
# ═══════════════════════════════════════════════════════════════════════════════

## The AIDA-C Model (Attention → Interest → Desire → Action → Capture)

Every single piece of content Aria creates follows this:

```
A — ATTENTION (First 1-3 seconds)
    Hook that stops the scroll.
    Rule: If someone wouldn't stop scrolling, KILL the concept.

I — INTEREST (Seconds 3-15)
    Show or tell something they didn't know.
    Rule: New information or unexpected angle. Never generic.

D — DESIRE (Seconds 15-45)
    Make them want this for THEMSELVES.
    Rule: Show the outcome, not the feature.
    "Never miss a customer" not "AI phone answering."

A — ACTION (Last 5-10 seconds)
    Tell them exactly what to do RIGHT NOW.
    Rule: ONE action. Not two. Not three. ONE.
    "Call (727) 334-8156" or "Link in bio" or "Comment DEMO"

C — CAPTURE (After the content)
    Capture the lead even if they don't act immediately.
    Rule: Retarget via comments, DMs, or email capture.
```

## Conversion Elements by Platform

| Platform | Primary CTA | Capture Mechanism |
|----------|-----------|-------------------|
| TikTok | "Comment [WORD] for a free trial" | DM automation or manual reply with link |
| YouTube Shorts | "Link in description" | Description link to landing page |
| LinkedIn | "Link in comments ↓" | First comment = landing page link |
| Instagram Reels | "Link in bio" | Linktree → product-specific page |
| Twitter/X | "Reply for a demo" | DM with Calendly link |

## Hook Library (Rotate These — Track Which Convert)

### AnswrdBy Hooks
- "I made a pirate answer my phone for a week."
- "Watch what happens when a telemarketer calls MY AI."
- "I haven't answered my phone in 30 days. Here's why."
- "Same call. Four different AI personalities. Which do you pick?"
- "My friends don't know my phone has an AI now."
- "I have phone anxiety. So I built this."
- "What if your voicemail could actually have a conversation?"
- "This AI answered 47 calls for me this week."

### InSync B2B Hooks
- "I called 50 businesses. 35 went to voicemail."
- "This barbershop was losing $5,000/month to voicemail."
- "Watch an AI handle a real business call in 30 seconds."
- "Your receptionist costs $3,000/month. This costs $149."
- "Every missed call is a customer calling your competitor."

### CertusOrdo Hooks
- "$130 million invested in AI agent security. Zero in rollback."
- "What happens when your AI agent makes a mistake?"
- "This one API call can undo any AI agent action."

## Conversion Tracking (Aria Monitors Weekly)

| Metric | Target | How to Track |
|--------|--------|-------------|
| Hook-to-view rate | >70% (3-second retention) | TikTok/YouTube analytics |
| View-to-engage rate | >5% (likes, comments, shares) | Platform analytics |
| Engage-to-click rate | >2% of viewers click CTA | Link tracking (Bitly or UTM) |
| Click-to-signup rate | >10% of clickers sign up | Stripe + Google Analytics |
| Cost per acquisition | <$15 (organic), <$30 (paid) | Total content cost / signups |

## Content Kill Rule
If a content FORMAT gets <50% of target metrics after 5 posts → KILL IT.
Double down on formats exceeding targets.
Aria tracks this automatically and recommends pivots in the weekly report.


# ═══════════════════════════════════════════════════════════════════════════════
# 5. A/B TESTING & ADAPTIVE OPTIMIZATION
# ═══════════════════════════════════════════════════════════════════════════════

## What Aria Tests (Continuously)

### Visual Tests
- Character render style A vs B (photorealistic vs stylized)
- Color palette variations (warm vs cool, dark vs light)
- Thumbnail with face vs without face
- Text overlay placement (top vs bottom vs center)
- Persona in full scene vs portrait-only

### Copy Tests
- Hook A vs Hook B (same video, different opening line)
- Short CTA vs detailed CTA
- Question-ending vs statement-ending
- Emoji in copy vs no emoji
- First person ("I built") vs third person ("We built")

### Format Tests
- Static image vs short video vs animated
- 15s vs 30s vs 60s video length
- Screen recording vs animated render vs talking head
- Single persona vs comparison format
- Tutorial style vs storytelling vs pure demo

## How Aria Runs Tests

```
1. HYPOTHESIS: "[Change] will increase [metric] by [amount]"
2. CREATE: Two versions of content (A and B)
3. PUBLISH: Same time slot, same day of week, 1 week apart
4. MEASURE: Compare metrics after 7 days (equal exposure time)
5. DECIDE: Winner becomes the new default
6. LOG: Results in Google Sheets "A/B Test Log"
7. REPORT: Include top findings in weekly report to Ian
```

## Adaptive Strategy (Aria's Real Intelligence)

Aria doesn't just follow the calendar. She ADAPTS based on what's working:

| Signal | Aria's Response |
|--------|----------------|
| Hook gets 2x avg views | Create 3 variants of that hook this week |
| Persona Flint outperforms others 3:1 | Feature Flint in 60% of AnswrdBy content |
| LinkedIn text outperforms video | Shift to 4 text posts + 1 video (from 3+2) |
| TikTok comment "how do I get this" | Immediately reply with link + DM follow-up |
| Competitor posts similar content | Differentiate — go harder on live demos (they can't fake that) |
| Call demo videos get 10x engagement | Make call demos 70% of content (not 40%) |
| ROI calculator posts get saves | Create calculator for every vertical, post weekly |
| Weekday morning posts outperform evening | Shift ALL posting to 8-10 AM window |

**The goal is a self-improving content machine.** Every week,
Aria's content is better than the last because she learns from data.


# ═══════════════════════════════════════════════════════════════════════════════
# 6. PLATFORM-SPECIFIC PRODUCTION SPECS
# ═══════════════════════════════════════════════════════════════════════════════

## TikTok / YouTube Shorts / Instagram Reels
- Aspect ratio: 9:16 (1080×1920)
- Length: 15-60 seconds (30-45 sweet spot)
- Captions: MANDATORY (85% watch without sound)
- First frame: Must be compelling as a thumbnail
- Text: Large, bold, high-contrast, centered
- Music: Trending audio when relevant (check TikTok trends weekly)
- Export: MP4, H.264, 30fps minimum

## LinkedIn
- Video: 1:1 (1080×1080) or 16:9 (1920×1080)
- Image: 1200×1200 (square) or 1200×628 (landscape)
- Text post: 1,300 character sweet spot, generous line breaks
- Carousel: 1080×1350 (portrait), 8-12 slides
- PDF carousel: Same dims, export as PDF for native embedding

## YouTube (Long-form, Future)
- Aspect ratio: 16:9 (1920×1080 minimum, 4K preferred)
- Thumbnail: 1280×720, high-contrast, face + text + emotion
- Length: 8-15 minutes for algorithm preference
- Chapters: Add timestamps for retention

## Website / Landing Pages
- Hero images: 1920×1080 minimum, 4K for retina
- Product shots: PNG with transparency for flexible placement
- Persona renders: Multiple angles and expressions for variety
- All images: WebP format for fast loading + PNG for quality


# ═══════════════════════════════════════════════════════════════════════════════
# 7. ARIA'S CREATIVE WORKFLOW (Division 16)
# ═══════════════════════════════════════════════════════════════════════════════

## Daily Creative Production Schedule

```
7:00 AM ─── REVIEW YESTERDAY'S PERFORMANCE
             Pull metrics from all platforms
             Identify top/bottom performers
             Update Google Sheets "Content Performance"

7:30 AM ─── GENERATE TODAY'S ASSETS
             Nano Banana: Generate images/thumbnails for today's content
             Voice: Generate any needed voiceovers
             Video: Queue video renders for today's posts

8:00 AM ─── WRITE & ASSEMBLE
             Write post copy, captions, descriptions
             Match copy to generated assets
             Assemble final content package

8:30 AM ─── SUBMIT FOR APPROVAL
             WhatsApp to Ian: "Today's content ready for review"
             Include: Final image/video + copy + CTA + rationale
             If Ian is unavailable and content is within brand guidelines:
               Aria can publish pre-approved content formats autonomously

9:00-10:00 AM ── PUBLISH WINDOW
             Post approved content to scheduled platforms
             First comment with link (LinkedIn)
             Engage with any immediate comments

THROUGHOUT DAY ── ENGAGEMENT MONITORING
             Respond to comments within 1 hour (draft replies, Ian posts)
             DM follow-up on high-intent comments
             Track real-time metrics on new posts

5:00 PM ─── PREP TOMORROW
             Review trending content/sounds on TikTok
             Identify tomorrow's content topic from calendar
             Pre-draft tomorrow's script
             Queue Nano Banana generation prompts
```

## Creative Asset Library (Build Over Time)

Aria maintains an organized asset library in Google Drive or local storage:

```
/creative-assets/
├── /brand/
│   ├── aria-character/          ← Locked Aria renders (10+ angles)
│   ├── insync-brand/            ← Logo, color palettes, backgrounds
│   └── templates/               ← Reusable post/video templates
├── /answrdby/
│   ├── captain-flint/           ← All Flint renders, poses, scenes
│   ├── chase-sterling/          ← All Chase renders
│   ├── dr-marcus-webb/          ← All Marcus renders
│   ├── reginald/                ← All Reginald renders
│   └── persona-comparison/      ← Side-by-side assets
├── /insync-b2b/
│   ├── call-demos/              ← Screen recordings of AI calls
│   ├── roi-graphics/            ← Calculator animations, stat cards
│   └── client-results/          ← Testimonial graphics, case studies
├── /certusrodo/
│   ├── tech-visuals/            ← Architecture diagrams, API demos
│   └── competitive/             ← Comparison graphics
└── /performance/
    ├── top-performers/          ← Best-performing content for reference
    └── killed-formats/          ← What didn't work (learn from it)
```

## Approval Tiers (Speed vs Control)

| Content Type | Approval Required? | Why |
|-------------|-------------------|-----|
| Scheduled post matching approved template | NO — publish autonomously | Pre-approved format + copy structure |
| New hook or creative angle | YES — WhatsApp Ian first | Untested messaging, brand risk |
| Persona render (new pose/scene) | NO — publish autonomously | Locked identity token = consistent |
| Live call recording | YES — Ian records + approves | Real client/prospect data involved |
| Competitive mention | YES — always | Brand risk |
| Telecom-related content | YES — always | Strategic sensitivity |
| Paid ad creative | YES — always | Money at stake |

As trust builds over time, more formats move from "YES" to "NO" approval.


# ═══════════════════════════════════════════════════════════════════════════════
# 8. PROMPT LIBRARY (Nano Banana + Video Generation)
# ═══════════════════════════════════════════════════════════════════════════════

## Nano Banana Image Prompts

### Social Media Thumbnails
```
"Clean modern tech thumbnail, dark navy background (#1a1a2e),
bold white text '[HEADLINE]', electric blue accent glow,
subtle AI circuit pattern, professional SaaS aesthetic,
1200x1200px square format. Sharp, high-contrast, scroll-stopping."
```

### ROI Stat Cards
```
"Minimalist financial stat card, dark background, large bold
number '$[X],XXX' in white with electric blue glow, smaller
subtitle text '[context]', clean sans-serif typography,
subtle grid pattern, premium data visualization aesthetic."
```

### Scene Backgrounds for Video
```
"Cinematic [environment] scene, volumetric lighting, shallow
depth of field, film grain, warm color temperature, 16:9 aspect
ratio, photorealistic, suitable as background for text overlay,
[specific details]."
```

### Product Mockup
```
"Premium smartphone mockup showing [app screen/website],
floating at slight angle, dark gradient background with
subtle reflection, soft studio lighting, photorealistic,
clean and modern, [specific screen content]."
```

## Video Generation Prompts

### Character Animation (Image-to-Video)
```
"Slow cinematic camera movement, slight head turn, subtle
natural breathing motion, warm atmospheric lighting shifts,
shallow depth of field with soft bokeh, 5 seconds, smooth
and natural, photorealistic quality."
```

### Product Demo Scene
```
"Smooth camera dolly forward toward smartphone screen,
phone rings with subtle glow effect, UI elements animate
naturally, clean modern environment, warm lighting,
10 seconds, 1080p, cinematic quality."
```

### Before/After Transition
```
"Split screen wipe transition, left side dim/cold lighting
(voicemail), right side warm/vibrant lighting (AI answers),
smooth horizontal wipe at 3-second mark, both sides
photorealistic office/business environment."
```

## Voice Generation Prompts

### Aria Brand Narration
```
Voice: sqskhHdmEWFUgFIrJEuI
Stability: 0.5
Similarity: 0.75
Speed: 1.1 (slightly slower than conversational for narration)
Style: Confident, warm, knowledgeable
```

### Persona Demo Voices
```
Captain Flint: Deep, warm, playful authority, subtle pirate charm
Chase Sterling: Low, calm, authoritative, minimal words
Dr. Marcus Webb: Warm, measured, reassuring, unhurried
Reginald: Refined British, formal yet welcoming, supremely capable
```


# ═══════════════════════════════════════════════════════════════════════════════
# 9. CONVERSION OPTIMIZATION RULES
# ═══════════════════════════════════════════════════════════════════════════════

## The 10 Laws of Content That Converts

1. **SHOW, NEVER DESCRIBE.**
   A 30-second call recording beats 500 words about how good the AI is.

2. **LEAD WITH THE OUTCOME, NOT THE FEATURE.**
   "Never miss a customer" beats "AI phone answering technology."

3. **USE REAL NUMBERS, NOT ADJECTIVES.**
   "$5,280/month in missed revenue" beats "a lot of missed calls."

4. **ONE CTA PER PIECE.**
   "Call (727) 334-8156" — that's it. Not "call and visit and subscribe and share."

5. **THE FIRST 2 SECONDS DECIDE EVERYTHING.**
   If the hook doesn't stop the scroll, nothing else matters.

6. **UGLY AUTHENTIC BEATS POLISHED GENERIC.**
   A real screen recording of Mel answering a barbershop call beats
   a perfect AI-generated commercial. Use both, but never sacrifice
   authenticity for polish.

7. **EVERY PIECE MUST ANSWER: "WHY SHOULD I CARE RIGHT NOW?"**
   Urgency comes from specificity. "You're losing $X today" not "you could save money."

8. **REPURPOSE EVERYTHING.**
   One call recording = LinkedIn post + TikTok video + email content +
   case study data point + sales deck slide + website testimonial.

9. **KILL WHAT DOESN'T WORK. FAST.**
   5 posts of a format with below-target metrics = dead format. Move on.

10. **THE ALGORITHM REWARDS CONSISTENCY.**
    Posting 5 mediocre pieces/week beats 1 masterpiece/month.
    Volume × quality × consistency = growth.


# ═══════════════════════════════════════════════════════════════════════════════
# 10. MILESTONE TRIGGERS (Add to Milestone Engine)
# ═══════════════════════════════════════════════════════════════════════════════

| Trigger | Aria's Action |
|---------|--------------|
| New persona build complete | Generate 10+ Nano Banana renders, lock identity token, create intro video |
| TikTok video hits 10K views | Create 3 variants of that format within 48 hours |
| TikTok video hits 100K views | Allocate 50% of next week's content to that format |
| LinkedIn post gets 50+ comments | Reply to every comment with value (draft for Ian) |
| Content converts at 2x avg rate | Promote to "evergreen" — repost monthly with variations |
| Content format fails 5 times | Kill format, document why, never repeat |
| AnswrdBy hits 100 subscribers | Generate "100 phones answered by AI" celebration content |
| First carrier meeting booked | Generate carrier-specific pitch video assets |
| Competitor launches similar product | Accelerate content output to 2x for 2 weeks |
| New ElevenLabs model released | Test immediately, update production pipeline if better |
| Nano Banana releases update | Test identity consistency, update prompts if needed |

---

## How This Connects to Revenue

```
Content → Attention → Interest → Demo/Signup → Revenue

Weekly targets:
- 5+ content pieces published
- 500+ total views (growing 20% MoM)
- 2+ demo calls from content
- 1+ signup from content
- $500+ revenue attributable to content

Monthly targets:
- 20+ content pieces
- 5,000+ total views
- 8+ demo calls
- 4+ signups
- $2,000+ content-attributed revenue

When content-attributed revenue exceeds $5K/month:
→ Consider paid amplification (boost top-performing organic posts)
→ Allocate 10% of content-attributed revenue to paid distribution
```


# ═══════════════════════════════════════════════════════════════════════════════
# SUMMARY: WHAT THIS ADDS TO ARIA'S OPERATING SYSTEM
# ═══════════════════════════════════════════════════════════════════════════════
#
# NEW DIVISION 16: Creative Production
# - Full production pipeline from concept to published content
# - Nano Banana Pro for studio-quality character renders and graphics
# - ElevenLabs ecosystem for video, voice, lip-sync, and assembly
# - Character bible for every persona and brand element
# - Conversion framework (AIDA-C) for every piece of content
# - A/B testing engine with automatic optimization
# - Platform-specific production specs
# - Prompt library for consistent quality
# - 10 Laws of Content That Converts
# - Adaptive strategy that improves every week based on data
#
# Aria doesn't just post content. She PRODUCES content.
# Studio-quality visuals. Conversion-optimized copy.
# Data-driven iteration. Every week better than the last.
#
# "Beautiful content that doesn't convert is a hobby.
#  Content that converts at scale is a billion-dollar company."
#
# ═══════════════════════════════════════════════════════════════════════════════
# END OF CREATIVE PRODUCTION ENGINE
# ═══════════════════════════════════════════════════════════════════════════════
