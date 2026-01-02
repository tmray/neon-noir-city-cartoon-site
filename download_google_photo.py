#!/usr/bin/env python3
"""
Script to download comic images from Google Photos shared links for Mission Hill comic site
Usage: python3 download_google_photo.py <google-photos-url>
"""

import sys
import os
import re
import requests
from datetime import datetime
from pathlib import Path

# ANSI colors
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
NC = '\033[0m'  # No Color

def print_usage():
    print(f"{RED}Error: No URL provided{NC}")
    print("Usage: python3 download_google_photo.py <google-photos-url>")
    print("Example: python3 download_google_photo.py https://photos.app.goo.gl/xxxxx")

def get_user_input(prompt, default=None):
    """Get user input with optional default value"""
    if default:
        response = input(f"{YELLOW}{prompt} [{default}]:{NC} ").strip()
        return response if response else default
    else:
        response = input(f"{YELLOW}{prompt}:{NC} ").strip()
        return response

def select_comic_series():
    """Prompt user to select a comic series"""
    print(f"\n{YELLOW}Select comic series:{NC}")
    print("1. Then This Happened (then-this-happened)")
    print("2. Bobert and the Monster (bobert-and-the-monster)")
    
    while True:
        choice = input(f"{YELLOW}Enter 1 or 2:{NC} ").strip()
        if choice == "1":
            return "then-this-happened", "Then This Happened", "then-this-happened"
        elif choice == "2":
            return "bobert-and-the-monster", "Bobert and the Monster", "bobert"
        else:
            print(f"{RED}Invalid choice. Please enter 1 or 2.{NC}")

def extract_image_url(google_url):
    """Extract the actual image URL from a Google Photos shared link"""
    try:
        # Follow redirects and get the page content
        response = requests.get(google_url, timeout=10)
        response.raise_for_status()
        html = response.text
        
        # Try multiple patterns to find the image URL
        patterns = [
            r'https://lh3\.googleusercontent\.com/[^"\s<>]+',
            r'"(https://lh3\.googleusercontent\.com/[^"]+)"',
            r'contentUrl":"(https://lh3\.googleusercontent\.com/[^"]+)"',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, html)
            if matches:
                # Clean up the URL
                image_url = matches[0].strip('"')
                # Remove any existing size parameters and add download parameter
                image_url = re.sub(r'=w\d+-h\d+.*$', '', image_url)
                image_url = re.sub(r'=s\d+.*$', '', image_url)
                # Add parameter to download full resolution
                if '=' not in image_url.split('/')[-1]:
                    image_url += '=d'
                else:
                    image_url = re.sub(r'=[^/]*$', '=d', image_url)
                return image_url
        
        return None
    except requests.RequestException as e:
        print(f"{RED}Error fetching URL: {e}{NC}")
        return None

def download_image(image_url, output_path):
    """Download the image from the URL to the output path"""
    try:
        response = requests.get(image_url, stream=True, timeout=30)
        response.raise_for_status()
        
        # Get the total file size
        total_size = int(response.headers.get('content-length', 0))
        
        with open(output_path, 'wb') as f:
            if total_size == 0:
                f.write(response.content)
            else:
                downloaded = 0
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        # Simple progress indicator
                        percent = (downloaded / total_size) * 100
                        print(f"\rDownloading: {percent:.1f}%", end='', flush=True)
                print()  # New line after progress
        
        return True
    except requests.RequestException as e:
        print(f"{RED}Error downloading image: {e}{NC}")
        return False

def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    
    google_url = sys.argv[1]
    
    # Get comic series info
    series_slug, series_name, image_folder = select_comic_series()
    
    # Get episode/comic slug
    episode_slug = get_user_input("\nEnter episode slug (e.g., 'coffee-spill', 'monster-roommate')")
    if not episode_slug:
        print(f"{RED}Error: Episode slug is required{NC}")
        sys.exit(1)
    
    # Get filename (with default)
    default_filename = f"{episode_slug}.jpg"
    filename = get_user_input(f"\nEnter filename", default_filename)
    
    # Set up paths - use appropriate folder structure
    episode_dir = Path(f"./assets/images/{image_folder}/{episode_slug}")
    episode_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = episode_dir / filename
    
    print(f"\n{YELLOW}Downloading image from Google Photos...{NC}")
    
    # Extract the actual image URL
    image_url = extract_image_url(google_url)
    
    if not image_url:
        print(f"{RED}Error: Could not extract image URL from Google Photos link{NC}")
        print(f"{YELLOW}Please try:{NC}")
        print("1. Open the link in a browser")
        print("2. Right-click the image and select 'Open image in new tab'")
        print("3. Copy that URL and run the script again with that direct URL")
        sys.exit(1)
    
    print(f"{YELLOW}Found image URL:{NC} {image_url[:80]}...")
    print(f"{YELLOW}Downloading to:{NC} {output_path}")
    
    # Download the image
    if download_image(image_url, output_path):
        relative_path = f"/assets/images/{image_folder}/{episode_slug}/{filename}"
        print(f"{GREEN}✓ Success!{NC} Image downloaded to: {output_path}")
        print()
        print(f"{GREEN}Add this to your Jekyll comic post front matter:{NC}")
        print()
        print("---")
        print(f'title: "Your Comic Title"')
        print(f"date: {datetime.now().strftime('%Y-%m-%d')}")
        print(f"issue_number: 1")
        print(f'series: "{series_name}"')
        print(f'series_slug: "{series_slug}"')
        print(f"layout: comic-page")
        print(f'comic_image: {relative_path}')
        print(f'alt_text: "Description of your comic"')
        print("---")
        print()
        print(f"{YELLOW}Or if using panel images:{NC}")
        print("panel_images:")
        print(f"  - {relative_path}")
        print()
    else:
        print(f"{RED}Error: Failed to download image{NC}")
        sys.exit(1)

if __name__ == "__main__":
    main()
