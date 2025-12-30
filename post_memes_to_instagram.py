#!/usr/bin/env python3
"""
Post memes from Contentful to Instagram via Ayrshare.
Schedules all memes on a 2-day cadence at 12pm PT.
"""

import os
import json
import requests
from datetime import datetime, timedelta
from typing import Optional

# ============================================================================
# CONFIGURATION
# ============================================================================

# Contentful
CONTENTFUL_SPACE_ID = "oa9mphdwsgvp"
CONTENTFUL_ENVIRONMENT = "master"
CONTENTFUL_DELIVERY_TOKEN = os.getenv("CONTENTFUL_DELIVERY_TOKEN", "")

# Ayrshare
AYRSHARE_API_KEY = os.getenv("AYRSHARE_API_KEY", "27958FC8-7A0F4D14-916AEDF1-C96C4E0A")

# Posting config
POST_INTERVAL_DAYS = 2
POST_HOUR = 12  # 12pm PT
POST_MINUTE = 0

# Hashtags
HASHTAGS = "#customsoftware #automation #smallbusiness #techhumor #nocode #entrepreneur #businesstips"

# ============================================================================
# CAPTION TEMPLATES (Gera's Voice)
# ============================================================================

CAPTION_TEMPLATES = {
    # Excel/Spreadsheet memes
    "morpheus-excel": "What if I told you... your Excel 'database' isn't a database. Sound familiar?",
    "disaster-spreadsheet": "Your business is on fire. Your spreadsheet? Also on fire. Sometimes that's just how it is.",
    "excel-fine": "This is fine. 🔥 Your 47-tab spreadsheet is definitely fine.",
    "pigeon-database": "Is this a database? No. No it's not. It's a spreadsheet pretending to be one.",
    
    # Automation memes
    "fry-automation": "Not sure if I should automate this... or spend 10x longer doing it manually forever.",
    "buzz-integrations": "Integrations. Integrations everywhere. And none of them talk to each other.",
    "rollsafe-data": "Can't lose your data if you never organize it in the first place. Wait—",
    "oprah-workaround": "You get a workaround! And YOU get a workaround! Everyone gets workarounds!",
    
    # Development/Tech memes
    "kermit-push-to-prod": "Me: I should test this first. Also me: Push to prod, it's fine.",
    "dwight-dev": "False. That's not how databases work. —Every developer, constantly.",
    "harold-timeline": "Client: 'Can we add just one more feature?' Me: *hide the pain*",
    "batman-slap": "But we've always done it this way— *slap* That's not a reason.",
    
    # Business/ROI memes
    "stonks-efficiency": "When your custom software actually works and saves you money. Stonks. 📈",
    "success-roi": "Built custom software. Actually got ROI. Nothing can stop me now.",
    "leo-cheers": "Here's to everyone who finally ditched their spreadsheet 'systems.' Cheers. 🥂",
    "gru-plan": "Step 1: Buy off-the-shelf software. Step 2: Customize it. Step 3: It doesn't work. Step 4: It doesn't work.",
    
    # Process memes
    "simple-process": "One does not simply... 'just export it to Excel.' Trust me on this one.",
    "mocking-spongebob": "'wE jUsT nEeD a SiMpLe DaTaBaSe' —Famous last words.",
    "panik-kalm": "Spreadsheet crashes. PANIK. You have a backup. KALM. It's from 2019. PANIK.",
    "wonka-enterprise": "Oh, you want enterprise software pricing? Tell me more about your 'unlimited budget.'",
    
    # Workflow automation memes
    "afraid-zap-failed": "I don't know why my Zap failed. I don't know why any of my Zaps fail.",
    "astronaut-polling": "Wait, it's all polling delays? Always has been. 🔫",
    "boat-buy-custom": "I should buy custom automation. —Every business owner at 2am.",
    "both-hybrid": "Why not both? Build custom AND use some SaaS. There's no wrong answer here.",
    "captain-owner": "Look at me. I am the platform owner now.",
    "cmm-automation": "$500/month for automation? You should probably just own that.",
    "db-distracted": "Me: Focus on the task. Also me: *distracted by custom automation possibilities*",
    "drake-own-vs-rent": "Renting software forever ❌ Owning your own tools ✅",
    "exit-build-custom": "EXIT: Build something custom. Me: Don't mind if I do.",
    "gandalf-zaps": "I have no memory of this Zap. Or why I built it. Or what it does.",
    "happening-deployed": "It's happening! It's actually deployed and working!",
    "inigo-simple": "You keep using that word 'simple.' I do not think it means what you think it means.",
    "pooh-own-engine": "Using Zapier: Fine. Owning your own automation engine: *distinguished*",
    "ski-polling": "If you rely on polling for real-time data... you're gonna have a bad time.",
    "wddth-hipaa": "Store patient data in a spreadsheet? We don't do that here.",
    
    # Other memes
    "brain-evolution": "Galaxy brain: Build exactly what you need. No compromises.",
    "drake-build": "Buying software that 'almost' works ❌ Building exactly what you need ✅",
    "exit-custom": "Every business owner eventually: 'What if we just... built our own?'",
    "fry-roi": "Take my money. Seriously. Just make the software work.",
    "galaxy-brain-software": "Small brain: Use Excel. Galaxy brain: Build custom software that actually scales.",
    "patrick-push": "Is this a production database? *pushes untested changes*",
    "ackabar-trap": "Enterprise pricing? IT'S A TRAP!",
}

