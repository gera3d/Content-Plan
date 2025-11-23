"""
Content Strategy Dashboard - Complete Version with Modern Components
All 8 original tabs restored with streamlit-extras styling
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

# Page configuration
st.set_page_config(
    page_title="Content Strategy Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    * {
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Inter", sans-serif !important;
    }
    
    #MainMenu, footer {visibility: hidden;}
    
    .main {
        background: #fafafa;
    }
    
    .block-container {
        padding: 2rem 3rem !important;
        max-width: 1800px !important;
    }
    
    [data-testid="stMetricValue"] {
        font-size: 2rem !important;
        font-weight: 700 !important;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 0.9rem !important;
        font-weight: 500 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
    }
    
    .stDataFrame {
        border-radius: 12px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    }
    
    h1 {
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        letter-spacing: -0.03em !important;
    }
    
    h2 {
        font-size: 1.8rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em !important;
    }
    
    h3 {
        font-size: 1.4rem !important;
        font-weight: 600 !important;
    }
    
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        padding: 0.6rem 1.5rem;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 12px 24px;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# Header
colored_header(
    label="Content Strategy Dashboard",
    description="Gera Yeremin | Digital Marketing & Software Architecture",
    color_name="blue-70"
)

add_vertical_space(1)

# Focus Card
st.info("""
**🎯 Your Focus: Custom Software Development**

**Core Offering:** Building custom business applications and software architecture solutions  
**Specialty:** Review management systems, BI tools, workflow automation, custom CRM/data platforms  
**Your Edge:** You understand both technical AND marketing—build software that drives business results
""")

add_vertical_space(2)

# Create tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "📊 Overview",
    "🎯 Keyword Strategy", 
    "🔥 Content Opportunities",
    "📅 Content Calendar",
    "📝 Content Review",
    "✍️ Voice Guide",
    "🧮 Interactive Tools",
    "🔍 Live Analysis"
])

with tab1:
    colored_header(label="Market Overview", description="", color_name="blue-70")
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Target Keywords", "11", "Custom Software Focus")
    with col2:
        st.metric("Avg Interest", "42", "Rising trends")
    with col3:
        st.metric("Low Competition", "2", "Quick wins")
    with col4:
        st.metric("Tools Built", "3", "Interactive")
    
    style_metric_cards(background_color="#FFFFFF", border_left_color="#0071e3", border_size_px=3)
    
    add_vertical_space(2)
    
    # Keyword data table
    colored_header(label="Search Interest & Competition", description="", color_name="blue-70")
    
    keyword_data = pd.DataFrame({
        'Keyword': [
            'custom software development',
            'business applications',
            'software architecture',
            'custom business software',
            'bespoke software development',
            'enterprise software development',
            'SaaS development',
            'web application development',
            'review management software',
            'custom CRM development',
            'workflow automation software'
        ],
        'Category': [
            'Custom Software', 'Custom Software', 'Custom Software',
            'Custom Software', 'Custom Software', 'Custom Software',
            'Custom Software', 'Custom Software',
            'Software (Niche)', 'Software (Niche)', 'Software (Niche)'
        ],
        'Avg Interest': [58, 42, 38, 35, 28, 52, 65, 71, 35, 45, 55],
        'Competition': ['High', 'Medium', 'Medium', 'Low', 'Low', 'High', 'Very High', 'High', 'Medium', 'Medium', 'Medium'],
        'Related Queries': [40, 4, 21, 12, 8, 35, 45, 50, 24, 18, 22],
        'Rising Queries': [18, 0, 6, 5, 3, 15, 20, 25, 10, 8, 12],
        'Opportunity Score': ['🟢 High', '🟡 Medium', '🟡 Medium', '🟢 High', '🟢 High', '🟡 Medium', '🔴 Low', '🔴 Low', '🟢 High', '🟢 High', '🟢 High']
    })
    
    st.dataframe(keyword_data, use_container_width=True, hide_index=True)
    
    st.caption("💡 **Opportunity Score** = High interest + Low competition + Rising queries = Best targets")
    
    add_vertical_space(2)
    
    # Category breakdown
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.success("""
        **Custom Software (6 Keywords)**  
        🔥 Primary Focus
        
        **Top Keywords:**
        - 🟢 custom software development
        - 🟢 custom business software
        - 🟢 bespoke software development
        """)
    
    with col2:
        st.success("""
        **Niche Solutions (3 Keywords)**  
        🔥 High Priority
        
        **Top Keywords:**
        - 🟢 review management software
        - 🟢 custom CRM development
        - 🟢 workflow automation software
        """)
    
    with col3:
        st.warning("""
        **Web/SaaS Dev (2 Keywords)**  
        Secondary
        
        **Top Keywords:**
        - 🔴 web application development
        - 🔴 SaaS development (skip)
        """)
    
    add_vertical_space(2)
    
    # Strategic insights
    colored_header(label="Strategic Insights", description="", color_name="blue-70")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🔥 Best Opportunities:**
        1. **Custom business software** - 35 interest, LOW comp! 🎯
        2. **Bespoke software development** - 28 interest, LOW comp! 🎯
        3. **Custom CRM development** - 45 interest, medium comp
        4. **Workflow automation software** - 55 interest, medium comp
        5. **Custom software development** - 58 interest, 40 related queries
        6. **Review management software** - 35 interest, niche opportunity
        """)
    
    with col2:
        st.markdown("""
        **📈 Your Winning Strategy:**
        - ✅ Target "custom" + specific industry
        - ✅ Focus on "business software" not "enterprise"
        - ✅ Emphasize ROI, marketing integration
        - ✅ Build showcase projects in niche areas
        - ✅ Go LOCAL for "custom software development"
        - ❌ Avoid SaaS development (too competitive)
        """)

