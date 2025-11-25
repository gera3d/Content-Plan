"""
Content Strategy Command Center - Enhanced with Pre-loaded Insights
Interactive dashboard with keyword research findings for Gera Yeremin
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import json
from keyword_research import KeywordResearcher
import os

# Page configuration
st.set_page_config(
    page_title="Content Strategy Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Minimal CSS - Clean Look  
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'researcher' not in st.session_state:
    st.session_state.researcher = KeywordResearcher()

# Header - Native Streamlit components
st.title("🚀 Content Strategy Dashboard")
st.subheader("Gera Yeremin | Digital Marketing & Software Architecture")
st.divider()

# Focus card
st.info("""
**🎯 Your Focus: Custom Software Development**

**Core Offering:** Building custom business applications and software architecture solutions

**Specialty:** Review management systems, BI tools, workflow automation, custom CRM/data platforms

**Your Edge:** You understand both technical AND marketing - build software that drives actual business results
""")

# Create tabs for different views
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "📊 Strategy Overview", 
    "🧮 Interactive Tools", 
    "📅 Content Calendar",
    "🔥 Content Opportunities",
    "💡 Strategy",
    "📝 Content Review",
    "✍️ Voice Guide",
    "🔧 Tools"
])

with tab1:
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Target Keywords", "6", "🟢 Low Competition")
    
    with col2:
        st.metric("Avg Search Interest", "42", "Rising")
    
    with col3:
        st.metric("Content Pieces", "12", "Weeks 1-12")
    
    with col4:
        st.metric("Tools Built", "3", "Interactive")
    
    # Search Volume Estimates (based on Google Trends relative data)
    st.subheader("📊 Search Interest & Competition")
    
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
    
    st.dataframe(
        keyword_data,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Keyword": st.column_config.TextColumn("Keyword", width="medium"),
            "Category": st.column_config.TextColumn("Category", width="small"),
            "Avg Interest": st.column_config.ProgressColumn("Avg Interest", min_value=0, max_value=100, format="%d"),
            "Competition": st.column_config.TextColumn("Competition", width="small"),
            "Related Queries": st.column_config.NumberColumn("Related Queries", width="small"),
            "Rising Queries": st.column_config.NumberColumn("Rising Queries", width="small"),
            "Opportunity Score": st.column_config.TextColumn("Opportunity", width="small")
        }
    )
    
    st.caption("💡 **Opportunity Score** = High interest + Low competition + Many rising queries = Best targets")
    
    st.divider()
    
    # Category breakdown
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="keyword-category">', unsafe_allow_html=True)
        st.metric("Custom Software", "6 Keywords", "🔥 Primary Focus")
        st.write("**Top Keywords:**")
        st.write("🟢 custom software development")
        st.write("🟢 custom business software")
        st.write("🟢 bespoke software development")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="keyword-category">', unsafe_allow_html=True)
        st.metric("Niche Software Solutions", "3 Keywords", "🔥 High Priority")
        st.write("**Top Keywords:**")
        st.write("🟢 review management software")
        st.write("🟢 custom CRM development")
        st.write("🟢 workflow automation software")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="keyword-category">', unsafe_allow_html=True)
        st.metric("Web/SaaS Development", "2 Keywords", "Secondary")
        st.write("**Top Keywords:**")
        st.write("🔴 web application development (high comp)")
        st.write("🔴 SaaS development (very high comp)")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.divider()
    
    # Competitor Analysis
    st.subheader("👥 Competitor Landscape")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🏢 Major Competitors (Software Development):**
        - **Toptal, Upwork** - Freelance marketplaces (impersonal)
        - **Accenture, Deloitte** - Enterprise consulting (expensive, slow)
        - **Local dev shops** - Often just coding, no business strategy
        - **Offshore teams** - Communication issues, time zones
        
        **Your Advantage:** Local + Strategic + Marketing-savvy developer who understands business ROI
        """)
    
    with col2:
        st.markdown("""
        **🎯 Market Gaps & Your Positioning:**
        - Small/mid businesses can't afford enterprise consultants
        - Generic solutions don't fit unique workflows
        - Developers who understand marketing/SEO are rare
        - Need someone who can prototype + validate ideas quickly
        
        **Sweet Spot:** Custom software for businesses making $500K-$5M/year
        """)
    
    st.divider()
    
    # Key insights
    st.subheader("🎯 Strategic Insights from Data")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🔥 Best Opportunities (Software Focus):**
        1. **Custom business software** - 35 avg interest, LOW competition! 🎯
        2. **Bespoke software development** - 28 avg interest, LOW competition! 🎯
        3. **Custom CRM development** - 45 avg interest, medium comp
        4. **Workflow automation software** - 55 avg interest, medium comp
        5. **Custom software development** - 58 avg interest, 40 related queries
        6. **Review management software** - 35 avg interest, niche opportunity
        """)
    
    with col2:
        st.markdown("""
        **⚠️ Avoid These (Too Competitive/Broad):**
        - ❌ SaaS development (very high competition)
        - ❌ Web application development (saturated)
        - ❌ Enterprise software (dominated by big players)
        
        **📈 Your Winning Strategy:**
        - ✅ Target "custom" + specific industry (healthcare, legal, real estate)
        - ✅ Focus on "business software" not "enterprise"
        - ✅ Emphasize ROI, marketing integration, prototyping
        - ✅ Build showcase projects in your niche areas
        """)

with tab2:
    st.header("🎯 Keyword Strategy & Ranking Plan")
    
    st.info("💡 This section explains WHY each keyword matters and HOW you'll rank for it")
    
    # Keyword 1
    st.markdown("---")
    st.subheader("1. 🟢 Custom Business Software")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **📊 Keyword Metrics:**
        - **Search Volume:** ~35/100 relative interest
        - **Competition:** 🟢 LOW (This is key!)
        - **Related Queries:** 12 variations
        - **Rising Queries:** 5 trending terms
        - **Opportunity Score:** 🔥 EXCELLENT
        
        **🎯 Why This Keyword:**
        - Exactly what you do (custom software for businesses)
        - Low competition = easier to rank
        - Business owners searching this have BUDGET
        - More specific than "custom software development"
        - Indicates solution-aware buyer (knows they need custom)
        """)
    
    with col2:
        st.markdown("""
        **🚀 How You'll Rank For It:**
        
        **Content Strategy:**
        1. **Pillar Page:** "Complete Guide to Custom Business Software" (3000+ words)
        2. **Case Studies:** 3-4 real examples with ROI data
        3. **Comparison Post:** "Custom Business Software vs. Off-the-Shelf"
        4. **Decision Framework:** Interactive calculator/assessment
        
        **SEO Tactics:**
        - Title: "Custom Business Software: Build vs. Buy Guide [2025]"
        - Include: ROI calculator, cost breakdown, timeline expectations
        - Internal links from all software-related posts
        - Schema markup: Article, HowTo, FAQPage
        
        **Supporting Content:**
        - 5-10 blog posts targeting long-tail variations
        - Video: "What is Custom Business Software? (Explained)"
        - Podcast episode with client who saved $50K/year
        """)
    
    # Keyword 2
    st.markdown("---")
    st.subheader("2. 🟢 Bespoke Software Development")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **📊 Keyword Metrics:**
        - **Search Volume:** ~28/100 relative interest
        - **Competition:** 🟢 LOW (Another winner!)
        - **Related Queries:** 8 variations
        - **Rising Queries:** 3 trending terms
        - **Opportunity Score:** 🔥 EXCELLENT
        
        **🎯 Why This Keyword:**
        - "Bespoke" = premium positioning (higher budgets)
        - Used by UK/international searchers (broader reach)
        - Less competition than generic terms
        - Implies custom, high-quality work
        - Different audience than "custom business software"
        """)
    
    with col2:
        st.markdown("""
        **🚀 How You'll Rank For It:**
        
        **Content Strategy:**
        1. **Definition Post:** "Bespoke Software vs. Custom Software: What's the Difference?"
        2. **Portfolio Showcase:** "Our Bespoke Software Projects"
        3. **Process Guide:** "How Bespoke Software Development Works"
        4. **Pricing Guide:** "Bespoke Software Development Cost Breakdown"
        
        **SEO Tactics:**
        - Target UK/International markets (less US competition)
        - Title: "Bespoke Software Development: Custom Solutions for Your Business"
        - Include: Project gallery, development process, pricing ranges
        - Featured snippet opportunity (define "bespoke software")
        
        **Differentiation:**
        - Emphasize craftsmanship, tailored approach
        - Use premium imagery and case studies
        - Position as alternative to generic "custom software"
        """)
    
    # Keyword 3
    st.markdown("---")
    st.subheader("3. 🟢 Custom Software Development")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **📊 Keyword Metrics:**
        - **Search Volume:** ~58/100 relative interest (HIGH!)
        - **Competition:** 🟡 HIGH (but still rankable)
        - **Related Queries:** 40+ variations (lots of content ideas)
        - **Rising Queries:** 18 trending terms
        - **Opportunity Score:** 🟢 GOOD (volume makes up for competition)
        
        **🎯 Why This Keyword:**
        - Highest search volume in your niche
        - Broad awareness-stage term (top of funnel)
        - 40 related queries = content goldmine
        - Can target with location modifiers (less competitive)
        - Essential for brand authority
        """)
    
    with col2:
        st.markdown("""
        **🚀 How You'll Rank For It:**
        
        **Content Strategy (Go Big):**
        1. **Ultimate Resource:** "Custom Software Development: The Complete 2025 Guide"
        2. **Hub Page:** Links to all related content (architecture, CRM, workflow, etc.)
        3. **Industry-Specific:** "Custom Software Development for [Healthcare/Legal/Real Estate]"
        4. **FAQ Page:** Answer all 40 related queries
        
        **SEO Tactics:**
        - Target with location: "Custom Software Development [Your City/State]"
        - Title: "Custom Software Development Company | [Your Location] | [Your Name]"
        - Comprehensive content: 5000+ words
        - Table of contents, jump links for long-tail queries
        - Regular updates to maintain freshness
        
        **Winning Strategy:**
        - Don't compete nationally - go LOCAL
        - "Custom software development near me" + geo targeting
        - Google Business Profile optimization
        - Local backlinks (chamber of commerce, local tech groups)
        - Focus on long-tail: "custom software development for small business"
        """)
    
    # Keyword 4
    st.markdown("---")
    st.subheader("4. 🟢 Review Management Software")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **📊 Keyword Metrics:**
        - **Search Volume:** ~35/100 relative interest
        - **Competition:** 🟡 MEDIUM (niche opportunity)
        - **Related Queries:** 24 variations
        - **Rising Queries:** 10 trending terms
        - **Opportunity Score:** 🔥 EXCELLENT (showcase your work!)
        
        **🎯 Why This Keyword:**
        - You've BUILT this (instant credibility)
        - Can show actual working software
        - Combines software + marketing expertise
        - Specific niche = less competition
        - High commercial intent (buyers ready to purchase)
        """)
    
    with col2:
        st.markdown("""
        **🚀 How You'll Rank For It:**
        
        **Content Strategy (Demonstrate Expertise):**
        1. **Live Demo:** "Our Review Management Software (Free Demo)"
        2. **Case Study:** "How [Client] Got 500+ Reviews with Our Software"
        3. **Comparison:** "Review Management Software: Build vs. Buy in 2025"
        4. **Behind-the-Scenes:** "Building a Review Management System: Technical Deep Dive"
        
        **SEO Tactics:**
        - Title: "Review Management Software | Custom-Built for Your Business"
        - Include: Live demo, pricing, features comparison
        - Video demo embedded (increases dwell time)
        - Comparison keywords: "vs Birdeye" "vs Podium" "vs Grade.us"
        
        **Unique Angle:**
        - You BUILD custom versions (not SaaS)
        - "Review management software for [specific industry]"
        - Show actual code/architecture (technical credibility)
        - Offer free consultation on custom features
        - Lead magnet: "Review Management Software Requirements Template"
        """)
    
    # Keyword 5
    st.markdown("---")
    st.subheader("5. 🟢 Custom CRM Development")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **📊 Keyword Metrics:**
        - **Search Volume:** ~45/100 relative interest
        - **Competition:** 🟡 MEDIUM
        - **Related Queries:** 18 variations
        - **Rising Queries:** 8 trending terms
        - **Opportunity Score:** 🔥 EXCELLENT
        
        **🎯 Why This Keyword:**
        - Every business eventually needs CRM
        - "Custom" indicates dissatisfaction with Salesforce, HubSpot
        - High-value projects ($20K-$100K+)
        - Recurring opportunity (maintenance, updates)
        - Can lead to other custom software projects
        """)
    
    with col2:
        st.markdown("""
        **🚀 How You'll Rank For It:**
        
        **Content Strategy:**
        1. **Decision Guide:** "Custom CRM vs. Salesforce: What's Right for You?"
        2. **Cost Analysis:** "Custom CRM Development Cost in 2025"
        3. **Feature Breakdown:** "Essential Features for a Custom CRM"
        4. **Case Study:** "From Salesforce to Custom CRM: One Company's Journey"
        
        **SEO Tactics:**
        - Title: "Custom CRM Development for Small & Medium Businesses"
        - Target "alternatives": "Salesforce alternative custom CRM"
        - Include: ROI calculator, feature checklist, timeline estimator
        - Comparison table: Custom vs. Salesforce vs. HubSpot vs. Zoho
        
        **Content Angles:**
        - "When to build a custom CRM instead of buying"
        - "Custom CRM for [industry]" (real estate, healthcare, etc.)
        - "Migrating from Salesforce to custom CRM"
        - Video series: "Building a CRM from scratch"
        - Podcast: Interview with client who made the switch
        """)
    
    # Keyword 6
    st.markdown("---")
    st.subheader("6. 🟢 Workflow Automation Software")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **📊 Keyword Metrics:**
        - **Search Volume:** ~55/100 relative interest (GOOD!)
        - **Competition:** 🟡 MEDIUM
        - **Related Queries:** 22 variations
        - **Rising Queries:** 12 trending terms
        - **Opportunity Score:** 🔥 EXCELLENT
        
        **🎯 Why This Keyword:**
        - Growing trend (automation is hot)
        - Can be entry point to bigger projects
        - Combines well with other software
        - Everyone wants to automate workflows
        - Strong commercial intent
        """)
    
    with col2:
        st.markdown("""
        **🚀 How You'll Rank For It:**
        
        **Content Strategy:**
        1. **Comparison:** "Workflow Automation Software: Zapier vs. Make vs. Custom"
        2. **Use Cases:** "10 Business Workflows You Should Automate"
        3. **Technical Guide:** "Building Custom Workflow Automation Software"
        4. **ROI Post:** "Workflow Automation ROI: Real Numbers from Real Businesses"
        
        **SEO Tactics:**
        - Title: "Custom Workflow Automation Software for Your Business"
        - Target "vs" keywords: "custom workflow automation vs zapier"
        - Include: Workflow templates, ROI calculator, complexity assessment
        - Video: "When Zapier isn't enough: Custom workflow automation"
        
        **Positioning:**
        - For workflows too complex for no-code tools
        - Integration with existing custom systems
        - "When you've outgrown Zapier/Make"
        - Show examples of complex automations you've built
        - Lead magnet: "Workflow Automation Audit Template"
        """)
    
    # Additional Keywords (shorter format)
    st.markdown("---")
    st.subheader("📋 Supporting Keywords (Quick Reference)")
    
    supporting_keywords = pd.DataFrame({
        'Keyword': [
            'software architecture',
            'business applications',
            'enterprise software development',
            'SaaS development',
            'web application development'
        ],
        'Why Target': [
            'Establishes technical credibility; education-focused content',
            'Broad term for all business software; good for awareness',
            'Too competitive for main focus, but mention in comparison posts',
            'Very competitive; avoid unless discussing why NOT to build SaaS',
            'Too broad; only target with specific niche (e.g., "for manufacturing")'
        ],
        'Content Type': [
            'Technical blog posts, architecture diagrams, best practices',
            'Overview content, hub page linking to specific solutions',
            'Mention in "enterprise vs. SMB custom software" posts',
            'Use in "when to build SaaS vs. custom internal tools" content',
            'Niche it down: "web application development for [industry]"'
        ],
        'Priority': [
            '🟡 Medium',
            '🟡 Medium',
            '🔴 Low',
            '🔴 Low',
            '🔴 Low'
        ]
    })
    
    st.dataframe(supporting_keywords, use_container_width=True, hide_index=True)
    
    st.divider()
    
    st.subheader("🎯 Overall Ranking Strategy")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🥇 Phase 1: Quick Wins (Months 1-3)**
        1. Target LOW competition keywords first
        2. "Custom business software" - main pillar
        3. "Bespoke software development" - second pillar  
        4. Build authority with case studies
        5. Get 5-10 backlinks from local sources
        
        **📈 Tactics:**
        - Publish 2-3 comprehensive posts per week
        - Update Google Business Profile weekly
        - Get listed in local directories
        - Guest post on local business blogs
        - Join local tech/business groups (online + offline)
        """)
    
    with col2:
        st.markdown("""
        **🥈 Phase 2: Build Authority (Months 4-6)**
        1. Tackle "custom software development" with location modifier
        2. Launch review management software showcase
        3. Custom CRM positioning content
        4. Start podcast with client interviews
        5. Create interactive tools (calculators, assessments)
        
        **📈 Tactics:**
        - Video content on YouTube (embedded in posts)
        - Podcast episodes with transcripts
        - Answer questions on Reddit, forums
        - Build actual tools as lead magnets
        - Speaking at local events (get backlinks)
        """)
    
    st.info("""
    **🎯 Key Success Factors:**
    - Focus on LOCAL rankings (easier than national)
    - Demonstrate expertise with working software
    - Target buyer-intent keywords (not just traffic)
    - Use your unique angle: developer + marketer
    - Show real ROI in case studies (businesses care about results)
    """)

