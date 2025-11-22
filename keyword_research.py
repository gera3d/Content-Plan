#!/usr/bin/env python3
"""
Google Trends Keyword Research Tool
Pulls trending data and keyword insights using pytrends
"""

from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime
import json

class KeywordResearcher:
    def __init__(self):
        """Initialize pytrends connection"""
        self.pytrends = TrendReq(hl='en-US', tz=360)
    
    def get_interest_over_time(self, keywords, timeframe='today 12-m'):
        """
        Get search interest over time for given keywords
        
        Args:
            keywords: List of keywords (max 5 at a time)
            timeframe: Time period (e.g., 'today 12-m', 'today 3-m', 'now 7-d')
        """
        self.pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo='US', gprop='')
        interest_df = self.pytrends.interest_over_time()
        
        if not interest_df.empty:
            # Remove 'isPartial' column if it exists
            if 'isPartial' in interest_df.columns:
                interest_df = interest_df.drop(columns=['isPartial'])
        
        return interest_df
    
    def get_related_queries(self, keyword):
        """
        Get related queries for a keyword (rising and top)
        
        Args:
            keyword: Single keyword to analyze
        """
        self.pytrends.build_payload([keyword], cat=0, timeframe='today 12-m', geo='US', gprop='')
        related_queries = self.pytrends.related_queries()
        return related_queries[keyword]
    
    def get_trending_searches(self, country='united_states'):
        """
        Get current trending searches
        
        Args:
            country: Country code (e.g., 'united_states', 'united_kingdom')
        """
        trending_df = self.pytrends.trending_searches(pn=country)
        return trending_df
    
    def get_suggestions(self, keyword):
        """
        Get keyword suggestions from Google autocomplete
        
        Args:
            keyword: Keyword to get suggestions for
        """
        suggestions = self.pytrends.suggestions(keyword=keyword)
        return pd.DataFrame(suggestions)
    
    def analyze_keywords(self, keywords, timeframe='today 12-m'):
        """
        Complete keyword analysis with interest and related queries
        
        Args:
            keywords: List of keywords to analyze
            timeframe: Time period for analysis
        """
        results = {
            'timestamp': datetime.now().isoformat(),
            'keywords': keywords,
            'timeframe': timeframe,
            'interest_over_time': {},
            'related_queries': {}
        }
        
        # Get interest over time
        print(f"Analyzing interest over time for: {', '.join(keywords)}")
        interest_df = self.get_interest_over_time(keywords, timeframe)
        if not interest_df.empty:
            results['interest_over_time'] = interest_df.to_dict()
            print(f"✓ Found interest data for {len(interest_df)} time periods")
        
        # Get related queries for each keyword
        for keyword in keywords:
            print(f"\nFinding related queries for: {keyword}")
            related = self.get_related_queries(keyword)
            
            results['related_queries'][keyword] = {}
            
            if related['top'] is not None:
                results['related_queries'][keyword]['top'] = related['top'].to_dict()
                print(f"  ✓ Found {len(related['top'])} top related queries")
            
            if related['rising'] is not None:
                results['related_queries'][keyword]['rising'] = related['rising'].to_dict()
                print(f"  ✓ Found {len(related['rising'])} rising queries")
        
        return results
    
    def save_results(self, results, filename='keyword_results.json'):
        """Save results to JSON file"""
        # Convert any Timestamp keys to strings
        if 'interest_over_time' in results and results['interest_over_time']:
            clean_interest = {}
            for key, value in results['interest_over_time'].items():
                if isinstance(value, dict):
                    clean_interest[key] = {str(k): v for k, v in value.items()}
                else:
                    clean_interest[str(key)] = value
            results['interest_over_time'] = clean_interest
        
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        print(f"\n✓ Results saved to {filename}")


def main():
    """Example usage"""
    researcher = KeywordResearcher()
    
    # Example: Analyze keywords related to your business
    keywords = [
        'review management software',
        'customer feedback tools',
        'online reputation management'
    ]
    
    print("=" * 60)
    print("KEYWORD RESEARCH TOOL")
    print("=" * 60)
    
    # Analyze keywords
    results = researcher.analyze_keywords(keywords, timeframe='today 12-m')
    
    # Save results
    researcher.save_results(results)
    
    print("\n" + "=" * 60)
    print("Analysis complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