DEFAULT_CAPTION = "When your software actually does what you need. What a concept."


# ============================================================================
# CONTENTFUL API
# ============================================================================

def fetch_memes_from_contentful() -> list:
    """Fetch all memePost entries from Contentful Delivery API."""
    base_url = f"https://cdn.contentful.com/spaces/{CONTENTFUL_SPACE_ID}/environments/{CONTENTFUL_ENVIRONMENT}"
    
    if not CONTENTFUL_DELIVERY_TOKEN:
        print("⚠️  No Contentful token - using local meme list")
        return get_local_meme_list()
    
    headers = {"Authorization": f"Bearer {CONTENTFUL_DELIVERY_TOKEN}"}
    
    response = requests.get(
        f"{base_url}/entries",
        headers=headers,
        params={"content_type": "memePost", "limit": 100, "include": 1}
    )
    
    if response.status_code != 200:
        print(f"⚠️  Contentful API error {response.status_code} - using local list")
        return get_local_meme_list()
    
    data = response.json()
    assets = {a["sys"]["id"]: a for a in data.get("includes", {}).get("Asset", [])}
    
    memes = []
    for entry in data.get("items", []):
        fields = entry.get("fields", {})
        image_ref = fields.get("image", {}).get("sys", {}).get("id")
        
        if image_ref and image_ref in assets:
            asset = assets[image_ref]
            file_info = asset.get("fields", {}).get("file", {})
            memes.append({
                "id": entry["sys"]["id"],
                "title": fields.get("title", "Untitled"),
                "filename": file_info.get("fileName", ""),
                "image_url": "https:" + file_info.get("url", "")
            })
    
    return memes


def get_local_meme_list() -> list:
    """Fallback local meme list."""
    meme_files = [
        "meme-ackabar-trap.png", "meme-afraid-zap-failed.png", "meme-astronaut-polling.png",
        "meme-batman-slap.png", "meme-boat-buy-custom.png", "meme-both-hybrid.png",
        "meme-brain-evolution.png", "meme-buzz-integrations.png", "meme-captain-owner.png",
        "meme-cmm-automation.png", "meme-db-distracted.png", "meme-disaster-spreadsheet.png",
        "meme-drake-build.png", "meme-drake-own-vs-rent.png", "meme-dwight-dev.png",
        "meme-excel-fine.png", "meme-exit-build-custom.png", "meme-exit-custom.png",
        "meme-fry-automation.png", "meme-fry-roi.png", "meme-galaxy-brain-software.png",
        "meme-gandalf-zaps.png", "meme-gru-plan.png", "meme-happening-deployed.png",
        "meme-harold-timeline.png", "meme-inigo-simple.png", "meme-kermit-push-to-prod.png",
        "meme-leo-cheers.png", "meme-mocking-spongebob.png", "meme-morpheus-excel.png",
        "meme-oprah-workaround.png", "meme-panik-kalm.png", "meme-patrick-push.png",
        "meme-pigeon-database.png", "meme-pooh-own-engine.png", "meme-rollsafe-data.png",
        "meme-simple-process.png", "meme-ski-polling.png", "meme-stonks-efficiency.png",
        "meme-success-roi.png", "meme-wddth-hipaa.png", "meme-wonka-enterprise.png",
    ]
    return [{"filename": f, "title": f.replace("meme-", "").replace(".png", "").replace("-", " ").title(), 
             "image_url": f"https://gera.yerem.in/images/memes/{f}"} for f in meme_files]