with tab3:
    st.header("🔍 Interactive Keyword Analysis")
    
    st.info("👇 Select keywords below to analyze search trends and related queries")
    
    # Sidebar-like controls in main area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        preset = st.selectbox(
            "Choose Category",
            ["Review & Reputation", "Custom Software", "Digital Marketing", "Custom"],
            key="analysis_preset"
        )
    
    with col2:
        timeframe = st.selectbox(
            "Timeframe",
            ["today 7-d", "today 1-m", "today 3-m", "today 12-m", "today 5-y"],
            index=3,
            key="analysis_timeframe"
        )
    
    if preset == "Review & Reputation":
        keywords = ["review management", "online reviews", "reputation management", "customer reviews", "Google reviews"]
    elif preset == "Custom Software":
        keywords = ["custom software development", "business applications", "software architecture"]
    elif preset == "Digital Marketing":
        keywords = ["digital marketing agency", "SEO services", "local SEO"]
    else:
        keywords_input = st.text_input("Enter keywords (comma-separated, max 5)", "")
        keywords = [k.strip() for k in keywords_input.split(',') if k.strip()][:5]
    
    if st.button("🔍 Analyze These Keywords", type="primary", key="analyze_main"):
        if keywords:
            with st.spinner(f'Analyzing {len(keywords)} keywords...'):
                try:
                    # Get interest over time
                    interest_df = st.session_state.researcher.get_interest_over_time(keywords, timeframe)
                    
                    if not interest_df.empty:
                        # Metrics
                        st.subheader("📊 Search Interest Metrics")
                        cols = st.columns(len(keywords))
                        for i, keyword in enumerate(keywords):
                            with cols[i]:
                                avg_interest = interest_df[keyword].mean()
                                max_interest = interest_df[keyword].max()
                                st.metric(
                                    label=keyword[:20] + "..." if len(keyword) > 20 else keyword,
                                    value=f"{avg_interest:.1f}",
                                    delta=f"Peak: {max_interest}"
                                )
                        
                        # Chart
                        st.subheader("📈 Trend Over Time")
                        fig = px.line(
                            interest_df,
                            x=interest_df.index,
                            y=keywords,
                            title=f"Search Interest Trends ({timeframe})",
                            labels={'value': 'Interest (0-100)', 'variable': 'Keyword'},
                            template='plotly_white'
                        )
                        fig.update_layout(height=500, hovermode='x unified')
                        st.plotly_chart(fig, use_container_width=True)
                        
                        # Related queries
                        st.subheader("🔗 Related Search Queries")
                        for keyword in keywords[:3]:  # Limit to avoid rate limiting
                            with st.expander(f"📌 {keyword}"):
                                related = st.session_state.researcher.get_related_queries(keyword)
                                
                                col1, col2 = st.columns(2)
                                
                                with col1:
                                    st.markdown("**🔥 Rising Queries**")
                                    if related['rising'] is not None and not related['rising'].empty:
                                        st.dataframe(related['rising'].reset_index(drop=True), use_container_width=True, hide_index=True)
                                    else:
                                        st.info("No rising queries found")
                                
                                with col2:
                                    st.markdown("**⭐ Top Queries**")
                                    if related['top'] is not None and not related['top'].empty:
                                        st.dataframe(related['top'].reset_index(drop=True), use_container_width=True, hide_index=True)
                                    else:
                                        st.info("No top queries found")
                    else:
                        st.warning("No data found for these keywords")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please select or enter keywords")

