#!/usr/bin/env python3
"""
Content Strategy Keyword Research
Customized for Gera Yeremin's business focus
"""

from keyword_research import KeywordResearcher
import pandas as pd

def analyze_business_keywords():
    """Analyze keywords related to your core services"""
    researcher = KeywordResearcher()
    
    print("\n" + "="*70)
    print("CONTENT STRATEGY - KEYWORD RESEARCH FOR GERA YEREMIN")
    print("="*70)
    
    # Define keyword categories based on your services
    keyword_categories = {
        'Review & Reputation': [
            'review management',
            'online reviews',
            'reputation management',
            'customer reviews',
            'Google reviews'
        ],
        'Custom Software': [
            'custom software development',
            'business applications',
            'software architecture'
        ],
        'Digital Marketing': [
            'digital marketing agency',
            'SEO services',
            'local SEO'
        ]
    }
    
    all_results = {}
    
    for category, keywords in keyword_categories.items():
        print(f"\n📊 Analyzing: {category}")
        print("-" * 70)
        
        # Analyze in batches of 5 (Google Trends limit)
        for i in range(0, len(keywords), 5):
            batch = keywords[i:i+5]
            print(f"\nBatch: {', '.join(batch)}")
            
            results = researcher.analyze_keywords(batch, timeframe='today 12-m')
            all_results[f"{category}_{i}"] = results
            
            # Brief pause to avoid rate limiting
            import time
            time.sleep(2)
    
    return all_results

def get_trending_topics():
    """Get current trending searches for content ideas"""
    researcher = KeywordResearcher()
    
    print("\n" + "="*70)
    print("CURRENT TRENDING SEARCHES")
    print("="*70)
    
    trending = researcher.get_trending_searches('united_states')
    print("\nTop 20 Trending Searches:")
    print(trending.head(20).to_string(index=False))
    
    return trending

def explore_keyword_suggestions(seed_keyword):
    """Get Google autocomplete suggestions for a keyword"""
    researcher = KeywordResearcher()
    
    print(f"\n📝 Keyword Suggestions for: '{seed_keyword}'")
    print("-" * 70)
    
    suggestions = researcher.get_suggestions(seed_keyword)
    if not suggestions.empty:
        print(suggestions.to_string(index=False))
    else:
        print("No suggestions found")
    
    return suggestions


if __name__ == "__main__":
    # Uncomment the analyses you want to run:
    
    # 1. Analyze your business keywords
    results = analyze_business_keywords()
    
    # 2. Check current trends
    # trending = get_trending_topics()
    
    # 3. Explore specific keyword ideas
    # explore_keyword_suggestions('review management')
    # explore_keyword_suggestions('customer feedback')
    
    print("\n✅ Analysis complete! Check keyword_results.json for detailed data.")
