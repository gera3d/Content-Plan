#!/usr/bin/env python3
"""Delete broken meme entries and assets from Contentful"""

import requests

SPACE_ID = "oa9mphdwsgvp"
ENVIRONMENT = "master"
ACCESS_TOKEN = "***REDACTED***"
BASE_URL = f"https://api.contentful.com/spaces/{SPACE_ID}/environments/{ENVIRONMENT}"

HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/vnd.contentful.management.v1+json"
}

# Broken meme titles to delete
BROKEN_MEMES = [
    "First Time",
    "Aliens Custom",
    "Waiting Excel",
    "Money Printer",
    "Buttons Sweat",
    "Distracted Custom",
    "Yoda Code",
    "Car Choice",
    "Draw Owl",
    "Bernie Budget",
    "Waiting Skeleton",
    "Grandma File",
    "Change Mind Excel",
    "Math Lady"
]

def unpublish_and_delete_entry(entry_id, version):
    """Unpublish then delete an entry"""
    # Unpublish first
    requests.delete(
        f"{BASE_URL}/entries/{entry_id}/published",
        headers=HEADERS
    )
    # Get updated version
    resp = requests.get(f"{BASE_URL}/entries/{entry_id}", headers=HEADERS)
    if resp.ok:
        version = resp.json()["sys"]["version"]
    # Delete
    requests.delete(
        f"{BASE_URL}/entries/{entry_id}",
        headers={**HEADERS, "X-Contentful-Version": str(version)}
    )

def unpublish_and_delete_asset(asset_id, version):
    """Unpublish then delete an asset"""
    # Unpublish first
    requests.delete(
        f"{BASE_URL}/assets/{asset_id}/published",
        headers=HEADERS
    )
    # Get updated version
    resp = requests.get(f"{BASE_URL}/assets/{asset_id}", headers=HEADERS)
    if resp.ok:
        version = resp.json()["sys"]["version"]
    # Delete
    requests.delete(
        f"{BASE_URL}/assets/{asset_id}",
        headers={**HEADERS, "X-Contentful-Version": str(version)}
    )

def main():
    print("Fetching memePost entries...")
    resp = requests.get(f"{BASE_URL}/entries?content_type=memePost&limit=100", headers=HEADERS)
    entries = resp.json()["items"]
    
    print("Fetching assets...")
    resp = requests.get(f"{BASE_URL}/assets?limit=250", headers=HEADERS)
    assets = resp.json()["items"]
    
    deleted_entries = 0
    deleted_assets = 0
    
    for entry in entries:
        title = entry.get("fields", {}).get("title", {}).get("en-US", "")
        if title in BROKEN_MEMES:
            entry_id = entry["sys"]["id"]
            version = entry["sys"]["version"]
            print(f"Deleting entry: {title} ({entry_id})")
            unpublish_and_delete_entry(entry_id, version)
            deleted_entries += 1
    
    for asset in assets:
        title = asset.get("fields", {}).get("title", {}).get("en-US", "")
        if title in BROKEN_MEMES:
            asset_id = asset["sys"]["id"]
            version = asset["sys"]["version"]
            print(f"Deleting asset: {title} ({asset_id})")
            unpublish_and_delete_asset(asset_id, version)
            deleted_assets += 1
    
    print(f"\nDeleted {deleted_entries} entries and {deleted_assets} assets")

if __name__ == "__main__":
    main()