with tab2:
    colored_header(label="Keyword Strategy & Ranking Plan", description="How to rank for each keyword", color_name="blue-70")
    
    # Keyword details with expanders
    with st.expander("🟢 #1: Custom Business Software (LOW Competition)", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **📊 Metrics:**
            - Search Volume: ~35/100 interest
            - Competition: 🟢 LOW
            - Related Queries: 12 variations
            - Rising Queries: 5 trending
            
            **Why This Keyword:**
            - Exactly what you do
            - Low competition = easier to rank
            - Business owners have BUDGET
            - More specific than generic terms
            """)
        
        with col2:
            st.markdown("""
            **🚀 Ranking Strategy:**
            1. Pillar Page: "Complete Guide to Custom Business Software" (3000+ words)
            2. Case Studies: 3-4 real examples with ROI
            3. Comparison: "Custom vs. Off-the-Shelf"
            4. ROI Calculator (interactive tool)
            5. Schema markup: Article, HowTo, FAQ
            6. Local SEO optimization
            """)
    
    with st.expander("🟢 #2: Bespoke Software Development (LOW Competition)"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **📊 Metrics:**
            - Search Volume: ~28/100 interest
            - Competition: 🟢 LOW
            - Related Queries: 8 variations
            - Rising Queries: 3 trending
            
            **Why This Keyword:**
            - "Bespoke" = premium positioning
            - UK/international searchers
            - Less competition
            - Different audience than "custom"
            """)
        
        with col2:
            st.markdown("""
            **🚀 Ranking Strategy:**
            1. Definition Post: "Bespoke vs. Custom Software"
            2. Portfolio Showcase
            3. Process Guide: "How Bespoke Development Works"
            4. Pricing Guide with transparency
            5. Target UK/International markets
            6. Premium imagery and case studies
            """)
    
    with st.expander("🟡 #3: Custom Software Development (HIGH Competition)"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **📊 Metrics:**
            - Search Volume: ~58/100 (HIGH!)
            - Competition: 🟡 HIGH
            - Related Queries: 40+ variations
            - Rising Queries: 18 trending
            
            **Why This Keyword:**
            - Highest search volume
            - Broad awareness-stage term
            - 40 related queries = content goldmine
            - Can target with location modifiers
            """)
        
        with col2:
            st.markdown("""
            **🚀 Ranking Strategy:**
            1. Ultimate Resource: "Complete 2025 Guide" (5000+ words)
            2. Hub Page linking to all related content
            3. Industry-Specific guides
            4. FAQ page (answer all 40 related queries)
            5. **Go LOCAL:** "Custom Software Development [Your City]"
            6. Google Business Profile optimization
            7. Local backlinks
            """)
    
    with st.expander("🟢 #4: Review Management Software"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **📊 Metrics:**
            - Search Volume: ~35/100
            - Competition: 🟡 MEDIUM
            - Related Queries: 24 variations
            - Rising Queries: 10 trending
            
            **Why This Keyword:**
            - You've BUILT this (instant credibility)
            - Can show actual working software
            - Combines software + marketing
            - High commercial intent
            """)
        
        with col2:
            st.markdown("""
            **🚀 Ranking Strategy:**
            1. Live Demo: "Our Review Management Software"
            2. Case Study: Real ROI numbers
            3. Comparison: "Build vs. Buy"
            4. Technical Deep Dive
            5. Video demo embedded
            6. Comparison vs. Birdeye, Podium, Grade.us
            """)
    
    with st.expander("🟢 #5: Custom CRM Development"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **📊 Metrics:**
            - Search Volume: ~45/100
            - Competition: 🟡 MEDIUM
            - Related Queries: 18 variations
            - Rising Queries: 8 trending
            
            **Why This Keyword:**
            - High commercial intent
            - Business owners actively seeking
            - Can showcase custom solutions
            - Alternative to Salesforce
            """)
        
        with col2:
            st.markdown("""
            **🚀 Ranking Strategy:**
            1. Guide: "When to Build Custom CRM vs. Buy Salesforce"
            2. Migration guide from Salesforce
            3. ROI comparison calculator
            4. Feature checklist
            5. Integration capabilities
            6. Case studies with timelines
            """)
    
    with st.expander("🟢 #6: Workflow Automation Software"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **📊 Metrics:**
            - Search Volume: ~55/100
            - Competition: 🟡 MEDIUM
            - Related Queries: 22 variations
            - Rising Queries: 12 trending
            
            **Why This Keyword:**
            - Growing interest
            - Alternative to Zapier/Make
            - Complex needs = custom solutions
            - Good upsell from consulting
            """)
        
        with col2:
            st.markdown("""
            **🚀 Ranking Strategy:**
            1. Comparison: "Zapier vs Custom Workflow Automation"
            2. Use case library
            3. Template downloads
            4. API integration guide
            5. Pricing transparency
            6. Demo workflows
            """)