# ============================================================================
# CAPTION GENERATION
# ============================================================================

def get_caption(filename: str) -> str:
    """Generate caption based on meme filename."""
    key = filename.replace("meme-", "").replace(".png", "").replace(".jpg", "")
    caption = CAPTION_TEMPLATES.get(key, DEFAULT_CAPTION)
    return f"{caption}\n\n{HASHTAGS}"


# ============================================================================
# AYRSHARE API
# ============================================================================

def post_to_instagram(image_url: str, caption: str, schedule_date: Optional[datetime] = None, dry_run: bool = False) -> dict:
    """Post to Instagram via Ayrshare API."""
    
    payload = {
        "post": caption,
        "platforms": ["instagram"],
        "mediaUrls": [image_url],
        "instagramOptions": {"postType": "post"}
    }
    
    if schedule_date:
        # Ayrshare expects ISO format
        payload["scheduleDate"] = schedule_date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    
    if dry_run:
        return {"status": "dry_run", "payload": payload}
    
    headers = {
        "Authorization": f"Bearer {AYRSHARE_API_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(
        "https://app.ayrshare.com/api/post",
        headers=headers,
        json=payload
    )
    
    return response.json()


# ============================================================================
# MAIN
# ============================================================================

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Post memes to Instagram via Ayrshare")
    parser.add_argument("--dry-run", action="store_true", help="Preview without posting")
    parser.add_argument("--now", action="store_true", help="Post immediately (no scheduling)")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of posts")
    parser.add_argument("--start-date", type=str, default=None, help="Start date (YYYY-MM-DD)")
    args = parser.parse_args()
    
    print("=" * 60)
    print("MEME → INSTAGRAM POSTER")
    print("=" * 60)
    
    if args.dry_run:
        print("🔍 DRY RUN MODE - No actual posts will be made\n")
    
    # Fetch memes
    memes = fetch_memes_from_contentful()
    print(f"📦 Found {len(memes)} memes\n")
    
    # Apply limit if specified
    if args.limit:
        memes = memes[:args.limit]
        print(f"⚡ Limited to {args.limit} posts\n")
    
    # Calculate schedule
    if args.start_date:
        start = datetime.strptime(args.start_date, "%Y-%m-%d")
    else:
        start = datetime.now() + timedelta(days=1)
    
    start = start.replace(hour=POST_HOUR, minute=POST_MINUTE, second=0, microsecond=0)
    
    # Post each meme
    success_count = 0
    error_count = 0
    
    for i, meme in enumerate(memes):
        post_date = start + timedelta(days=i * POST_INTERVAL_DAYS)
        caption = get_caption(meme["filename"])
        
        print(f"[{i+1}/{len(memes)}] {meme['filename']}")
        print(f"    📅 {post_date.strftime('%Y-%m-%d %I:%M %p')} PT")
        print(f"    💬 {caption.split(chr(10))[0][:50]}...")
        
        try:
            result = post_to_instagram(
                image_url=meme["image_url"],
                caption=caption,
                schedule_date=None if args.now else post_date,
                dry_run=args.dry_run
            )
            
            if args.dry_run:
                print(f"    ✅ Would schedule\n")
            elif result.get("status") == "success" or "id" in result:
                print(f"    ✅ Scheduled!\n")
                success_count += 1
            else:
                print(f"    ❌ Error: {result}\n")
                error_count += 1
                
        except Exception as e:
            print(f"    ❌ Error: {e}\n")
            error_count += 1
    
    # Summary
    print("=" * 60)
    if args.dry_run:
        print(f"DRY RUN COMPLETE: {len(memes)} posts would be scheduled")
    else:
        print(f"COMPLETE: {success_count} scheduled, {error_count} failed")
    print("=" * 60)


if __name__ == "__main__":
    main()
