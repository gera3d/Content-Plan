"""
Content Adaptation Engine
Transforms long-form content for different platforms with specific formatting rules
"""

from typing import Dict, List, Optional
import re


class ContentAdapter:
    """Adapts content for different distribution platforms"""
    
    def __init__(self):
        self.platform_limits = {
            "twitter": 280,
            "linkedin_post": 1300,
            "linkedin_article": 10000,
            "medium": 50000,
            "devto": 50000,
            "reddit": 10000,
            "quora": 5000
        }
    
    def adapt_for_medium(self, content: Dict) -> Dict:
        """
        Adapt content for Medium with canonical link
        
        Args:
            content: Original content object
            
        Returns:
            Adapted content with Medium-specific formatting
        """
        canonical_url = content.get("canonical_url", "")
        
        # Medium-specific formatting
        adapted_content = f"""
> **Note:** This article was originally published at [{canonical_url}]({canonical_url})

{content['content_long']}

---

*Originally published at [{content.get('author', 'our website')}]({canonical_url})*
"""
        
        return {
            "title": content["title"],
            "content": adapted_content,
            "tags": content.get("tags", [])[:5],  # Medium allows max 5 tags
            "canonical_url": canonical_url,
            "publish_status": "public"
        }
    
    def adapt_for_devto(self, content: Dict) -> Dict:
        """
        Adapt content for Dev.to with frontmatter canonical
        
        Args:
            content: Original content object
            
        Returns:
            Adapted content with Dev.to frontmatter
        """
        canonical_url = content.get("canonical_url", "")
        tags = content.get("tags", [])[:4]  # Dev.to allows max 4 tags
        
        frontmatter = f"""---
title: {content['title']}
published: true
description: {content['meta_description']}
tags: {', '.join(tags)}
canonical_url: {canonical_url}
---

"""
        
        adapted_content = frontmatter + content['content_long']
        
        return {
            "title": content["title"],
            "content": adapted_content,
            "tags": tags
        }
    
    def adapt_for_linkedin_article(self, content: Dict) -> Dict:
        """
        Adapt content for LinkedIn Article (1000-2000 words)
        
        Args:
            content: Original content object
            
        Returns:
            Adapted content for LinkedIn
        """
        canonical_url = content.get("canonical_url", "")
        
        # Shorten if needed (target ~2000 words)
        shortened_content = self._shorten_content(
            content['content_long'],
            target_words=2000
        )
        
        # Add professional tone and canonical reference
        adapted_content = f"""{shortened_content}

---

**Want to learn more?** Read the full article with examples and case studies at [{content.get('author', 'our website')}]({canonical_url})

**About the Author:** {content.get('author', 'Gera Yeremin')} - Software Developer & Digital Marketing Strategist specializing in custom business applications.
"""
        
        return {
            "title": content["title"],
            "content": adapted_content,
            "visibility": "PUBLIC"
        }
    
    def adapt_for_linkedin_post(self, content: Dict) -> Dict:
        """
        Adapt content for LinkedIn Post (1300 characters max)
        Creates an engaging hook + key points + CTA format
        
        Args:
            content: Original content object
            
        Returns:
            Adapted short-form post
        """
        canonical_url = content.get("canonical_url", "")
        
        # Extract hook from first paragraph
        lines = content['content_long'].split('\n')
        hook = ""
        for line in lines:
            clean_line = re.sub(r'[#*`]', '', line).strip()
            if len(clean_line) > 50:
                hook = clean_line[:200]
                break
        
        # Create engaging LinkedIn post
        post = f"""🚀 {hook}

Here's what you need to know:

✅ {self._extract_key_point(content['content_long'], 1)}
✅ {self._extract_key_point(content['content_long'], 2)}
✅ {self._extract_key_point(content['content_long'], 3)}

💡 Want the full breakdown?
Read the complete guide: {canonical_url}

{' '.join(['#' + tag.replace(' ', '') for tag in content.get('tags', [])[:5]])}
"""
        
        # Ensure it fits within 1300 characters
        if len(post) > 1300:
            post = post[:1280] + f"...\n\nRead more: {canonical_url}"
        
        return {
            "content": post,
            "visibility": "PUBLIC"
        }
    
    def adapt_for_twitter_thread(self, content: Dict) -> List[str]:
        """
        Adapt content for Twitter thread (280 chars per tweet)
        
        Args:
            content: Original content object
            
        Returns:
            List of tweets forming a thread
        """
        canonical_url = content.get("canonical_url", "")
        
        tweets = []
        
        # Tweet 1: Hook
        hook = f"🧵 {content['title']}\n\nA thread 👇"
        tweets.append(hook[:280])
        
        # Extract key points from content
        key_points = self._extract_all_key_points(content['content_long'], max_points=8)
        
        # Tweet 2-9: Key points
        for i, point in enumerate(key_points, 1):
            tweet = f"{i}/ {point}"
            if len(tweet) > 280:
                tweet = tweet[:275] + "..."
            tweets.append(tweet)
        
        # Final tweet: CTA
        final_tweet = f"Want the full breakdown with examples and case studies?\n\nRead the complete article:\n{canonical_url}"
        tweets.append(final_tweet[:280])
        
        return tweets
    
    def adapt_for_reddit(self, content: Dict, subreddit: str = "entrepreneur") -> Dict:
        """
        Adapt content for Reddit (value-first, no promotion in title)
        
        Args:
            content: Original content object
            subreddit: Target subreddit (affects tone)
            
        Returns:
            Adapted Reddit post
        """
        canonical_url = content.get("canonical_url", "")
        
        # Make title value-focused, not promotional
        reddit_title = self._make_reddit_friendly_title(content['title'])
        
        # Shorten content (500-1500 words ideal for Reddit)
        shortened = self._shorten_content(content['content_long'], target_words=1000)
        
        # Add context and value disclaimer
        reddit_post = f"""{shortened}

---

*I've been working in custom software development and wanted to share what I've learned. Happy to answer questions in the comments.*

*Full article with more examples: {canonical_url}*
"""
        
        return {
            "title": reddit_title,
            "content": reddit_post,
            "subreddit": subreddit,
            "note": "Remember to engage in comments and provide value!"
        }
    
    def adapt_for_quora(self, content: Dict, question: str) -> Dict:
        """
        Adapt content for Quora answer format
        
        Args:
            content: Original content object
            question: The Quora question being answered
            
        Returns:
            Adapted Quora answer
        """
        canonical_url = content.get("canonical_url", "")
        
        # Format as answer to question
        answer = f"""**Short answer:** {content['content_summary']}

**Detailed explanation:**

{self._shorten_content(content['content_long'], target_words=800)}

**Key takeaways:**
{self._create_bullet_summary(content['content_long'])}

---

I've written a comprehensive guide on this topic with real examples and case studies. You can [read the full article here]({canonical_url}).

*{content.get('author', 'Gera Yeremin')} - Software Developer & Digital Marketing Strategist*
"""
        
        return {
            "question": question,
            "answer": answer
        }
    
    def adapt_for_substack(self, content: Dict) -> Dict:
        """
        Adapt content for Substack newsletter format
        
        Args:
            content: Original content object
            
        Returns:
            Adapted Substack content
        """
        canonical_url = content.get("canonical_url", "")
        
        # Newsletter-friendly format
        newsletter = f"""Hi there,

{content['content_summary']}

{self._shorten_content(content['content_long'], target_words=1500)}

**Want more details?** [Read the full article on my blog]({canonical_url}) for additional examples, case studies, and actionable templates.

---

Thanks for reading! If you found this helpful, share it with someone who might benefit.

Best,
{content.get('author', 'Gera')}
"""
        
        return {
            "subject": content['title'],
            "content": newsletter,
            "type": "newsletter"
        }
    
    def adapt_for_youtube_description(self, content: Dict) -> Dict:
        """
        Create YouTube video description from content
        
        Args:
            content: Original content object
            
        Returns:
            YouTube description and suggested script outline
        """
        canonical_url = content.get("canonical_url", "")
        
        description = f"""{content['meta_description']}

🔗 Full Article: {canonical_url}

📌 TIMESTAMPS
0:00 - Introduction
0:30 - {self._extract_key_point(content['content_long'], 1)}
2:00 - {self._extract_key_point(content['content_long'], 2)}
4:00 - {self._extract_key_point(content['content_long'], 3)}
6:00 - Key Takeaways

🔗 RESOURCES
Full article with examples: {canonical_url}

📬 CONNECT
Website: 57seconds.com

{' '.join(['#' + tag.replace(' ', '') for tag in content.get('tags', [])[:10]])}
"""
        
        return {
            "title": content['title'],
            "description": description,
            "script_outline": self._create_video_script_outline(content)
        }
    
    # Helper methods
    
    def _shorten_content(self, content: str, target_words: int) -> str:
        """Intelligently shorten content to target word count"""
        words = content.split()
        if len(words) <= target_words:
            return content
        
        # Try to find a natural break point near target
        shortened = ' '.join(words[:target_words])
        
        # Find last complete sentence
        last_period = shortened.rfind('.')
        if last_period > len(shortened) * 0.8:  # If close to end
            return shortened[:last_period + 1]
        
        return shortened + "..."
    
    def _extract_key_point(self, content: str, point_number: int) -> str:
        """Extract a key point from content"""
        # Simple extraction - look for numbered lists or headers
        lines = content.split('\n')
        points_found = 0
        
        for line in lines:
            # Check for numbered lists or key indicators
            if re.match(r'^\d+\.|\*\*\d+\.|##', line.strip()):
                points_found += 1
                if points_found == point_number:
                    clean = re.sub(r'[#*\d\.]', '', line).strip()
                    return clean[:100] if len(clean) > 100 else clean
        
        # Fallback: extract sentences
        sentences = [s.strip() for s in re.split(r'[.!?]', content) if len(s.strip()) > 30]
        if point_number <= len(sentences):
            return sentences[point_number - 1][:100]
        
        return "Key insight from the article"
    
    def _extract_all_key_points(self, content: str, max_points: int = 8) -> List[str]:
        """Extract multiple key points from content"""
        points = []
        for i in range(1, max_points + 1):
            point = self._extract_key_point(content, i)
            if point and point not in points:
                points.append(point)
        return points
    
    def _make_reddit_friendly_title(self, title: str) -> str:
        """Convert promotional title to value-focused Reddit title"""
        # Remove promotional words
        reddit_title = re.sub(r'Complete Guide|The Ultimate|Best|Top', '', title)
        
        # Make it question or learning-focused
        if ":" in reddit_title:
            reddit_title = reddit_title.split(':')[0]
        
        # Add context prefix if needed
        if not reddit_title.startswith(('How ', 'Why ', 'What ', 'I ')):
            reddit_title = f"What I learned about {reddit_title}"
        
        return reddit_title.strip()
    
    def _create_bullet_summary(self, content: str, num_bullets: int = 3) -> str:
        """Create bullet point summary"""
        key_points = self._extract_all_key_points(content, max_points=num_bullets)
        return '\n'.join([f"• {point}" for point in key_points])
    
    def _create_video_script_outline(self, content: Dict) -> str:
        """Create basic video script outline"""
        return f"""
VIDEO SCRIPT OUTLINE

Introduction (0:00-0:30)
- Hook: {content['title']}
- Why this matters
- What we'll cover

{self._create_bullet_summary(content['content_long'], num_bullets=5)}

Conclusion (6:00-7:00)
- Recap key points
- CTA: Link in description
- Ask for engagement
"""


