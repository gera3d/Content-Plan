# Keyword Research Tools - README

## Setup Complete! ✅

You now have Google Trends keyword research tools set up and working.

## Files Created

1. **keyword_research.py** - Main keyword research library
2. **analyze_content_keywords.py** - Customized for your business
3. **keyword_results.json** - Output from your first test run

## How to Use

### Quick Start
```bash
python3 analyze_content_keywords.py
```

### What It Does

The tool analyzes keywords in three categories based on your business:

1. **Review & Reputation**
   - review management
   - online reviews
   - reputation management
   - customer reviews
   - Google reviews

2. **Custom Software**
   - custom software development
   - business applications
   - software architecture

3. **Digital Marketing**
   - digital marketing agency
   - SEO services
   - local SEO

### Available Functions

**Analyze Business Keywords**
```python
from keyword_research import KeywordResearcher
researcher = KeywordResearcher()

# Get interest over time
results = researcher.analyze_keywords(['review management', 'online reviews'])
```

**Get Trending Searches**
```python
trending = researcher.get_trending_searches('united_states')
```

**Get Keyword Suggestions**
```python
suggestions = researcher.get_suggestions('review management')
```

**Get Related Queries**
```python
related = researcher.get_related_queries('online reputation')
```

## Customization

Edit `analyze_content_keywords.py` to:
- Change keyword lists
- Adjust timeframe (e.g., 'today 3-m', 'today 5-y')
- Add new keyword categories
- Modify analysis parameters

## Output

Results are saved to `keyword_results.json` with:
- Interest over time data
- Related queries (top and rising)
- Timestamp of analysis
- All keywords analyzed

## Next Steps for Content Strategy

Use this data to:
1. Identify trending topics in your industry
2. Find related keywords people are searching
3. Discover rising search terms
4. Plan content around high-interest topics
5. Optimize existing content for popular searches

## Rate Limits

Google Trends has rate limits. The script includes:
- 2-second delays between batches
- Max 5 keywords per request
- Automatic error handling

If you get rate limited, wait a few minutes before running again.