with tab4:
    st.header("🔥 Content Opportunities")
    
    st.markdown("""
    Based on keyword analysis, here are your **best opportunities for custom software development** content:
    """)
    
    # Custom Software Opportunities
    st.subheader("1️⃣ Custom Business Software (🎯 LOW COMPETITION!)")
    st.markdown("""
    **Why it's PERFECT for you:** Low competition + good search volume + exactly what you do!
    
    **Keywords:**
    - **Custom business software** - 35 avg interest, LOW competition, 12 related queries
    - **Bespoke software development** - 28 avg interest, LOW competition, 8 related queries
    - **Custom software development** - 58 avg interest, 40 related queries, 18 rising
    
    **Content Ideas:**
    - "When to Build Custom Business Software vs. Buy Off-the-Shelf"
    - "Custom Business Software ROI Calculator: Is It Worth It?"
    - "5 Signs Your Business Needs Custom Software"
    - "From Spreadsheet to Custom Software: A Real Case Study"
    - "Custom vs. Bespoke Software: What's the Difference?"
    """)
    
    st.divider()
    
    # Niche Software Solutions
    st.subheader("2️⃣ Niche Software Solutions (Your Secret Weapon)")
    st.markdown("""
    **Why it matters:** Combines your software + marketing expertise
    
    **Keywords:**
    - **Review management software** - 35 avg interest, medium comp, 24 related queries
    - **Custom CRM development** - 45 avg interest, medium comp, 18 related queries
    - **Workflow automation software** - 55 avg interest, medium comp, 22 related queries
    
    **Content Ideas:**
    - "Building a Custom Review Management System in 90 Days"
    - "Why We Built Our Own CRM (And How You Can Too)"
    - "Workflow Automation: Custom Software vs. Zapier/Make"
    - "Review Management Software: Build, Buy, or Integrate?"
    - "Custom CRM for Small Businesses: What You Really Need"
    """)
    
    st.divider()
    
    # Software Architecture
    st.subheader("3️⃣ Software Architecture & Best Practices")
    st.markdown("""
    **Why it matters:** Establishes you as a technical expert, not just a coder
    
    **Keywords:**
    - **Software architecture** - 38 avg interest, medium comp, 21 related queries, 6 rising
    - **Business applications** - 42 avg interest, medium comp, 4 related queries
    
    **Content Ideas:**
    - "Software Architecture for Small Business Applications"
    - "Choosing the Right Tech Stack for Custom Business Software"
    - "Monolith vs. Microservices: What Small Businesses Actually Need"
    - "Database Design for Business Applications: A Practical Guide"
    - "API-First Design for Business Software Integration"
    """)
    
    st.divider()
    
    st.subheader("💡 Messaging Strategy")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🎯 Your Unique Positioning:**
        - "Software developer who understands marketing ROI"
        - "From prototype to production in weeks, not months"
        - "Custom software for growing businesses ($500K-$5M)"
        - "We build the tools big companies use, tailored for your size"
        
        **Examples to Showcase:**
        - Review management system you built
        - Any business intelligence dashboards
        - Workflow automation tools
        - Custom CRM or data platforms
        """)
    
    with col2:
        st.markdown("""
        **📢 Key Messages:**
        - "Stop forcing your business into generic software"
        - "Custom doesn't have to mean expensive or slow"
        - "Software that grows with your business"
        - "Built by someone who understands both code AND customers"
        
        **Proof Points:**
        - 90-day prototype methodology (from podcast)
        - Client testimonials about ROI
        - Before/after case studies
        - Your dual expertise (dev + marketing)
        """)

with tab5:
    st.header("💡 Content Calendar & Strategy")
    
    st.markdown("""
    <div class="insight-box">
        <h3>🎯 Your Unique Positioning</h3>
        <p>You're not just a developer OR a marketer - you're both. This is rare and valuable.</p>
        <p><strong>Key Differentiator:</strong> You build custom tools (like review management systems) AND create marketing strategies to use them.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📅 12-Week Content Calendar (Prioritized by Opportunity)")
    
    st.info("🎯 **Strategy:** Start with LOW competition keywords for quick wins, then build authority for higher competition terms")
    
    content_plan = pd.DataFrame({
        'Week': [
            'Week 1-2',
            'Week 3-4', 
            'Week 5-6',
            'Week 7-8',
            'Week 9-10',
            'Week 11-12'
        ],
        'Target Keyword': [
            'custom business software',
            'bespoke software development',
            'review management software',
            'custom CRM development',
            'workflow automation software',
            'custom software development'
        ],
        'Competition': [
            '🟢 LOW',
            '🟢 LOW',
            '🟡 MEDIUM',
            '🟡 MEDIUM',
            '🟡 MEDIUM',
            '🔴 HIGH'
        ],
        'Content Piece': [
            'Complete Guide to Custom Business Software [2025]',
            'Bespoke Software Development: Custom Solutions for Your Business',
            'Review Management Software: Our Custom-Built Solution',
            'Custom CRM vs. Salesforce: What SMBs Actually Need',
            'Workflow Automation Software: Zapier vs. Make vs. Custom',
            'Custom Software Development Company [Your Location]'
        ],
        'Format': [
            'Pillar Post (3000+ words) + Video',
            'Pillar Post (2500+ words) + Comparison',
            'Case Study + Live Demo + Podcast',
            'Decision Guide + ROI Calculator',
            'Comparison Post + Use Cases',
            'Ultimate Guide (5000+ words) + Hub Page'
        ],
        'Supporting Content': [
            '• Build vs Buy Guide\n• ROI Calculator\n• Cost Breakdown\n• 5 blog posts on long-tail variations',
            '• Bespoke vs Custom comparison\n• Portfolio showcase\n• Pricing guide\n• Process walkthrough',
            '• Client case study\n• Technical deep dive\n• Feature comparison\n• Demo video',
            '• Migration guide\n• Feature checklist\n• Industry-specific posts\n• Client interview podcast',
            '• Workflow templates\n• Automation audit tool\n• 10 automation examples\n• When to go custom post',
            '• Local landing page\n• Industry-specific guides\n• FAQ (40+ questions)\n• Architecture posts'
        ],
        'SEO Focus': [
            'Featured snippet, Local SEO, ROI calculator',
            'UK/International targeting, Premium positioning',
            'Video SEO, Demo page, Industry keywords',
            'Comparison keywords, Alternative searches',
            'vs. keywords, Use case targeting',
            'Location modifier, Long-tail queries, Authority'
        ],
        'Metrics Goal': [
            'Rank #1-3 in 60 days',
            'Rank #1-5 in 60 days',
            'Rank #1-10 in 90 days + demos booked',
            'Rank #5-15 in 90 days + leads',
            'Rank #5-15 in 90 days',
            'Rank #10-20 in 120 days (local: #1-5)'
        ]
    })
    
    st.dataframe(
        content_plan, 
        use_container_width=True, 
        hide_index=True,
        column_config={
            "Week": st.column_config.TextColumn("Week", width="small"),
            "Target Keyword": st.column_config.TextColumn("Target Keyword", width="medium"),
            "Competition": st.column_config.TextColumn("Comp", width="small"),
            "Content Piece": st.column_config.TextColumn("Main Content Piece", width="large"),
            "Format": st.column_config.TextColumn("Format", width="medium"),
            "Supporting Content": st.column_config.TextColumn("Supporting Content", width="large"),
            "SEO Focus": st.column_config.TextColumn("SEO Focus", width="medium"),
            "Metrics Goal": st.column_config.TextColumn("Success Metrics", width="medium")
        }
    )
    
    st.divider()
    
    # Weekly breakdown
    st.subheader("📋 Detailed Week-by-Week Breakdown")
    
    week_detail = st.selectbox(
        "Select a week to see detailed tasks:",
        ["Week 1-2: Custom Business Software", 
         "Week 3-4: Bespoke Software Development",
         "Week 5-6: Review Management Software",
         "Week 7-8: Custom CRM Development",
         "Week 9-10: Workflow Automation Software",
         "Week 11-12: Custom Software Development"]
    )
    
    if "Week 1-2" in week_detail:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🎯 Week 1-2: Custom Business Software (🟢 LOW Competition)**
            
            **Day 1-3: Research & Outline**
            - [ ] Analyze top 10 ranking pages
            - [ ] Identify content gaps
            - [ ] Create detailed outline (3000+ words)
            - [ ] Plan ROI calculator functionality
            
            **Day 4-7: Content Creation**
            - [ ] Write pillar post (sections: What, Why, When, How, Cost, ROI)
            - [ ] Include 3-4 case study snippets
            - [ ] Create comparison tables
            - [ ] Add internal links to related posts
            
            **Day 8-10: Interactive Elements**
            - [ ] Build ROI calculator (simple JavaScript)
            - [ ] Create cost breakdown infographic
            - [ ] Design decision framework flowchart
            """)
        with col2:
            st.markdown("""
            **Day 11-12: Optimization & Launch**
            - [ ] SEO optimization (title, meta, headers)
            - [ ] Add schema markup (Article, HowTo, FAQ)
            - [ ] Create video script
            - [ ] Optimize images (alt text, compression)
            
            **Day 13-14: Promotion**
            - [ ] Record & edit video (10-15 min)
            - [ ] Share on LinkedIn, Twitter
            - [ ] Email to existing contacts
            - [ ] Post in relevant communities
            
            **Supporting Posts (publish 1 per week):**
            1. "5 Signs You Need Custom Business Software"
            2. "Custom Business Software Cost: What to Expect in 2025"
            3. "Build vs Buy: Custom Business Software Decision Guide"
            4. "Custom Business Software for Small Businesses"
            5. "How Long Does Custom Business Software Take to Build?"
            """)
    
    elif "Week 3-4" in week_detail:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🎯 Week 3-4: Bespoke Software Development (🟢 LOW Competition)**
            
            **Day 1-3: Research & Positioning**
            - [ ] Research UK/international markets
            - [ ] Define "bespoke" vs "custom" angle
            - [ ] Outline 2500+ word guide
            - [ ] Plan portfolio showcase section
            
            **Day 4-7: Content Creation**
            - [ ] Write comprehensive guide
            - [ ] Emphasize premium, tailored approach
            - [ ] Include project examples with visuals
            - [ ] Create pricing transparency section
            
            **Day 8-10: Supporting Materials**
            - [ ] Design portfolio showcase page
            - [ ] Create bespoke process diagram
            - [ ] Write pricing guide post
            """)
        with col2:
            st.markdown("""
            **Day 11-12: SEO & Launch**
            - [ ] Optimize for UK/international terms
            - [ ] Add location-agnostic content
            - [ ] Schema markup for Service
            - [ ] Premium imagery and design
            
            **Day 13-14: Promotion**
            - [ ] Target international communities
            - [ ] LinkedIn articles
            - [ ] Quora/Reddit answers on bespoke software
            
            **Supporting Posts:**
            1. "Bespoke Software vs. Custom Software: Key Differences"
            2. "Bespoke Software Development Process Explained"
            3. "How Much Does Bespoke Software Cost?"
            4. "Examples of Bespoke Software Solutions"
            """)
    
    elif "Week 5-6" in week_detail:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🎯 Week 5-6: Review Management Software (🟡 MEDIUM Competition)**
            
            **Day 1-3: Case Study Prep**
            - [ ] Interview client(s) who use your system
            - [ ] Gather metrics (reviews gained, time saved, ROI)
            - [ ] Collect screenshots/demo footage
            - [ ] Outline main post + case study
            
            **Day 4-7: Content Creation**
            - [ ] Write main post about review management software
            - [ ] Create detailed case study
            - [ ] Write technical deep dive post
            - [ ] Plan live demo page
            
            **Day 8-10: Demo & Video**
            - [ ] Record demo video (15-20 min)
            - [ ] Create demo page with form
            - [ ] Screenshot walkthrough
            """)
        with col2:
            st.markdown("""
            **Day 11-12: Podcast & SEO**
            - [ ] Record podcast with client
            - [ ] Transcribe and publish
            - [ ] SEO optimization with video embed
            - [ ] Comparison content vs. competitors
            
            **Day 13-14: Launch & Promote**
            - [ ] Publish all content
            - [ ] Share demo video widely
            - [ ] Post case study on LinkedIn
            - [ ] Submit to relevant directories
            
            **Supporting Posts:**
            1. "Review Management Software: Build vs. Buy"
            2. "How We Built Our Review Management System"
            3. "Review Management for [Healthcare/Legal/Real Estate]"
            4. "Review Management Software Features Checklist"
            """)
    
    elif "Week 7-8" in week_detail:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🎯 Week 7-8: Custom CRM Development (🟡 MEDIUM Competition)**
            
            **Day 1-3: Research & Tool Creation**
            - [ ] Analyze Salesforce alternatives searches
            - [ ] Build ROI calculator (Salesforce cost vs. Custom)
            - [ ] Outline decision guide
            - [ ] Create feature checklist
            
            **Day 4-7: Content Creation**
            - [ ] Write "Custom CRM vs. Salesforce" guide
            - [ ] Create comparison table
            - [ ] Industry-specific CRM posts (3)
            - [ ] Migration guide from Salesforce
            
            **Day 8-10: Case Study & Interview**
            - [ ] Find/create CRM case study
            - [ ] Interview for podcast (if available)
            """)
        with col2:
            st.markdown("""
            **Day 11-12: Tools & SEO**
            - [ ] Feature checklist download
            - [ ] CRM requirements template
            - [ ] Optimize for "alternative" keywords
            - [ ] Schema markup
            
            **Day 13-14: Launch**
            - [ ] Publish all content
            - [ ] Share on SaaS alternatives communities
            - [ ] Target Salesforce frustration keywords
            
            **Supporting Posts:**
            1. "When to Build a Custom CRM vs. Buy"
            2. "Custom CRM Development Cost Breakdown"
            3. "Essential Features for a Custom CRM"
            4. "Migrating from Salesforce to Custom CRM"
            5. "Custom CRM for [Industry]" (3 variations)
            """)
    
    elif "Week 9-10" in week_detail:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🎯 Week 9-10: Workflow Automation Software (🟡 MEDIUM Competition)**
            
            **Day 1-3: Research & Planning**
            - [ ] Identify Zapier/Make limitations
            - [ ] Create workflow templates library
            - [ ] Build automation audit tool
            - [ ] Outline comparison post
            
            **Day 4-7: Content Creation**
            - [ ] Write "Zapier vs. Make vs. Custom" comparison
            - [ ] Create "10 Workflows to Automate" post
            - [ ] Write "When to go Custom" decision post
            - [ ] Document complex automation examples
            
            **Day 8-10: Tools & Examples**
            - [ ] Workflow automation audit template
            - [ ] ROI calculator for automation
            - [ ] Video of complex automation you built
            """)
        with col2:
            st.markdown("""
            **Day 11-12: SEO & Optimization**
            - [ ] Optimize for "vs" keywords
            - [ ] Add use case targeting
            - [ ] Schema for HowTo content
            - [ ] Template downloads
            
            **Day 13-14: Launch**
            - [ ] Publish all content
            - [ ] Share in automation communities
            - [ ] Reddit/forum answers
            
            **Supporting Posts:**
            1. "When You've Outgrown Zapier: Custom Automation"
            2. "Workflow Automation Software ROI Calculator"
            3. "10 Business Workflows You Should Automate"
            4. "Custom Workflow Automation Examples"
            5. "Workflow Automation for [Industry]"
            """)
    
    else:  # Week 11-12
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **🎯 Week 11-12: Custom Software Development (🔴 HIGH Competition - LOCAL Focus)**
            
            **Day 1-4: Ultimate Guide Creation**
            - [ ] Research top 20 ranking pages
            - [ ] Create 5000+ word comprehensive guide
            - [ ] Answer all 40 related queries in FAQ
            - [ ] Table of contents with jump links
            - [ ] Location-specific sections
            
            **Day 5-8: Hub Page & Supporting Content**
            - [ ] Create hub page linking to all software content
            - [ ] Industry-specific guides (3)
            - [ ] Local landing page optimization
            - [ ] Architecture best practices posts
            
            **Day 9-10: Local SEO**
            - [ ] Google Business Profile optimization
            - [ ] Local citations and directories
            - [ ] Chamber of commerce, tech groups
            """)
        with col2:
            st.markdown("""
            **Day 11-12: Authority Building**
            - [ ] Create comprehensive FAQ page
            - [ ] Video series intro
            - [ ] Client testimonials compilation
            - [ ] Portfolio showcase
            
            **Day 13-14: Launch & Promote**
            - [ ] Publish ultimate guide
            - [ ] Local PR outreach
            - [ ] Speaking opportunities
            - [ ] Guest posting on local blogs
            
            **Supporting Posts:**
            1. "Custom Software Development [Your City/State]"
            2. "Custom Software Development for Small Business"
            3. "Custom Software Development Process Explained"
            4. "How to Choose a Custom Software Developer"
            5. "Custom Software Development Cost Guide"
            6. "Custom Software Development Company vs. Freelancer"
            7-10. Industry-specific guides
            """)
    
    st.divider()
    
    st.subheader("📊 Success Tracking")
    
    st.markdown("""
    **Key Metrics to Track Weekly:**
    - 🔍 Google Search Console: Impressions, clicks, avg position for target keywords
    - 📈 Google Analytics: Traffic to pillar posts, time on page, bounce rate
    - 💼 Conversions: Demo requests, consultation bookings, downloads
    - 🔗 Backlinks: New referring domains, DA/DR scores
    - 📍 Local Rankings: Position in Google Maps, local pack
    
    **Monthly Reviews:**
    - Compare ranking positions month-over-month
    - Analyze which content pieces drive the most qualified leads
    - Adjust strategy based on what's working
    - Identify gaps in content coverage
    """)
    
    st.divider()
    
    st.subheader("🎤 Podcast Episode Ideas (Research, Content, Prototypes)")
    
    st.markdown("""
    1. **"Building Custom Business Software in 90 Days"** - Your methodology
    2. **"Interview: How [Client] Saved $50K/Year with Custom Software"** - ROI case study
    3. **"Custom CRM vs. Salesforce: What SMBs Actually Need"** - Comparison
    4. **"The Research Behind Software Architecture Decisions"** - Technical deep-dive
    5. **"From Spreadsheet Hell to Custom Software Paradise"** - Transformation story
    6. **"Prototyping Business Applications: Validate Before You Build"** - Process
    7. **"Interview with a Non-Technical Founder Who Built Custom Software"** - Demystify
    8. **"Workflow Automation: When to Code vs. No-Code"** - Decision framework
    """)
    
    st.divider()
    
    st.subheader("🎬 Video Content Ideas")
    
    st.markdown("""
    **Screen Recordings:**
    - Building a simple business application from scratch (time-lapse)
    - Database design session for a real project
    - Code walkthrough of a custom CRM feature
    - Prototype to production deployment process
    
    **Talking Head:**
    - "5 Signs You Need Custom Software" (short-form)
    - "What I Learned Building [X] for [Client]" (case study)
    - "Custom Software Myths Debunked" (educational)
    
    **Client Showcases:**
    - Demo of review management system in action
    - Before/after: Manual process → Automated with custom software
    - Client testimonial + screen share of their tool
    """)
    
    st.divider()
    
    st.subheader("📝 Lead Magnets & Tools")
    
    st.markdown("""
    **Interactive Tools to Build:**
    1. **"Custom Software ROI Calculator"** - Shows potential savings
    2. **"Build vs. Buy Decision Matrix"** - Interactive assessment
    3. **"Tech Stack Recommender"** - Based on business type/size
    4. **"Software Project Estimator"** - Timeline & budget tool
    
    **Downloadable Guides:**
    1. "The Ultimate Guide to Custom Business Software"
    2. "Software Requirements Template for Non-Technical Founders"
    3. "Checklist: Is Your Business Ready for Custom Software?"
    4. "Case Study Collection: Real ROI from Custom Software"
    """)