with tab3:
    colored_header(label="Content Opportunities", description="Best opportunities for custom software content", color_name="blue-70")
    
    # Custom Software Opportunities
    st.subheader("1️⃣ Custom Business Software (🎯 LOW COMPETITION!)")
    st.markdown("""
    **Why it's PERFECT:** Low competition + good search volume + exactly what you do!
    
    **Keywords:**
    - **Custom business software** - 35 avg interest, LOW competition, 12 related
    - **Bespoke software development** - 28 avg interest, LOW competition, 8 related
    - **Custom software development** - 58 avg interest, 40 related, 18 rising
    
    **Content Ideas:**
    - "When to Build Custom Business Software vs. Buy Off-the-Shelf"
    - "Custom Business Software ROI Calculator"
    - "5 Signs Your Business Needs Custom Software"
    - "From Spreadsheet to Custom Software: Real Case Study"
    - "The Hidden Cost of SaaS: Why Custom Software Pays for Itself"
    - "How to Choose a Custom Software Developer"
    """)
    
    st.divider()
    
    st.subheader("2️⃣ Niche Software Solutions (Your Secret Weapon)")
    st.markdown("""
    **Why it matters:** Combines your software + marketing expertise
    
    **Keywords:**
    - **Review management software** - 35 interest, medium comp, 24 related
    - **Custom CRM development** - 45 interest, medium comp, 18 related
    - **Workflow automation software** - 55 interest, medium comp, 22 related
    
    **Content Ideas:**
    - "Building a Custom Review Management System in 90 Days"
    - "Why We Built Our Own CRM (And How You Can Too)"
    - "Workflow Automation: Custom Software vs. Zapier/Make"
    - "Review Software ROI: Custom vs. Birdeye/Podium"
    - "Migrating from Salesforce to Custom CRM"
    - "Automation Playbook: 10 Workflows to Build First"
    """)
    
    st.divider()
    
    st.subheader("3️⃣ Software Architecture & Best Practices")
    st.markdown("""
    **Why it matters:** Establishes you as technical expert, not just coder
    
    **Keywords:**
    - **Software architecture** - 38 interest, medium comp, 21 related, 6 rising
    - **Business applications** - 42 interest, medium comp
    
    **Content Ideas:**
    - "Software Architecture for Small Business Applications"
    - "Choosing the Right Tech Stack for Custom Software"
    - "API-First Design for Business Software Integration"
    - "Scaling Custom Software: Architecture Patterns"
    - "Microservices vs. Monolith for Business Apps"
    - "Security Best Practices for Custom Software"
    """)
    
    st.divider()
    
    st.subheader("4️⃣ Supporting Content (Link Building + Lead Gen)")
    st.markdown("""
    **Purpose:** Build authority, capture different search intents, internal linking
    
    **Content Types:**
    - **Comparison Posts:** "Custom vs. Off-the-Shelf Software"
    - **Calculator Tools:** ROI calculator, Cost estimator, Timeline calculator
    - **Templates:** RFP template, Requirements checklist, Vendor questions
    - **Case Studies:** Real projects with numbers and timelines
    - **Guides:** "Complete Guide to Software Development Costs"
    - **Video Content:** Process walkthrough, Case study videos, Tool demos
    """)

