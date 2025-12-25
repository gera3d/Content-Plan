#!/usr/bin/env python3
"""
Upload all meme images to Contentful as memePost entries.
"""

import os
import re
import json
import time
import requests
from pathlib import Path

# Configuration
SPACE_ID = "oa9mphdwsgvp"
ENVIRONMENT = "master"
ACCESS_TOKEN = "***REDACTED***"
BASE_URL = f"https://api.contentful.com/spaces/{SPACE_ID}/environments/{ENVIRONMENT}"
UPLOAD_URL = f"https://upload.contentful.com/spaces/{SPACE_ID}"

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/vnd.contentful.management.v1+json"
}

MEMES_DIR = Path(__file__).parent / "gera-yerem-in/public/images/memes"


def filename_to_title(filename: str) -> str:
    """Convert meme-morpheus-excel.png to Morpheus Excel"""
    name = filename.replace("meme-", "").replace(".png", "").replace(".jpg", "")
    words = name.split("-")
    return " ".join(word.capitalize() for word in words)


def upload_image(filepath: Path) -> dict:
    """Upload image file to Contentful and return upload object"""
    print(f"  Uploading file: {filepath.name}...")
    
    with open(filepath, "rb") as f:
        file_data = f.read()
    
    # Create upload
    upload_response = requests.post(
        f"{UPLOAD_URL}/uploads",
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/octet-stream"
        },
        data=file_data
    )
    upload_response.raise_for_status()
    upload = upload_response.json()
    return upload


def create_asset(filename: str, upload_id: str) -> dict:
    """Create asset from upload"""
    title = filename_to_title(filename)
    
    asset_data = {
        "fields": {
            "title": {"en-US": title},
            "file": {
                "en-US": {
                    "contentType": "image/png",
                    "fileName": filename,
                    "uploadFrom": {
                        "sys": {
                            "type": "Link",
                            "linkType": "Upload",
                            "id": upload_id
                        }
                    }
                }
            }
        }
    }
    
    response = requests.post(
        f"{BASE_URL}/assets",
        headers=HEADERS,
        json=asset_data
    )
    response.raise_for_status()
    return response.json()


def process_asset(asset_id: str, version: int) -> dict:
    """Process asset to make it available"""
    response = requests.put(
        f"{BASE_URL}/assets/{asset_id}/files/en-US/process",
        headers={**HEADERS, "X-Contentful-Version": str(version)}
    )
    response.raise_for_status()
    return response


def publish_asset(asset_id: str, version: int) -> dict:
    """Publish asset"""
    response = requests.put(
        f"{BASE_URL}/assets/{asset_id}/published",
        headers={**HEADERS, "X-Contentful-Version": str(version)}
    )
    response.raise_for_status()
    return response.json()


def wait_for_processing(asset_id: str, max_retries: int = 30) -> dict:
    """Wait for asset processing to complete"""
    for i in range(max_retries):
        response = requests.get(
            f"{BASE_URL}/assets/{asset_id}",
            headers=HEADERS
        )
        response.raise_for_status()
        asset = response.json()
        
        file_info = asset.get("fields", {}).get("file", {}).get("en-US", {})
        if "url" in file_info:
            return asset
        
        time.sleep(1)
    
    raise TimeoutError(f"Asset {asset_id} processing timed out")


def create_meme_post(title: str, asset_id: str) -> dict:
    """Create memePost entry linked to asset"""
    entry_data = {
        "fields": {
            "title": {"en-US": title},
            "image": {
                "en-US": {
                    "sys": {
                        "type": "Link",
                        "linkType": "Asset",
                        "id": asset_id
                    }
                }
            },
            "status": {"en-US": "draft"},
            "altText": {"en-US": title}
        }
    }
    
    response = requests.post(
        f"{BASE_URL}/entries",
        headers={**HEADERS, "X-Contentful-Content-Type": "memePost"},
        json=entry_data
    )
    response.raise_for_status()
    return response.json()


def publish_entry(entry_id: str, version: int) -> dict:
    """Publish entry"""
    response = requests.put(
        f"{BASE_URL}/entries/{entry_id}/published",
        headers={**HEADERS, "X-Contentful-Version": str(version)}
    )
    response.raise_for_status()
    return response.json()


def main():
    print("=" * 60)
    print("MEME UPLOAD TO CONTENTFUL")
    print("=" * 60)
    
    # Get all meme files
    meme_files = sorted(MEMES_DIR.glob("meme-*.png"))
    print(f"\nFound {len(meme_files)} meme files to upload\n")
    
    success_count = 0
    error_count = 0
    
    for i, filepath in enumerate(meme_files, 1):
        print(f"[{i}/{len(meme_files)}] {filepath.name}")
        try:
            # Step 1: Upload file
            upload = upload_image(filepath)
            upload_id = upload["sys"]["id"]
            
            # Step 2: Create asset
            print("  Creating asset...")
            asset = create_asset(filepath.name, upload_id)
            asset_id = asset["sys"]["id"]
            asset_version = asset["sys"]["version"]
            
            # Step 3: Process asset
            print("  Processing asset...")
            process_asset(asset_id, asset_version)
            
            # Step 4: Wait for processing
            print("  Waiting for processing...")
            processed_asset = wait_for_processing(asset_id)
            
            # Step 5: Publish asset
            print("  Publishing asset...")
            published_asset = publish_asset(asset_id, processed_asset["sys"]["version"])
            
            # Step 6: Create memePost entry
            title = filename_to_title(filepath.name)
            print(f"  Creating memePost: {title}")
            entry = create_meme_post(title, asset_id)
            entry_id = entry["sys"]["id"]
            entry_version = entry["sys"]["version"]
            
            # Step 7: Publish entry
            print("  Publishing entry...")
            publish_entry(entry_id, entry_version)
            
            print("  ✅ Done!\n")
            success_count += 1
            
            # Small delay to avoid rate limiting
            time.sleep(0.5)
            
        except Exception as e:
            print(f"  ❌ Error: {e}\n")
            error_count += 1
    
    print("=" * 60)
    print(f"COMPLETE: {success_count} succeeded, {error_count} failed")
    print("=" * 60)


if __name__ == "__main__":
    main()
