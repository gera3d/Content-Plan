"""
Content Management System for Publishing & Syndication
Handles content creation, storage, versioning, and metadata management
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional
import uuid
from pathlib import Path


class ContentManager:
    """Manages content creation, storage, and retrieval"""
    
    def __init__(self, base_dir: str = "content_data"):
        self.base_dir = Path(base_dir)
        self.drafts_dir = self.base_dir / "drafts"
        self.published_dir = self.base_dir / "published"
        self.images_dir = self.base_dir / "images"
        self.templates_dir = self.base_dir / "templates"
        
        # Create directories if they don't exist
        for directory in [self.drafts_dir, self.published_dir, self.images_dir, self.templates_dir]:
            directory.mkdir(parents=True, exist_ok=True)
    
    def create_content(
        self,
        title: str,
        content_long: str,
        keywords: List[str],
        category: str,
        meta_description: Optional[str] = None,
        tags: Optional[List[str]] = None,
        author: str = "Gera Yeremin"
    ) -> Dict:
        """
        Create new content with metadata
        
        Args:
            title: Content title
            content_long: Full long-form content (markdown or HTML)
            keywords: List of SEO keywords
            category: Content category
            meta_description: SEO meta description (auto-generated if not provided)
            tags: Content tags
            author: Author name
            
        Returns:
            Content object with metadata
        """
        content_id = str(uuid.uuid4())
        slug = self._generate_slug(title)
        
        # Auto-generate meta description if not provided
        if not meta_description:
            meta_description = self._generate_meta_description(content_long)
        
        # Auto-generate summary
        content_summary = self._generate_summary(content_long)
        
        content = {
            "content_id": content_id,
            "title": title,
            "slug": slug,
            "content_long": content_long,
            "content_summary": content_summary,
            "meta_description": meta_description,
            "keywords": keywords,
            "tags": tags or [],
            "category": category,
            "author": author,
            "created_date": datetime.now().isoformat(),
            "modified_date": datetime.now().isoformat(),
            "published_date": None,
            "status": "draft",
            "canonical_url": None,
            "syndication_status": {},
            "analytics": {
                "total_views": 0,
                "total_engagements": 0,
                "platform_performance": {}
            }
        }
        
        # Save as draft
        self._save_content(content, is_draft=True)
        
        return content
    
    def update_content(self, content_id: str, updates: Dict) -> Dict:
        """
        Update existing content
        
        Args:
            content_id: ID of content to update
            updates: Dictionary of fields to update
            
        Returns:
            Updated content object
        """
        content = self.get_content(content_id)
        
        if not content:
            raise ValueError(f"Content with ID {content_id} not found")
        
        # Update fields
        for key, value in updates.items():
            if key in content and key not in ["content_id", "created_date"]:
                content[key] = value
        
        # Update modified date
        content["modified_date"] = datetime.now().isoformat()
        
        # Re-generate slug if title changed
        if "title" in updates:
            content["slug"] = self._generate_slug(updates["title"])
        
        # Re-generate summary if content changed
        if "content_long" in updates:
            content["content_summary"] = self._generate_summary(updates["content_long"])
        
        # Save updated content
        is_draft = content["status"] == "draft"
        self._save_content(content, is_draft=is_draft)
        
        return content
    
    def publish_content(self, content_id: str, canonical_url: str) -> Dict:
        """
        Mark content as published and move to published directory
        
        Args:
            content_id: ID of content to publish
            canonical_url: The canonical URL where content is published
            
        Returns:
            Published content object
        """
        content = self.get_content(content_id)
        
        if not content:
            raise ValueError(f"Content with ID {content_id} not found")
        
        content["status"] = "published"
        content["published_date"] = datetime.now().isoformat()
        content["canonical_url"] = canonical_url
        
        # Move from drafts to published
        draft_path = self.drafts_dir / f"{content_id}.json"
        if draft_path.exists():
            draft_path.unlink()
        
        self._save_content(content, is_draft=False)
        
        return content
    
    def get_content(self, content_id: str) -> Optional[Dict]:
        """
        Retrieve content by ID
        
        Args:
            content_id: Content ID
            
        Returns:
            Content object or None if not found
        """
        # Check published first
        published_path = self.published_dir / f"{content_id}.json"
        if published_path.exists():
            with open(published_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        # Check drafts
        draft_path = self.drafts_dir / f"{content_id}.json"
        if draft_path.exists():
            with open(draft_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        
        return None
    
    def list_content(self, status: Optional[str] = None) -> List[Dict]:
        """
        List all content, optionally filtered by status
        
        Args:
            status: Filter by status ("draft" or "published"), or None for all
            
        Returns:
            List of content objects
        """
        content_list = []
        
        if status is None or status == "draft":
            for file_path in self.drafts_dir.glob("*.json"):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content_list.append(json.load(f))
        
        if status is None or status == "published":
            for file_path in self.published_dir.glob("*.json"):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content_list.append(json.load(f))
        
        # Sort by modified date (newest first)
        content_list.sort(key=lambda x: x["modified_date"], reverse=True)
        
        return content_list
    
    def delete_content(self, content_id: str) -> bool:
        """
        Delete content by ID
        
        Args:
            content_id: Content ID to delete
            
        Returns:
            True if deleted, False if not found
        """
        published_path = self.published_dir / f"{content_id}.json"
        draft_path = self.drafts_dir / f"{content_id}.json"
        
        deleted = False
        
        if published_path.exists():
            published_path.unlink()
            deleted = True
        
        if draft_path.exists():
            draft_path.unlink()
            deleted = True
        
        # Delete associated images directory
        images_path = self.images_dir / content_id
        if images_path.exists():
            import shutil
            shutil.rmtree(images_path)
        
        return deleted
    
    def update_syndication_status(
        self,
        content_id: str,
        platform: str,
        status: str,
        url: Optional[str] = None,
        error: Optional[str] = None
    ) -> Dict:
        """
        Update syndication status for a specific platform
        
        Args:
            content_id: Content ID
            platform: Platform name (e.g., "medium", "linkedin")
            status: Status ("pending", "published", "failed")
            url: Published URL on platform
            error: Error message if failed
            
        Returns:
            Updated content object
        """
        content = self.get_content(content_id)
        
        if not content:
            raise ValueError(f"Content with ID {content_id} not found")
        
        content["syndication_status"][platform] = {
            "status": status,
            "url": url,
            "date": datetime.now().isoformat(),
            "error": error
        }
        
        is_draft = content["status"] == "draft"
        self._save_content(content, is_draft=is_draft)
        
        return content
    
    def _save_content(self, content: Dict, is_draft: bool = True):
        """Save content to appropriate directory"""
        target_dir = self.drafts_dir if is_draft else self.published_dir
        file_path = target_dir / f"{content['content_id']}.json"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=2, ensure_ascii=False)
    
    def _generate_slug(self, title: str) -> str:
        """Generate URL-friendly slug from title"""
        import re
        
        # Convert to lowercase
        slug = title.lower()
        
        # Replace spaces and special chars with hyphens
        slug = re.sub(r'[^\w\s-]', '', slug)
        slug = re.sub(r'[\s_]+', '-', slug)
        slug = re.sub(r'^-+|-+$', '', slug)
        
        return slug
    
    def _generate_meta_description(self, content: str, max_length: int = 155) -> str:
        """
        Auto-generate meta description from content
        
        Args:
            content: Full content text
            max_length: Maximum length for meta description
            
        Returns:
            Meta description string
        """
        # Remove markdown/HTML formatting
        import re
        clean_content = re.sub(r'[#*`\[\]()<>]', '', content)
        
        # Get first paragraph or first max_length characters
        lines = clean_content.strip().split('\n')
        
        for line in lines:
            line = line.strip()
            if len(line) > 50:  # Skip very short lines
                if len(line) <= max_length:
                    return line
                else:
                    # Truncate at word boundary
                    truncated = line[:max_length].rsplit(' ', 1)[0]
                    return truncated + "..."
        
        # Fallback: just truncate
        return clean_content[:max_length].rsplit(' ', 1)[0] + "..."
    
    def _generate_summary(self, content: str, max_sentences: int = 3) -> str:
        """
        Auto-generate summary from content
        
        Args:
            content: Full content text
            max_sentences: Number of sentences to include
            
        Returns:
            Summary string
        """
        import re
        
        # Remove markdown/HTML formatting
        clean_content = re.sub(r'[#*`\[\]()<>]', '', content)
        
        # Split into sentences
        sentences = re.split(r'[.!?]+', clean_content)
        
        # Get first few meaningful sentences
        summary_sentences = []
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) > 30:  # Skip very short sentences
                summary_sentences.append(sentence)
                if len(summary_sentences) >= max_sentences:
                    break
        
        return '. '.join(summary_sentences) + '.'
    
    def get_stats(self) -> Dict:
        """Get content statistics"""
        drafts = self.list_content(status="draft")
        published = self.list_content(status="published")
        
        return {
            "total_content": len(drafts) + len(published),
            "drafts": len(drafts),
            "published": len(published),
            "total_views": sum(c.get("analytics", {}).get("total_views", 0) for c in published),
            "categories": self._get_category_breakdown(drafts + published)
        }
    
    def _get_category_breakdown(self, content_list: List[Dict]) -> Dict:
        """Get breakdown of content by category"""
        categories = {}
        for content in content_list:
            category = content.get("category", "Uncategorized")
            categories[category] = categories.get(category, 0) + 1
        return categories


if __name__ == "__main__":
    # Example usage
    manager = ContentManager()
    
    # Create sample content
    content = manager.create_content(
        title="Custom Business Software: The Complete Guide",
        content_long="""
        # Custom Business Software: The Complete Guide
        
        Your team is drowning in spreadsheets. Sales data lives in one system. 
        Customer info in another. Your unique workflow? It's held together with 
        duct tape, manual processes, and prayers.
        
        Sound familiar? What if there was another way?
        
        Custom business software might be the answer. But it's a significant 
        investment, and you need to know if it's right for your business.
        """,
        keywords=["custom business software", "business applications", "software development"],
        category="Software Development",
        tags=["custom software", "business", "ROI"]
    )
    
    print(f"Created content: {content['title']}")
    print(f"Content ID: {content['content_id']}")
    print(f"Slug: {content['slug']}")
    print(f"Summary: {content['content_summary']}")
    print(f"Meta Description: {content['meta_description']}")
