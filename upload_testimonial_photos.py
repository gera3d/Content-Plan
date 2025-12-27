#!/usr/bin/env python3
"""
Upload testimonial photos to Contentful and link them to existing testimonials.
"""

import os
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

PHOTOS_DIR = Path(__file__).parent / "gera-yerem-in/public/images/testimonials"

# Map photo filenames to testimonial names (based on LinkedIn data)
PHOTO_TO_NAME = {
    "tom_h.jpg": "Tom Hakel",
    "karen_s.jpg": "Karen Serpa",
    "leslie_c.jpg": "Leslie Chalmers",
    "verjel_c.jpg": "Verjel Cacayorin",
    "mark_v.jpg": "Mark Vargas",
    "nate_b.jpg": "Nate Bauer",
    "jenna_s.jpg": "Jenna Sherron Stutsman",
    "julie_h.jpg": "Julie Halpin",
    "Ryan_h.jpg": "Ryan Herche",
    "gloria.jpg": "Gloria Jakusz",
    "devon_s.jpg": "Devon Swift",
    "emily_k.jpg": "Emily Kischell",
    "emily_b.jpg": "Emily Barker",
    "bruce_c.jpg": "Bruce Corkhill",
    "david_m.jpg": "David Mercer",
    "george_m.jpg": "George R. Moskoff",
    "greg_j.jpg": "Greg Jones",
    "david_s.jpg": "David Simpson",
    "anne_p.jpg": "Anne Marie Petty",
    "brian.jpg": "Brian Chock",
    "arsen_y.jpg": "Arsen Yeremin",
}


def get_all_testimonials():
    """Fetch all testimonial entries"""
    response = requests.get(
        f"{BASE_URL}/entries?content_type=testimonial&limit=100",
        headers=HEADERS
    )
    response.raise_for_status()
    return response.json().get("items", [])


def find_testimonial_by_name(testimonials, name):
    """Find testimonial entry by name"""
    for t in testimonials:
        entry_name = t.get("fields", {}).get("name", {}).get("en-US", "")
        if name.lower() in entry_name.lower() or entry_name.lower() in name.lower():
            return t
    return None


def upload_image(filepath: Path) -> dict:
    """Upload image file to Contentful and return upload object"""
    print(f"  Uploading file: {filepath.name}...")
    
    with open(filepath, "rb") as f:
        file_data = f.read()
    
    upload_response = requests.post(
        f"{UPLOAD_URL}/uploads",
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/octet-stream"
        },
        data=file_data
    )
    upload_response.raise_for_status()
    return upload_response.json()


def create_asset(filename: str, upload_id: str, title: str) -> dict:
    """Create asset from upload"""
    asset_data = {
        "fields": {
            "title": {"en-US": f"{title} Photo"},
            "file": {
                "en-US": {
                    "contentType": "image/jpeg",
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


def process_asset(asset_id: str, version: int):
    """Process asset"""
    response = requests.put(
        f"{BASE_URL}/assets/{asset_id}/files/en-US/process",
        headers={**HEADERS, "X-Contentful-Version": str(version)}
    )
    response.raise_for_status()


def wait_for_processing(asset_id: str, max_retries: int = 30) -> dict:
    """Wait for asset processing"""
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


def publish_asset(asset_id: str, version: int) -> dict:
    """Publish asset"""
    response = requests.put(
        f"{BASE_URL}/assets/{asset_id}/published",
        headers={**HEADERS, "X-Contentful-Version": str(version)}
    )
    response.raise_for_status()
    return response.json()


def update_testimonial_image(entry_id: str, version: int, asset_id: str):
    """Update testimonial entry with image link"""
    update_data = {
        "fields": {
            "image": {
                "en-US": {
                    "sys": {
                        "type": "Link",
                        "linkType": "Asset",
                        "id": asset_id
                    }
                }
            }
        }
    }
    
    # First get the current entry to preserve other fields
    response = requests.get(
        f"{BASE_URL}/entries/{entry_id}",
        headers=HEADERS
    )
    response.raise_for_status()
    current = response.json()
    
    # Merge in the image field
    current_fields = current.get("fields", {})
    current_fields["image"] = update_data["fields"]["image"]
    
    # Update
    response = requests.put(
        f"{BASE_URL}/entries/{entry_id}",
        headers={**HEADERS, "X-Contentful-Version": str(version)},
        json={"fields": current_fields}
    )
    response.raise_for_status()
    return response.json()


def publish_entry(entry_id: str, version: int):
    """Publish entry"""
    response = requests.put(
        f"{BASE_URL}/entries/{entry_id}/published",
        headers={**HEADERS, "X-Contentful-Version": str(version)}
    )
    response.raise_for_status()
    return response.json()


def main():
    print("=" * 60)
    print("TESTIMONIAL PHOTO UPLOAD TO CONTENTFUL")
    print("=" * 60)
    
    # Get all testimonials
    print("\nFetching existing testimonials...")
    testimonials = get_all_testimonials()
    print(f"Found {len(testimonials)} testimonials\n")
    
    # Get all photo files
    photo_files = list(PHOTOS_DIR.glob("*.jpg"))
    print(f"Found {len(photo_files)} photo files to upload\n")
    
    success_count = 0
    error_count = 0
    skipped_count = 0
    
    for filepath in photo_files:
        filename = filepath.name
        person_name = PHOTO_TO_NAME.get(filename)
        
        if not person_name:
            print(f"⚠️  No mapping for {filename}, skipping")
            skipped_count += 1
            continue
        
        testimonial = find_testimonial_by_name(testimonials, person_name)
        if not testimonial:
            print(f"⚠️  No testimonial found for {person_name}, skipping")
            skipped_count += 1
            continue
        
        entry_id = testimonial["sys"]["id"]
        entry_version = testimonial["sys"]["version"]
        
        # Check if already has image
        if testimonial.get("fields", {}).get("image", {}).get("en-US"):
            print(f"⏭️  {person_name} already has image, skipping")
            skipped_count += 1
            continue
        
        print(f"📸 Processing {person_name} ({filename})")
        
        try:
            # Upload image
            upload = upload_image(filepath)
            upload_id = upload["sys"]["id"]
            
            # Create asset
            print("  Creating asset...")
            asset = create_asset(filename, upload_id, person_name)
            asset_id = asset["sys"]["id"]
            asset_version = asset["sys"]["version"]
            
            # Process asset
            print("  Processing...")
            process_asset(asset_id, asset_version)
            
            # Wait for processing
            print("  Waiting for processing...")
            processed_asset = wait_for_processing(asset_id)
            
            # Publish asset
            print("  Publishing asset...")
            published_asset = publish_asset(asset_id, processed_asset["sys"]["version"])
            
            # Update testimonial with image
            print("  Linking to testimonial...")
            updated = update_testimonial_image(entry_id, entry_version, asset_id)
            
            # Publish testimonial
            print("  Publishing testimonial...")
            publish_entry(entry_id, updated["sys"]["version"])
            
            print(f"  ✅ Done!\n")
            success_count += 1
            
            time.sleep(0.5)
            
        except Exception as e:
            print(f"  ❌ Error: {e}\n")
            error_count += 1
    
    print("=" * 60)
    print(f"COMPLETE: {success_count} uploaded, {skipped_count} skipped, {error_count} failed")
    print("=" * 60)


if __name__ == "__main__":
    main()
