#!/usr/bin/env python3
"""
Preview meme posting schedule with generated captions.
This is a dry-run to show what would be posted.
"""

import os
import json
import requests
from datetime import datetime, timedelta

# Configuration
SPACE_ID = "oa9mphdwsgvp"
ENVIRONMENT = "master"
# Use Delivery API (read-only, no auth issues)
DELIVERY_TOKEN = os.getenv("CONTENTFUL_DELIVERY_TOKEN", "")

BASE_URL = f"https://cdn.contentful.com/spaces/{SPACE_ID}/environments/{ENVIRONMENT}"

# Meme-specific caption templates in Gera's voice
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

# Default caption for memes without specific templates
DEFAULT_CAPTION = "When your software actually does what you need. What a concept."

# Hashtags
HASHTAGS = "#customsoftware #automation #smallbusiness #techhumor #nocode #entrepreneur #businesstips"


def get_caption_for_meme(filename: str) -> str:
    """Generate caption based on meme filename."""
    # Extract key from filename (e.g., "meme-morpheus-excel.png" -> "morpheus-excel")
    key = filename.replace("meme-", "").replace(".png", "").replace(".jpg", "")
    
    caption = CAPTION_TEMPLATES.get(key, DEFAULT_CAPTION)
    return f"{caption}\n\n{HASHTAGS}"


def fetch_memes_from_contentful(token: str) -> list:
    """Fetch all memePost entries from Contentful."""
    if not token:
        # Fallback to local file list
        return get_local_meme_list()
    
    headers = {"Authorization": f"Bearer {token}"}
    
    # Get entries
    response = requests.get(
        f"{BASE_URL}/entries",
        headers=headers,
        params={
            "content_type": "memePost",
            "limit": 100,
            "include": 1
        }
    )
    
    if response.status_code != 200:
        print(f"Error fetching from Contentful: {response.status_code}")
        return get_local_meme_list()
    
    data = response.json()
    
    # Build asset map
    assets = {a["sys"]["id"]: a for a in data.get("includes", {}).get("Asset", [])}
    
    memes = []
    for entry in data.get("items", []):
        fields = entry.get("fields", {})
        title = fields.get("title", "Untitled")
        
        # Get image URL
        image_ref = fields.get("image", {}).get("sys", {}).get("id")
        image_url = ""
        filename = ""
        if image_ref and image_ref in assets:
            asset = assets[image_ref]
            file_info = asset.get("fields", {}).get("file", {})
            image_url = "https:" + file_info.get("url", "")
            filename = file_info.get("fileName", "")
        
        memes.append({
            "id": entry["sys"]["id"],
            "title": title,
            "filename": filename,
            "image_url": image_url
        })
    
    return memes


def get_local_meme_list() -> list:
    """Fallback: get meme list from MEME_REFERENCE.md patterns."""
    meme_files = [
        "meme-ackabar-trap.png",
        "meme-afraid-zap-failed.png",
        "meme-astronaut-polling.png",
        "meme-batman-slap.png",
        "meme-boat-buy-custom.png",
        "meme-both-hybrid.png",
        "meme-brain-evolution.png",
        "meme-buzz-integrations.png",
        "meme-captain-owner.png",
        "meme-cmm-automation.png",
        "meme-db-distracted.png",
        "meme-disaster-spreadsheet.png",
        "meme-drake-build.png",
        "meme-drake-own-vs-rent.png",
        "meme-dwight-dev.png",
        "meme-excel-fine.png",
        "meme-exit-build-custom.png",
        "meme-exit-custom.png",
        "meme-fry-automation.png",
        "meme-fry-roi.png",
        "meme-galaxy-brain-software.png",
        "meme-gandalf-zaps.png",
        "meme-gru-plan.png",
        "meme-happening-deployed.png",
        "meme-harold-timeline.png",
        "meme-inigo-simple.png",
        "meme-kermit-push-to-prod.png",
        "meme-leo-cheers.png",
        "meme-mocking-spongebob.png",
        "meme-morpheus-excel.png",
        "meme-oprah-workaround.png",
        "meme-panik-kalm.png",
        "meme-patrick-push.png",
        "meme-pigeon-database.png",
        "meme-pooh-own-engine.png",
        "meme-rollsafe-data.png",
        "meme-simple-process.png",
        "meme-ski-polling.png",
        "meme-stonks-efficiency.png",
        "meme-success-roi.png",
        "meme-wddth-hipaa.png",
        "meme-wonka-enterprise.png",
    ]
    
    return [{"filename": f, "title": f.replace("meme-", "").replace(".png", "").replace("-", " ").title()} for f in meme_files]


def generate_schedule(memes: list, start_date: datetime, interval_days: int = 2) -> list:
    """Generate posting schedule."""
    schedule = []
    post_time = start_date.replace(hour=12, minute=0, second=0, microsecond=0)
    
    for i, meme in enumerate(memes):
        post_date = post_time + timedelta(days=i * interval_days)
        caption = get_caption_for_meme(meme["filename"])
        
        schedule.append({
            "number": i + 1,
            "date": post_date.strftime("%Y-%m-%d"),
            "day": post_date.strftime("%A"),
            "time": "12:00 PM PT",
            "filename": meme["filename"],
            "title": meme["title"],
            "caption": caption
        })
    
    return schedule


def main():
    print("=" * 80)
    print("MEME POSTING SCHEDULE PREVIEW")
    print("=" * 80)
    print()
    
    # Fetch memes
    token = DELIVERY_TOKEN
    memes = fetch_memes_from_contentful(token)
    
    print(f"Found {len(memes)} memes\n")
    
    # Generate schedule starting tomorrow
    start = datetime.now() + timedelta(days=1)
    schedule = generate_schedule(memes, start)
    
    # Output as formatted table
    print("-" * 80)
    for item in schedule:
        print(f"#{item['number']:02d} | {item['date']} ({item['day']}) at {item['time']}")
        print(f"    Meme: {item['filename']}")
        print(f"    Caption:")
        for line in item['caption'].split('\n'):
            print(f"      {line}")
        print("-" * 80)
    
    # Summary
    last_date = schedule[-1]['date'] if schedule else "N/A"
    print(f"\nTotal: {len(schedule)} posts")
    print(f"Schedule: Every 2 days at 12:00 PM PT")
    print(f"First post: {schedule[0]['date'] if schedule else 'N/A'}")
    print(f"Last post: {last_date}")
    
    # Output JSON for artifact
    print("\n\n--- JSON OUTPUT FOR REVIEW ---\n")
    print(json.dumps(schedule, indent=2))


if __name__ == "__main__":
    main()