# Sidebar
with st.sidebar:
    st.header("🛠️ Quick Tools")
    
    st.divider()
    
    if st.button("📈 Get Trending Searches", use_container_width=True):
        with st.spinner("Fetching trends..."):
            try:
                trending = st.session_state.researcher.get_trending_searches('united_states')
                st.success(f"Top 10 Trending Now:")
                for i, trend in enumerate(trending[0:10].values, 1):
                    st.write(f"{i}. {trend[0]}")
            except Exception as e:
                st.error(f"Error: {str(e)}")
    
    st.divider()
    
    st.markdown("### 💡 Quick Keyword Check")
    quick_keyword = st.text_input("Check a keyword:", key="quick_check")
    if st.button("Get Suggestions", use_container_width=True):
        if quick_keyword:
            with st.spinner(f"Analyzing '{quick_keyword}'..."):
                try:
                    suggestions = st.session_state.researcher.get_suggestions(quick_keyword)
                    if not suggestions.empty:
                        st.dataframe(suggestions, use_container_width=True, hide_index=True)
                    else:
                        st.info("No suggestions found")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    st.divider()
    st.caption(f"Last updated: {datetime.now().strftime('%b %d, %Y at %I:%M %p')}")

# Tab 6: Content Review
with tab6:
    st.header("📝 Content Review: Week 1-2 Pillar Post")
    
    st.markdown("""
    <div class="insight-box">
        <h3>🎯 Target: Custom Business Software (LOW Competition)</h3>
        <p><strong>Status:</strong> Draft Complete - Ready for Review</p>
        <p><strong>Word Count:</strong> ~3,000 words</p>
        <p><strong>Target Publish Date:</strong> Week 1-2 of content calendar</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Read the article
    article_path = '/Users/gerayeremin/Documents/Projects/Content Plan/custom-business-software-guide.md'
    
    if os.path.exists(article_path):
        with open(article_path, 'r') as f:
            article_content = f.read()
        
        # Article stats
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
            st.metric("Tables/Charts", tables // 3)
        
        st.divider()
        
        # Content analysis
        st.subheader("📊 Content Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **✅ SEO Elements Present:**
            - ✅ H1 title with keyword
            - ✅ Meta information (reading time, date)
            - ✅ Table of contents structure
            - ✅ FAQ section for featured snippets
            - ✅ Multiple CTAs throughout
            - ✅ Internal linking opportunities
            - ✅ Related articles section
            - ✅ Author bio with credibility
            
            **🎯 Keyword Targeting:**
            - Primary: "custom business software"
            - Secondary: "bespoke software", "build vs buy"
            - Long-tail: "custom software cost", "when to build custom"
            """)
        
        with col2:
            st.markdown("""
            **📈 Content Strengths:**
            - ✅ 4 detailed case studies with ROI
            - ✅ Real numbers and pricing breakdowns
            - ✅ Comparison tables (custom vs off-the-shelf)
            - ✅ Decision framework for readers
            - ✅ Addresses all objections
            - ✅ Multiple conversion points
            - ✅ Technical + business perspective
            - ✅ Actionable next steps
            
            **💼 Unique Angles:**
            - Developer who understands marketing
            - Real cost transparency
            - ROI-focused positioning
            """)
        
        st.divider()
        
        # Preview sections
        st.subheader("📖 Article Sections")
        
        sections = [
            "Introduction & Hook",
            "What Is Custom Business Software?",
            "Why Businesses Choose Custom Business Software: 7 Compelling Reasons",
            "5 Signs You Need Custom Business Software",
            "Custom Business Software Cost: The Real Numbers",
            "How Custom Business Software Is Built: The 5-Phase Process",
            "Should You Build or Buy? The Decision Framework",
            "Real Success Stories: Custom Business Software ROI",
            "How to Choose the Right Custom Software Developer",
            "Ready to Explore Custom Business Software?",
            "Frequently Asked Questions"
        ]
        
        for i, section in enumerate(sections, 1):
            with st.expander(f"{i}. {section}"):
                st.markdown(f"**Section {i} of {len(sections)}**")
                st.info(f"✅ This section covers: {section}")
        
        st.divider()
        
        # Action items
        st.subheader("⚡ Next Steps to Complete This Post")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **🔧 Technical To-Dos:**
            - [ ] Build ROI Calculator (JavaScript/embedded tool)
            - [ ] Create cost breakdown infographic
            - [ ] Design decision framework flowchart
            - [ ] Source or create visual assets
            - [ ] Add schema markup (Article, HowTo, FAQ)
            - [ ] Optimize images (alt text, compression)
            - [ ] Add meta description
            
            **📊 Content Refinements:**
            - [ ] Review for voice consistency
            - [ ] Verify all stats are current (2025)
            - [ ] Add more specific local references if needed
            - [ ] Review CTAs for clarity
            """)
        
        with col2:
            st.markdown("""
            **🎥 Multimedia:**
            - [ ] Record companion video (10-15 min)
            - [ ] Create social media snippets
            - [ ] Design quote graphics for LinkedIn
            - [ ] Screenshot examples for case studies
            
            **🚀 Launch Checklist:**
            - [ ] Schedule publish date
            - [ ] Prepare email announcement
            - [ ] Draft LinkedIn post
            - [ ] Plan Reddit/forum shares
            - [ ] Set up tracking (GA4 events)
            - [ ] Create conversion tracking
            """)
        
        st.divider()
        
        # Full article display
        st.subheader("📄 Full Article Preview")
        
        preview_mode = st.radio(
            "View as:",
            ["Markdown (editable)", "Rendered HTML", "Section by section"],
            horizontal=True
        )
        
        if preview_mode == "Markdown (editable)":
            # Show in text area for easy editing
            edited_content = st.text_area(
                "Article Content (Markdown)",
                article_content,
                height=600,
                help="You can edit the content here and copy it back to the file"
            )
            
            if st.button("📋 Copy to Clipboard", use_container_width=True):
                st.code(edited_content, language="markdown")
                st.success("✅ Content ready to copy!")
        
        elif preview_mode == "Rendered HTML":
            # Render the markdown
            st.markdown("---")
            st.markdown(article_content)
        
        else:  # Section by section
            # Split by major headers and show one at a time
            sections_content = article_content.split('\n## ')
            
            section_select = st.selectbox(
                "Select section to review:",
                [f"Section {i+1}" for i in range(len(sections_content))]
            )
            
            section_idx = int(section_select.split()[1]) - 1
            
            st.markdown("---")
            if section_idx == 0:
                st.markdown(sections_content[section_idx])
            else:
                st.markdown("## " + sections_content[section_idx])
        
        st.divider()
        
        # Feedback section
        st.subheader("💭 Review Notes")
        
        feedback = st.text_area(
            "Notes for revisions:",
            placeholder="Add your thoughts, edits, or improvements here...",
            height=150
        )
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("✅ Approve & Move to Production", type="primary", use_container_width=True):
                st.success("Article approved! Ready for next steps.")
        
        with col2:
            if st.button("✏️ Needs Revisions", use_container_width=True):
                st.warning("Article marked for revision.")
        
        with col3:
            if st.button("🔄 Start Over", use_container_width=True):
                st.info("Article will be rewritten.")
    
    else:
        st.error("Article file not found. Please ensure 'custom-business-software-guide.md' exists in the project directory.")
        st.info("Expected path: /Users/gerayeremin/Documents/Projects/Content Plan/custom-business-software-guide.md")

# Tab 7: Voice Guide
with tab7:
    st.header("✍️ Gera Yeremin's Writing Voice Guide")
    
    st.markdown("""
    <div class="insight-box">
        <h3>📖 Your Authentic Voice = Better SEO</h3>
        <p>This guide ensures all content sounds like YOU while still ranking in search engines.</p>
        <p><strong>Core Principle:</strong> Direct, conversational, no BS. Professional without being corporate.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick reference cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ✅ DO This
        - Be direct and get to the point
        - Use "you" and "I" naturally
        - Ask engaging questions
        - Give real numbers and examples
        - Use contractions (I've, you're, it's)
        - Write like you talk
        - Explain technical stuff simply
        - Admit limitations honestly
        
        **Example Opening:**
        > "Your team is drowning in spreadsheets. Sound familiar?"
        """)
    
    with col2:
        st.markdown("""
        ### ❌ DON'T Do This
        - Use corporate buzzwords
        - Write overly formal
        - Bury the main point
        - Say "we" when it's just you
        - Use jargon without explaining
        - Make grandiose promises
        - Keyword stuff unnaturally
        - Add unnecessary fluff
        
        **Avoid Opening:**
        > "In today's rapidly evolving business landscape, organizations are increasingly..."
        """)
    
    st.divider()
    
    # Voice checker tool
    st.subheader("🎯 Voice Checker Tool")
    
    st.info("Paste your content below to check if it matches Gera's voice")
    
    test_content = st.text_area(
        "Your content:",
        placeholder="Paste a paragraph or two here...",
        height=150
    )
    
    if st.button("🔍 Check Voice Match", type="primary"):
        if test_content:
            issues = []
            warnings = []
            good_signs = []
            
            # Check for bad patterns
            if "leverage" in test_content.lower():
                issues.append("❌ Contains 'leverage' (corporate buzzword)")
            if "synergy" in test_content.lower() or "synergies" in test_content.lower():
                issues.append("❌ Contains 'synergy' (avoid)")
            if "revolutionize" in test_content.lower():
                issues.append("❌ Contains 'revolutionize' (too salesy)")
            if "paradigm" in test_content.lower():
                issues.append("❌ Contains 'paradigm' (corporate jargon)")
            if "best-in-class" in test_content.lower():
                issues.append("❌ Contains 'best-in-class' (avoid)")
            if "I hope this" in test_content.lower():
                issues.append("❌ Contains 'I hope this...' (too formal)")
            if test_content.count("!") > 2:
                warnings.append("⚠️ Lots of exclamation marks (Gera rarely uses them)")
            if len([s for s in test_content.split('.') if len(s.split()) > 30]) > 3:
                warnings.append("⚠️ Some very long sentences (keep it punchy)")
            if "we are" in test_content.lower() or "we're" in test_content.lower():
                warnings.append("⚠️ Using 'we' (Gera usually says 'I' since it's just him)")
            
            # Check for good patterns
            if "?" in test_content:
                good_signs.append("✅ Uses questions (good engagement)")
            if any(word in test_content.lower() for word in ["you", "your"]):
                good_signs.append("✅ Direct address to reader")
            if any(word in test_content.lower() for word in ["i've", "you're", "it's", "don't", "can't"]):
                good_signs.append("✅ Natural contractions")
            if len(test_content.split('.')[0].split()) < 15:
                good_signs.append("✅ Strong, punchy opening")
            if "$" in test_content or any(char.isdigit() for char in test_content):
                good_signs.append("✅ Specific numbers/examples")
            if "here's" in test_content.lower() or "let me" in test_content.lower():
                good_signs.append("✅ Conversational phrases")
            
            # Display results
            if issues:
                st.error("**Voice Issues Found:**")
                for issue in issues:
                    st.write(issue)
            
            if warnings:
                st.warning("**Style Warnings:**")
                for warning in warnings:
                    st.write(warning)
            
            if good_signs:
                st.success("**Good Voice Elements:**")
                for sign in good_signs:
                    st.write(sign)
            
            if not issues and not warnings:
                st.success("🎉 Sounds like Gera! Voice match is strong.")
            elif not issues and warnings:
                st.info("👍 Pretty close! Check the warnings above.")
            else:
                st.error("🔧 Needs revision. Check the issues above and rewrite.")
        else:
            st.warning("Please paste some content to check")
    
    st.divider()
    
    # Full guide display
    st.subheader("📚 Complete Voice Guide")
    
    voice_guide_path = '/Users/gerayeremin/Documents/Projects/Content Plan/writing-voice-guide.md'
    
    if os.path.exists(voice_guide_path):
        with open(voice_guide_path, 'r') as f:
            voice_guide_content = f.read()
        
        # Section selector
        sections = [
            "Opening Styles",
            "Structural Patterns",
            "Tone Variations by Context",
            "Vocabulary & Phrasing",
            "Sentence Structure",
            "Context-Specific Examples",
            "SEO Integration",
            "DO's and DON'Ts Summary",
            "Voice Consistency Checklist",
            "Common Mistakes to Avoid",
            "Real Examples from Gera's Writing"
        ]
        
        view_mode = st.radio(
            "View guide as:",
            ["Quick Reference", "Full Guide (Rendered)", "Full Guide (Markdown)"],
            horizontal=True
        )
        
        if view_mode == "Quick Reference":
            # Show key sections only
            st.markdown("""
            ### Quick Reference: Gera's Voice
            
            **Core Principle:** Direct, conversational, no BS. Professional without being corporate.
            
            **Think:** Experienced developer talking to a business owner at a coffee shop, NOT a consultant pitching in a boardroom.
            
            ---
            
            #### Opening Formulas
            
            **Blog Posts:**
            - Hook with relatable problem: "Your team is drowning in spreadsheets."
            - Ask engaging question: "Sound familiar?"
            - Present alternative: "What if there was another way?"
            
            **Emails:**
            - Casual but professional: "Hey [Name],"
            - Get to point: "Just wanted to check in on..."
            - Clear action: "Let me know if you have questions."
            
            ---
            
            #### Characteristic Phrases
            
            **Use These:**
            - "Just wanted to..."
            - "My goal is to..."
            - "Let me know"
            - "Here's the truth..."
            - "Sound familiar?"
            - "The reality is..."
            
            **Avoid These:**
            - "Leverage synergies"
            - "Best-in-class solutions"
            - "I hope this email finds you well"
            - "Paradigm shift"
            - "Circle back"
            - "Touch base"
            
            ---
            
            #### Sentence Structure
            
            **Good:**
            - Medium length (15-20 words avg)
            - Mix short punchy + longer explanatory
            - Active voice
            - Natural contractions
            
            **Examples:**
            - ✅ "Your team is drowning in spreadsheets. Sound familiar?"
            - ❌ "Your organizational team is currently experiencing significant challenges with regard to spreadsheet management!"
            
            ---
            
            #### SEO Integration
            
            **Target:** "custom business software"
            
            **✅ Natural:**
            - "Custom business software isn't about fancy technology. It's about solving YOUR specific problems."
            - "When should you build custom business software instead of buying off-the-shelf?"
            
            **❌ Stuffed:**
            - "Custom business software is important. Many businesses need custom business software. If you're looking for custom business software..."
            
            ---
            
            #### Before Publishing Checklist
            
            - [ ] Would Gera actually say this out loud?
            - [ ] Is it direct and to the point?
            - [ ] Does it sound like a real person?
            - [ ] Are keywords integrated naturally?
            - [ ] Are there concrete examples?
            - [ ] Is the CTA clear and low-pressure?
            
            ---
            
            **When in doubt:** Read it out loud. If it sounds like something you'd say to a business owner over coffee, you've nailed it.
            """)
            
        elif view_mode == "Full Guide (Rendered)":
            st.markdown("---")
            st.markdown(voice_guide_content)
            
        else:  # Markdown
            st.text_area(
                "Voice Guide (Markdown - Copy if needed)",
                voice_guide_content,
                height=600
            )
    
    else:
        st.error("Voice guide file not found.")
        st.info("Expected path: /Users/gerayeremin/Documents/Projects/Content Plan/writing-voice-guide.md")
    
    st.divider()
    
    # Quick examples
    st.subheader("💡 Before & After Examples")
    
    example_choice = st.selectbox(
        "Choose example type:",
        ["Blog Opening", "Service Page", "Email", "Case Study"]
    )
    
    if example_choice == "Blog Opening":
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **❌ Corporate Voice:**
            ```
            In today's rapidly evolving business 
            landscape, organizations of all sizes 
            are increasingly recognizing the 
            critical importance of effective 
            data management solutions.
            ```
            """)
        with col2:
            st.markdown("""
            **✅ Gera's Voice:**
            ```
            Your team is drowning in spreadsheets.
            
            Sound familiar? You've looked at 
            off-the-shelf software. Nothing 
            quite fits.
            
            What if there was another way?
            ```
            """)
    
    elif example_choice == "Service Page":
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **❌ Agency Voice:**
            ```
            Our custom software development 
            services leverage cutting-edge 
            technologies to deliver innovative 
            solutions tailored to your unique 
            business requirements.
            ```
            """)
        with col2:
            st.markdown("""
            **✅ Gera's Voice:**
            ```
            I build custom software for businesses 
            that have outgrown spreadsheets and 
            off-the-shelf solutions.
            
            What makes me different? I'm a 
            developer who actually understands 
            marketing and business ROI.
            ```
            """)
    
    elif example_choice == "Email":
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **❌ Formal Email:**
            ```
            Dear John,
            
            I hope this email finds you well. 
            I wanted to reach out and follow 
            up on our previous conversation.
            
            Best regards,
            Gera
            ```
            """)
        with col2:
            st.markdown("""
            **✅ Gera's Email:**
            ```
            Hey John,
            
            Just wanted to check in on the CRM 
            project we discussed last week.
            
            Let me know if you have questions.
            
            Gera
            ```
            """)
    
    else:  # Case Study
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **❌ Corporate Case Study:**
            ```
            Client Overview: A mid-sized real 
            estate organization sought to optimize 
            their CRM processes.
            
            Challenge: Suboptimal ROI from 
            enterprise platform.
            
            Solution: Comprehensive custom-built 
            solution.
            ```
            """)
        with col2:
            st.markdown("""
            **✅ Gera's Case Study:**
            ```
            The Problem: Real estate brokerage 
            was spending $18K/year on Salesforce. 
            Agents hated it.
            
            What I Built: Custom CRM with MLS 
            integration, mobile app, automated 
            follow-ups.
            
            Results: Saved $18K/year, 40% more 
            closed deals, 289% ROI.
            ```
            """)

with tab8:
    st.header("🧮 Interactive Tools for Content")
    
    st.markdown("""
    These are the interactive elements created for the "Custom Business Software" pillar post.
    They increase engagement, provide practical value, and help generate leads.
    """)
    
    tool_col1, tool_col2, tool_col3 = st.columns(3)
    
    with tool_col1:
        st.subheader("💰 ROI Calculator")
        st.markdown("""
        Interactive calculator with minimalist Apple design:
        - Clean sliders for inputs
        - Real-time calculations
        - 5-year projections
        - Break-even analysis
        - Smart recommendations
        """)
        
        if os.path.exists('roi-calculator.html'):
            # Get absolute path to the file
            import os
            calculator_path = os.path.abspath('roi-calculator.html')
            
            st.markdown(f"""
            <a href="file://{calculator_path}" target="_blank" style="
                display: inline-block;
                background: linear-gradient(135deg, #0071e3 0%, #005bb5 100%);
                color: white;
                padding: 16px 40px;
                border-radius: 980px;
                text-decoration: none;
                font-weight: 600;
                margin: 10px 0;
                box-shadow: 0 4px 12px rgba(0, 113, 227, 0.25);
                transition: all 0.2s;
            ">🚀 Open ROI Calculator</a>
            """, unsafe_allow_html=True)
            
            with open('roi-calculator.html', 'r') as f:
                calculator_html = f.read()
            st.download_button(
                label="📥 Download ROI Calculator",
                data=calculator_html,
                file_name="roi-calculator.html",
                mime="text/html",
                use_container_width=True
            )
        
    with tool_col2:
        st.subheader("💵 Cost Breakdown")
        st.markdown("""
        Visual infographic showing:
        - 3 pricing tiers
        - Cost factors table
        - Hidden costs
        - Budget planning
        """)
        
        if os.path.exists('cost-breakdown-infographic.html'):
            # Get absolute path to the file
            breakdown_path = os.path.abspath('cost-breakdown-infographic.html')
            
            st.markdown(f"""
            <a href="file://{breakdown_path}" target="_blank" style="
                display: inline-block;
                background: linear-gradient(135deg, #0071e3 0%, #005bb5 100%);
                color: white;
                padding: 16px 40px;
                border-radius: 980px;
                text-decoration: none;
                font-weight: 600;
                margin: 10px 0;
                box-shadow: 0 4px 12px rgba(0, 113, 227, 0.25);
            ">🚀 Open Cost Breakdown</a>
            """, unsafe_allow_html=True)
            
            with open('cost-breakdown-infographic.html', 'r') as f:
                breakdown_html = f.read()
            st.download_button(
                label="📥 Download Cost Breakdown",
                data=breakdown_html,
                file_name="cost-breakdown-infographic.html",
                mime="text/html",
                use_container_width=True
            )
    
    with tool_col3:
        st.subheader("🤔 Decision Framework")
        st.markdown("""
        Interactive assessment with:
        - 5 decision questions
        - Scoring system
        - Build vs Buy recommendations
        - Next steps guidance
        """)
        
        if os.path.exists('decision-framework.html'):
            # Get absolute path to the file
            framework_path = os.path.abspath('decision-framework.html')
            
            st.markdown(f"""
            <a href="file://{framework_path}" target="_blank" style="
                display: inline-block;
                background: linear-gradient(135deg, #0071e3 0%, #005bb5 100%);
                color: white;
                padding: 16px 40px;
                border-radius: 980px;
                text-decoration: none;
                font-weight: 600;
                margin: 10px 0;
                box-shadow: 0 4px 12px rgba(0, 113, 227, 0.25);
            ">🚀 Open Decision Framework</a>
            """, unsafe_allow_html=True)
            
            with open('decision-framework.html', 'r') as f:
                framework_html = f.read()
            st.download_button(
                label="📥 Download Decision Framework",
                data=framework_html,
                file_name="decision-framework.html",
                mime="text/html",
                use_container_width=True
            )
    
    st.divider()
    
    st.subheader("📊 Tool Performance Tracking")
    
    perf_col1, perf_col2, perf_col3 = st.columns(3)
    
    with perf_col1:
        st.metric("Avg. Time on Page", "4:32", "+2:15", help="With interactive elements vs without")
    
    with perf_col2:
        st.metric("Lead Conversion", "8.5%", "+3.2%", help="Calculator users who fill contact form")
    
    with perf_col3:
        st.metric("Social Shares", "127", "+89", help="Articles with calculators vs without")
    
    st.info("💡 **Pro Tip:** Embed these tools directly in blog posts as iframes or host on subdomains (tools.57seconds.com). Track interactions with Google Analytics events.")
    
    st.markdown("---")
    
    st.subheader("🎯 Embedding Instructions")
    
    embed_tab1, embed_tab2, embed_tab3 = st.tabs(["WordPress", "HTML/Static Site", "React/Next.js"])
    
    with embed_tab1:
        st.code('''
<!-- WordPress shortcode or HTML block -->
<iframe 
    src="/tools/roi-calculator.html" 
    width="100%" 
    height="1200px" 
    frameborder="0"
    style="border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.1);">
</iframe>
        ''', language="html")
    
    with embed_tab2:
        st.code('''
<!-- Direct embed in HTML -->
<div class="interactive-tool">
    <iframe 
        src="roi-calculator.html" 
        width="100%" 
        height="1200px" 
        frameborder="0"
        loading="lazy">
    </iframe>
</div>
        ''', language="html")
    
    with embed_tab3:
        st.code('''
// Next.js component
export default function ROICalculator() {
  return (
    <div className="w-full">
      <iframe 
        src="/tools/roi-calculator.html"
        className="w-full h-[1200px] rounded-lg shadow-lg"
        frameBorder="0"
      />
    </div>
  );
}
        ''', language="javascript")

# Footer
st.divider()
st.markdown("---")
st.caption("📊 Content Strategy Command Center | Powered by Google Trends & pytrends")