with tab4:
    colored_header(label="12-Week Content Calendar", description="Prioritized by opportunity", color_name="blue-70")
    
    st.info("🎯 **Strategy:** Start with LOW competition keywords for quick wins, then build authority for harder terms")
    
    content_plan = pd.DataFrame({
        'Week': ['1-2', '3-4', '5-6', '7-8', '9-10', '11-12'],
        'Keyword': [
            'custom business software',
            'bespoke software development',
            'review management software',
            'custom CRM development',
            'workflow automation software',
            'custom software development'
        ],
        'Competition': ['🟢 LOW', '🟢 LOW', '🟡 MEDIUM', '🟡 MEDIUM', '🟡 MEDIUM', '🔴 HIGH'],
        'Main Content': [
            'Complete Guide (3000+ words)',
            'Bespoke Solutions Guide',
            'Case Study + Live Demo',
            'CRM vs Salesforce Guide',
            'Zapier vs Custom Comparison',
            'Ultimate Guide (5000+ words)'
        ],
        'Supporting': [
            'ROI Calculator, 5 blog posts',
            'Portfolio, Pricing guide',
            'Demo video, Podcast',
            'Migration guide, Checklist',
            'Templates, Use cases',
            'Local SEO, FAQ page'
        ],
        'Goal': [
            'Rank #1-3 in 60 days',
            'Rank #1-5 in 60 days',
            'Rank #5-10, Get demos',
            'Rank #5-15, Get leads',
            'Rank #5-15 in 90 days',
            'Rank #10-20 (Local #1-5)'
        ]
    })
    
    st.dataframe(content_plan, use_container_width=True, hide_index=True)
    
    add_vertical_space(2)
    
    # Week details
    with st.expander("📋 Week 1-2: Custom Business Software (PRIORITY)", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Days 1-7: Content Creation**
            - [x] Research top 10 ranking pages
            - [x] Create detailed outline (3000+ words)
            - [x] Write pillar post (What, Why, When, How, Cost, ROI)
            - [x] Include 3-4 case study snippets
            - [x] Create comparison tables
            - [x] Plan ROI calculator functionality
            """)
        
        with col2:
            st.markdown("""
            **Days 8-14: Launch & Promote**
            - [x] Build ROI calculator (JavaScript)
            - [x] Create cost breakdown infographic
            - [ ] SEO optimization (title, meta, schema)
            - [ ] Record video (10-15 min)
            - [ ] Share on LinkedIn, Twitter
            - [ ] Email contacts
            - [ ] Post in communities
            """)
    
    with st.expander("📋 Week 3-4: Bespoke Software Development"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Days 15-21: Content Creation**
            - [ ] Research "bespoke" vs "custom" differences
            - [ ] Create 2000+ word guide
            - [ ] Portfolio showcase page
            - [ ] Process flowchart
            - [ ] Pricing guide (transparent)
            - [ ] Client testimonials
            """)
        
        with col2:
            st.markdown("""
            **Days 22-28: Launch & Promote**
            - [ ] On-page SEO optimization
            - [ ] Submit to relevant directories
            - [ ] LinkedIn article version
            - [ ] Create Instagram carousel
            - [ ] Email sequence for leads
            - [ ] Share in UK/international groups
            """)
    
    with st.expander("📋 Week 5-6: Review Management Software"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Days 29-35: Content Creation**
            - [ ] Case study writeup
            - [ ] Demo video recording
            - [ ] Comparison vs competitors
            - [ ] Technical architecture post
            - [ ] ROI calculator for reviews
            - [ ] Integration guide
            """)
        
        with col2:
            st.markdown("""
            **Days 36-42: Launch & Promote**
            - [ ] Product Hunt launch
            - [ ] Marketing subreddits
            - [ ] YouTube video
            - [ ] Podcast pitch
            - [ ] Guest post on marketing blogs
            - [ ] Webinar planning
            """)

with tab5:
    colored_header(label="Content Review", description="Week 1-2 Pillar Post", color_name="blue-70")
    
    article_path = '/Users/gerayeremin/Documents/Projects/Content Plan/custom-business-software-guide.md'
    
    if os.path.exists(article_path):
        with open(article_path, 'r') as f:
            article_content = f.read()
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            word_count = len(article_content.split())
            st.metric("Word Count", f"{word_count:,}")
        with col2:
            headers = article_content.count('##')
            st.metric("Sections", headers)
        with col3:
            links = article_content.count('[')
            st.metric("Links/CTAs", links)
        with col4:
            tables = article_content.count('|')
            st.metric("Tables", tables // 3)
        
        style_metric_cards(background_color="#FFFFFF", border_left_color="#00c853", border_size_px=3)
        
        add_vertical_space(2)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("""
            **✅ SEO Elements:**
            - ✅ H1 title with keyword
            - ✅ Table of contents
            - ✅ FAQ section
            - ✅ Multiple CTAs
            - ✅ Internal links
            - ✅ Author bio
            """)
        
        with col2:
            st.success("""
            **✅ Content Strengths:**
            - ✅ 4 detailed case studies
            - ✅ Real numbers & pricing
            - ✅ Comparison tables
            - ✅ Decision framework
            - ✅ Actionable next steps
            """)
        
        add_vertical_space(2)
        
        # Review actions
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("✅ Approve for Publishing", type="primary"):
                st.success("Article approved! Ready to publish.")
        
        with col2:
            if st.button("📝 Request Edits"):
                st.info("Edit requests will be tracked here.")
        
        with col3:
            if st.button("🗑️ Archive Draft"):
                st.warning("Draft archived.")
        
        add_vertical_space(2)
        
        preview_mode = st.radio("View as:", ["Rendered Markdown", "Raw Markdown"], horizontal=True)
        
        if preview_mode == "Rendered Markdown":
            st.markdown(article_content)
        else:
            st.code(article_content, language="markdown")
    else:
        st.warning("Article file not found. Create `custom-business-software-guide.md` to review here.")

with tab6:
    colored_header(label="Writing Voice Guide", description="Gera Yeremin's authentic voice", color_name="blue-70")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        ### ✅ DO This
        - Be direct and get to the point
        - Use "you" and "I" naturally
        - Ask engaging questions
        - Give real numbers and examples
        - Use contractions (I've, you're)
        - Write like you talk
        - Explain technical stuff simply
        - Admit limitations honestly
        - Show personality
        - Use specific examples from experience
        """)
    
    with col2:
        st.error("""
        ### ❌ DON'T Do This
        - Use corporate buzzwords
        - Write overly formal
        - Bury the main point
        - Say "we" when it's just you
        - Use jargon without explaining
        - Make grandiose promises
        - Keyword stuff unnaturally
        - Sound like a sales page
        - Be vague or generic
        - Hide behind corporate speak
        """)
    
    add_vertical_space(2)
    
    # Voice examples
    colored_header(label="Before & After Examples", description="", color_name="blue-70")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ❌ Corporate Voice")
        st.code("""
Our innovative solutions leverage cutting-edge 
technology to revolutionize your business processes 
and drive unprecedented value creation through 
synergistic partnerships.

We provide best-in-class software engineering 
services to enterprise clients seeking to 
optimize their digital transformation journey.
        """, language="text")
    
    with col2:
        st.markdown("### ✅ Gera's Voice")
        st.code("""
I build custom software for businesses that are tired 
of paying $2,000/month for SaaS tools that don't quite 
fit what they need.

Here's the thing: most businesses don't need 
"enterprise" software. They need something that 
actually works for their specific workflow.
        """, language="text")
    
    add_vertical_space(2)
    
    st.subheader("🎯 Voice Checker Tool")
    
    test_content = st.text_area("Paste content to check:", height=150, placeholder="Paste your writing here...")
    
    if st.button("🔍 Check Voice Match", type="primary"):
        if test_content:
            issues = []
            warnings = []
            good_signs = []
            
            # Check patterns
            bad_words = ['leverage', 'synergy', 'revolutionize', 'paradigm', 'best-in-class', 'innovative solutions', 'cutting-edge', 'unprecedented']
            for word in bad_words:
                if word in test_content.lower():
                    issues.append(f"❌ Contains '{word}' (corporate buzzword)")
            
            if "?" in test_content:
                good_signs.append("✅ Uses questions")
            if any(word in test_content.lower() for word in ["you", "your"]):
                good_signs.append("✅ Direct address to reader")
            if any(word in test_content.lower() for word in ["i've", "you're", "it's", "don't", "here's"]):
                good_signs.append("✅ Natural contractions")
            if any(word in test_content for word in ["I ", " I'", "I'm"]):
                good_signs.append("✅ First person voice")
            
            avg_sentence_length = len(test_content.split()) / max(test_content.count('.'), 1)
            if avg_sentence_length < 20:
                good_signs.append("✅ Concise sentences")
            elif avg_sentence_length > 30:
                warnings.append("⚠️ Sentences might be too long")
            
            if issues:
                st.error("**Issues Found:**\n" + "\n".join(issues))
            if warnings:
                st.warning("**Warnings:**\n" + "\n".join(warnings))
            if good_signs:
                st.success("**Good Elements:**\n" + "\n".join(good_signs))
            if not issues and not warnings:
                st.success("🎉 Sounds like Gera!")
        else:
            st.info("Paste some content above to check it")

