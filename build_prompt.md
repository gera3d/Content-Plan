# Optimized Prompt for Building gera.yerem.in

Copy everything below to start the build:

---

## PROJECT PROMPT

### Context

I'm Gera Yeremin, a software developer and digital marketer. I need you to build my personal content publishing platform at **gera.yerem.in**.

This is NOT a rebuild of my old WordPress site. This is a fresh start with modern, fast infrastructure. The old content will be migrated later.

### What Already Exists

In my `/Users/gerayeremin/Documents/Projects/Content Plan` directory:

**Working Code:**
- `dashboard.py` - 3,398-line Streamlit dashboard with keyword research, content strategy
- `content_manager.py` - Content creation, storage, metadata management
- `content_adapter.py` - Platform-specific content formatters (Medium, LinkedIn, Twitter, etc.)

**Reference Documents (READ THESE FIRST):**
- `brand-profile.md` - Who I am, what I sell, my voice
- `writing-voice-guide.md` - How I write (CRITICAL for all copy)
- `custom-business-software-guide.md` - My main pillar content (40KB)

**Planning Artifacts in `.gemini/antigravity/brain/[session-id]/`:**
- `master_plan.md` - Full project roadmap
- `homepage_design.md` - Homepage layout and copy
- `content_management_strategy.md` - How content is managed

### What I Need Built

**1. gera.yerem.in Website**

Stack:
- **Astro** - Static site generator (fast, 100 Lighthouse score)
- **Turso** - Distributed SQLite for content storage (scales without slowing)
- **Vercel or Cloudflare** - Hosting
- **MDX** - For content (Markdown + components)

URL Structure:
```
gera.yerem.in/                          ← Homepage
gera.yerem.in/post-slug                 ← Individual posts
gera.yerem.in/topic/software-development ← Topic archives
gera.yerem.in/about
gera.yerem.in/work
gera.yerem.in/contact
```

**2. Homepage (See homepage_design.md)**

Sections:
1. Hero - "I build custom software for businesses that have outgrown spreadsheets"
2. What I Build - Custom apps, review tools, workflow automation
3. Who I Work With - $500K-$5M businesses, $15K-$150K projects
4. Featured Writing - Pillar content + recent posts
5. About - Human, personal touch
6. Simple CTA - Low-pressure "Let's talk"

Design:
- Clean, minimal, fast
- Black text, white background, one accent color
- My photo
- Lots of whitespace
- NO: stock photos, sliders, animations, corporate jargon

**3. Content Publishing Integration**

Connect `content_manager.py` to the new site so I can:
- Create content in dashboard
- Publish to gera.yerem.in (creates MDX file, deploys)
- Get canonical URL back
- Then syndicate to other platforms

### Technical Requirements

**Performance:**
- 100 Lighthouse score
- < 1 second load time
- No unnecessary JavaScript
- Optimized images (WebP, lazy loading)

**SEO:**
- Schema markup (Article, Person, Organization)
- Open Graph tags
- Twitter cards
- Sitemap.xml
- RSS feed
- Canonical URLs on every page

**Content:**
- MDX support
- Code syntax highlighting
- Reading time estimates
- Table of contents for long posts
- Related posts

### My Voice (CRITICAL)

Read `writing-voice-guide.md` before writing ANY copy.

Key rules:
- Direct, conversational, no BS
- "Professional without being corporate"
- Like talking to a business owner at a coffee shop
- Use contractions (I'm, you're, it's)
- Short paragraphs, punchy sentences
- Ask questions to engage: "Sound familiar?"

**DO:**
- "I build custom software for businesses that have outgrown spreadsheets."
- "Let's talk about what you're trying to solve."
- "I'll tell you if we're not a good fit."

**DON'T:**
- "Leverage cutting-edge solutions to maximize ROI"
- "We cordially invite you to schedule a consultation"
- "Best-in-class enterprise software development"

### Acceptance Criteria

**Done when:**
- [ ] gera.yerem.in loads in < 1 second
- [ ] Lighthouse score is 100 across all metrics
- [ ] Homepage matches the design in homepage_design.md
- [ ] Pillar post is live at gera.yerem.in/custom-business-software-guide
- [ ] Topic pages work: gera.yerem.in/topic/software-development
- [ ] RSS feed works
- [ ] Sitemap generated
- [ ] Schema markup validates
- [ ] All copy sounds like me (check against writing-voice-guide.md)
- [ ] Dashboard can publish new content to the site
- [ ] Mobile responsive
- [ ] Dark mode (optional but nice)

### Files to Read First

1. `writing-voice-guide.md` - How to write in my voice
2. `brand-profile.md` - Who I am
3. `homepage_design.md` - Homepage layout
4. `master_plan.md` - Full project context
5. `custom-business-software-guide.md` - Pillar content to publish

### Sequence

1. Set up Astro project with Turso
2. Build homepage (hero, sections, footer)
3. Build blog/post template
4. Build topic archive pages
5. Publish pillar post
6. Connect to content_manager.py
7. Deploy to Vercel/Cloudflare
8. Configure gera.yerem.in domain
9. Test everything

### Constraints

- No WordPress
- No React (Astro is fine, minimal JS)
- No Tailwind unless I ask for it
- No dark patterns or pop-ups
- No "solutions" or "leverage" or corporate words
- No stock photos
- Keep it simple

### When Stuck

- Check writing-voice-guide.md for copy questions
- Check brand-profile.md for positioning questions
- Check homepage_design.md for layout questions
- Ask me if something is unclear

---

**Start by reading the reference documents, then build the Astro site structure. Show me the homepage first before building everything else.**