if __name__ == "__main__":
    # Example usage
    adapter = ContentAdapter()
    
    sample_content = {
        "title": "Custom Business Software: The Complete Guide",
        "content_long": """
# Custom Business Software: The Complete Guide

Your team is drowning in spreadsheets. What if there was another way?

## 1. What is Custom Business Software

Custom software is built specifically for your business needs.

## 2. Why Choose Custom

You get exactly what you need, not what everyone else uses.

## 3. Cost Considerations

Typically $15,000 - $150,000 depending on complexity.
""",
        "content_summary": "Learn when custom business software makes sense and how to decide between building custom vs buying off-the-shelf solutions.",
        "meta_description": "Complete guide to custom business software for SMBs. Learn costs, benefits, and when to build vs buy.",
        "tags": ["custom software", "business", "ROI", "software development"],
        "canonical_url": "https://57seconds.com/custom-business-software-guide",
        "author": "Gera Yeremin"
    }
    
    print("=== LINKEDIN POST ===")
    linkedin_post = adapter.adapt_for_linkedin_post(sample_content)
    print(linkedin_post['content'])
    
    print("\n=== TWITTER THREAD ===")
    twitter_thread = adapter.adapt_for_twitter_thread(sample_content)
    for i, tweet in enumerate(twitter_thread, 1):
        print(f"Tweet {i}: {tweet}\n")