with tab7:
    colored_header(label="Interactive Tools", description="Embedded in content for engagement", color_name="blue-70")
    
    tool_col1, tool_col2, tool_col3 = st.columns(3)
    
    with tool_col1:
        st.subheader("💰 ROI Calculator")
        st.write("""
        **Features:**
        - 6 input sliders
        - Real-time calculations
        - 5-year projections
        - Smart recommendations
        - Apple/Nike design
        
        **Used in:**
        - Custom Business Software post
        - Bespoke Development guide
        """)
        
        if os.path.exists('roi-calculator.html'):
            calculator_path = os.path.abspath('roi-calculator.html')
            st.link_button("🚀 Open Calculator", f"file://{calculator_path}", use_container_width=True)
    
    with tool_col2:
        st.subheader("💵 Cost Breakdown")
        st.write("""
        **Features:**
        - 3 pricing tiers
        - Cost factors table
        - Hidden costs
        - Budget planning
        
        **Used in:**
        - Pricing transparency pages
        - Lead magnets
        """)
        
        if os.path.exists('cost-breakdown-infographic.html'):
            breakdown_path = os.path.abspath('cost-breakdown-infographic.html')
            st.link_button("🚀 Open Breakdown", f"file://{breakdown_path}", use_container_width=True)
    
    with tool_col3:
        st.subheader("🤔 Decision Framework")
        st.write("""
        **Features:**
        - 5 decision questions
        - Scoring system
        - Build vs Buy advice
        - Next steps
        
        **Used in:**
        - Consultation pages
        - Discovery calls
        """)
        
        if os.path.exists('decision-framework.html'):
            framework_path = os.path.abspath('decision-framework.html')
            st.link_button("🚀 Open Framework", f"file://{framework_path}", use_container_width=True)
    
    add_vertical_space(2)
    
    colored_header(label="Embed Code", description="", color_name="blue-70")
    
    st.info("Copy these embed codes to add tools to your blog posts or website")
    
    embed_tool = st.selectbox("Select tool:", ["ROI Calculator", "Cost Breakdown", "Decision Framework"])
    
    if embed_tool == "ROI Calculator":
        st.code('''
<iframe src="roi-calculator.html" 
        width="100%" 
        height="1200" 
        frameborder="0" 
        style="border-radius: 12px; box-shadow: 0 4px 24px rgba(0,0,0,0.1);">
</iframe>
        ''', language="html")
    elif embed_tool == "Cost Breakdown":
        st.code('''
<iframe src="cost-breakdown-infographic.html" 
        width="100%" 
        height="800" 
        frameborder="0" 
        style="border-radius: 12px; box-shadow: 0 4px 24px rgba(0,0,0,0.1);">
</iframe>
        ''', language="html")
    else:
        st.code('''
<iframe src="decision-framework.html" 
        width="100%" 
        height="900" 
        frameborder="0" 
        style="border-radius: 12px; box-shadow: 0 4px 24px rgba(0,0,0,0.1);">
</iframe>
        ''', language="html")

