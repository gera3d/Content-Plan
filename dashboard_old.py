"""
Content Strategy Command Center
Interactive dashboard for keyword research and content planning
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
    page_title="Content Strategy Command Center",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'researcher' not in st.session_state:
    st.session_state.researcher = KeywordResearcher()

# Header
st.markdown('<p class="main-header">📊 Content Strategy Command Center</p>', unsafe_allow_html=True)
st.markdown("**Gera Yeremin** | Digital Marketing & Software Architecture")
st.divider()

# Sidebar
with st.sidebar:
    st.header("⚙️ Control Panel")
    
    analysis_type = st.selectbox(
        "Analysis Type",
        ["Keyword Trends", "Related Queries", "Trending Searches", "Keyword Suggestions", "Saved Results"]
    )
    
    st.divider()
    
    if analysis_type in ["Keyword Trends", "Related Queries"]:
        st.subheader("Keywords")
        
        # Preset keyword categories
        preset = st.selectbox(
            "Preset Categories",
            ["Custom", "Review & Reputation", "Custom Software", "Digital Marketing", "All Services"]
        )
        
        if preset == "Review & Reputation":
            default_keywords = "review management, online reviews, reputation management"
        elif preset == "Custom Software":
            default_keywords = "custom software development, business applications"
        elif preset == "Digital Marketing":
            default_keywords = "digital marketing, SEO services, local SEO"
        elif preset == "All Services":
            default_keywords = "review management, custom software, digital marketing"
        else:
            default_keywords = ""
        
        keywords_input = st.text_area(
            "Enter keywords (comma-separated, max 5)",
            value=default_keywords,
            height=100
        )
        
        timeframe = st.selectbox(
            "Timeframe",
            ["today 7-d", "today 1-m", "today 3-m", "today 12-m", "today 5-y"],
            index=3
        )
        
        analyze_btn = st.button("🔍 Analyze Keywords", type="primary", use_container_width=True)
    
    elif analysis_type == "Trending Searches":
        country = st.selectbox(
            "Country",
            ["united_states", "united_kingdom", "canada", "australia"]
        )
        trending_btn = st.button("📈 Get Trends", type="primary", use_container_width=True)
    
    elif analysis_type == "Keyword Suggestions":
        seed_keyword = st.text_input("Seed Keyword", value="review management")
        suggest_btn = st.button("💡 Get Suggestions", type="primary", use_container_width=True)

# Main content area
if analysis_type == "Keyword Trends":
    st.header("📈 Keyword Interest Over Time")
    
    if 'analyze_btn' in locals() and analyze_btn:
        if keywords_input:
            keywords = [k.strip() for k in keywords_input.split(',') if k.strip()]
            
            if len(keywords) > 5:
                st.warning("⚠️ Maximum 5 keywords allowed. Using first 5.")
                keywords = keywords[:5]
            
            with st.spinner('Fetching data from Google Trends...'):
                try:
                    interest_df = st.session_state.researcher.get_interest_over_time(keywords, timeframe)
                    
                    if not interest_df.empty:
                        # Store in session state
                        st.session_state.current_data = interest_df
                        st.session_state.current_keywords = keywords
                        
                        # Metrics row
                        cols = st.columns(len(keywords))
                        for i, keyword in enumerate(keywords):
                            with cols[i]:
                                avg_interest = interest_df[keyword].mean()
                                max_interest = interest_df[keyword].max()
                                st.metric(
                                    label=keyword,
                                    value=f"{avg_interest:.1f}",
                                    delta=f"Peak: {max_interest}"
                                )
                        
                        st.divider()
                        
                        # Interactive line chart
                        fig = px.line(
                            interest_df,
                            x=interest_df.index,
                            y=keywords,
                            title=f"Search Interest: {timeframe}",
                            labels={'value': 'Interest (0-100)', 'variable': 'Keyword'},
                            template='plotly_white'
                        )
                        fig.update_layout(height=500, hovermode='x unified')
                        st.plotly_chart(fig, use_container_width=True)
                        
                        # Data table
                        with st.expander("📊 View Raw Data"):
                            st.dataframe(interest_df, use_container_width=True)
                        
                        # Download button
                        csv = interest_df.to_csv()
                        st.download_button(
                            label="📥 Download CSV",
                            data=csv,
                            file_name=f"keyword_trends_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                            mime="text/csv"
                        )
                    else:
                        st.warning("No data found for these keywords.")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.info("👆 Enter keywords in the sidebar to begin analysis")
    
    elif hasattr(st.session_state, 'current_data'):
        # Display cached data
        st.info("Showing cached results. Click 'Analyze Keywords' to refresh.")
        
        interest_df = st.session_state.current_data
        keywords = st.session_state.current_keywords
        
        # Metrics
        cols = st.columns(len(keywords))
        for i, keyword in enumerate(keywords):
            with cols[i]:
                avg_interest = interest_df[keyword].mean()
                max_interest = interest_df[keyword].max()
                st.metric(label=keyword, value=f"{avg_interest:.1f}", delta=f"Peak: {max_interest}")
        
        # Chart
        fig = px.line(interest_df, x=interest_df.index, y=keywords, template='plotly_white')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("👆 Enter keywords in the sidebar to begin analysis")

elif analysis_type == "Related Queries":
    st.header("🔗 Related Queries")
    
    if 'analyze_btn' in locals() and analyze_btn:
        if keywords_input:
            keywords = [k.strip() for k in keywords_input.split(',') if k.strip()]
            
            for keyword in keywords[:3]:  # Limit to 3 to avoid rate limiting
                st.subheader(f"📌 {keyword}")
                
                with st.spinner(f'Analyzing "{keyword}"...'):
                    try:
                        related = st.session_state.researcher.get_related_queries(keyword)
                        
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.markdown("**🔥 Rising Queries**")
                            if related['rising'] is not None and not related['rising'].empty:
                                rising_df = related['rising'].reset_index(drop=True)
                                st.dataframe(rising_df, use_container_width=True, hide_index=True)
                            else:
                                st.info("No rising queries found")
                        
                        with col2:
                            st.markdown("**⭐ Top Queries**")
                            if related['top'] is not None and not related['top'].empty:
                                top_df = related['top'].reset_index(drop=True)
                                st.dataframe(top_df, use_container_width=True, hide_index=True)
                            else:
                                st.info("No top queries found")
                        
                        st.divider()
                    except Exception as e:
                        st.error(f"Error analyzing '{keyword}': {str(e)}")
        else:
            st.info("👆 Enter keywords in the sidebar")
    else:
        st.info("👆 Enter keywords in the sidebar and click 'Analyze'")

elif analysis_type == "Trending Searches":
    st.header("🌟 Trending Searches")
    
    if 'trending_btn' in locals() and trending_btn:
        with st.spinner('Fetching trending searches...'):
            try:
                trending = st.session_state.researcher.get_trending_searches(country)
                
                st.success(f"✅ Found {len(trending)} trending searches")
                
                # Display in columns
                col1, col2 = st.columns(2)
                
                mid = len(trending) // 2
                
                with col1:
                    st.markdown("**Top Trending (1-10)**")
                    for i, trend in enumerate(trending[0:10].values, 1):
                        st.write(f"{i}. {trend[0]}")
                
                with col2:
                    st.markdown("**Top Trending (11-20)**")
                    for i, trend in enumerate(trending[10:20].values, 11):
                        st.write(f"{i}. {trend[0]}")
                
                # Full table
                with st.expander("📋 View All Trends"):
                    st.dataframe(trending, use_container_width=True, hide_index=True)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.info("👆 Click 'Get Trends' in the sidebar")

elif analysis_type == "Keyword Suggestions":
    st.header("💡 Keyword Suggestions")
    
    if 'suggest_btn' in locals() and suggest_btn:
        if seed_keyword:
            with st.spinner(f'Getting suggestions for "{seed_keyword}"...'):
                try:
                    suggestions = st.session_state.researcher.get_suggestions(seed_keyword)
                    
                    if not suggestions.empty:
                        st.success(f"✅ Found {len(suggestions)} suggestions")
                        st.dataframe(suggestions, use_container_width=True, hide_index=True)
                    else:
                        st.warning("No suggestions found")
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    else:
        st.info("👆 Enter a seed keyword and click 'Get Suggestions'")

elif analysis_type == "Saved Results":
    st.header("💾 Saved Analysis Results")
    
    # Look for JSON files
    json_files = [f for f in os.listdir('.') if f.endswith('.json') and 'keyword' in f.lower()]
    
    if json_files:
        selected_file = st.selectbox("Select saved results", json_files)
        
        if selected_file:
            with open(selected_file, 'r') as f:
                data = json.load(f)
            
            st.json(data)
            
            with open(selected_file, 'r') as f:
                st.download_button(
                    label="📥 Download JSON",
                    data=f.read(),
                    file_name=selected_file,
                    mime="application/json"
                )
    else:
        st.info("No saved results found. Run an analysis to generate data.")

# Footer
st.divider()
st.markdown("---")
st.caption(f"Last updated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}")