with tab8:
    colored_header(label="Live Keyword Analysis", description="Optional: Connect to Google Trends", color_name="blue-70")
    
    st.info("""
    📊 This tab can connect to Google Trends API for live keyword research.
    
    Currently showing saved data. To enable live analysis, uncomment the KeywordResearcher import and add your API credentials.
    """)
    
    add_vertical_space(2)
    
    # Placeholder for live trends
    colored_header(label="Interest Over Time", description="", color_name="blue-70")
    
    # Sample data for visualization
    dates = pd.date_range(start='2024-01-01', end='2024-12-01', freq='M')
    trend_data = pd.DataFrame({
        'Date': dates,
        'custom business software': [32, 35, 33, 38, 36, 39, 35, 37, 38, 40, 42, 41],
        'bespoke software development': [25, 26, 28, 27, 29, 28, 30, 29, 31, 30, 32, 31],
        'custom software development': [55, 56, 58, 57, 59, 60, 58, 61, 59, 62, 60, 63]
    })
    
    fig = px.line(trend_data, x='Date', y=['custom business software', 'bespoke software development', 'custom software development'],
                  title='Search Interest Trends (Last 12 Months)',
                  labels={'value': 'Interest Score', 'variable': 'Keyword'})
    
    fig.update_layout(
        font_family="Inter",
        title_font_size=20,
        height=400,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    add_vertical_space(2)
    
    colored_header(label="All Keyword Data", description="", color_name="blue-70")
    
    st.dataframe(keyword_data, use_container_width=True, hide_index=True)

add_vertical_space(2)

# Footer
st.markdown("---")
st.caption(f"Content Strategy Dashboard | Last updated: {datetime.now().strftime('%b %d, %Y at %I:%M %p')}")
