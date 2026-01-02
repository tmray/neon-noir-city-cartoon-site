#!/usr/bin/env python3
"""
Split "Then This Happened" comics into 4 mobile-friendly panels.

Usage:
    python split_comic_panels.py path/to/comic.jpg
    python split_comic_panels.py path/to/comic.jpg --output-dir assets/images/comics/my-comic/
"""

import sys
import os
from PIL import Image
import argparse

def split_comic_into_panels(input_path, output_dir=None, panel_height=300):
    """
    Split a comic image into 4 equal panels.
    
    Args:
        input_path: Path to the comic image (1000x1200px)
        output_dir: Directory to save panels (default: same as input)
        panel_height: Height of each panel in pixels (default: 300)
    """
    try:
        # Open the comic image
        img = Image.open(input_path)
        width, height = img.size
        
        print(f"Processing: {input_path}")
        print(f"Image size: {width}x{height}px")
        
        # Verify dimensions
        if width != 1000:
            print(f"⚠️  Warning: Expected width 1000px, got {width}px")
        if height != 1200:
            print(f"⚠️  Warning: Expected height 1200px, got {height}px")
        
        # Determine output directory
        if output_dir is None:
            output_dir = os.path.dirname(input_path)
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Get the base filename and extension
        base_filename = os.path.splitext(os.path.basename(input_path))[0]
        file_extension = os.path.splitext(input_path)[1].lower()
        
        # Determine PIL format based on extension
        if file_extension in ['.jpg', '.jpeg']:
            save_format = 'JPEG'
            extension = '.jpg'
        elif file_extension == '.png':
            save_format = 'PNG'
            extension = '.png'
        else:
            # Default to PNG for unknown formats
            save_format = 'PNG'
            extension = '.png'
            print(f"⚠️  Warning: Unknown format {file_extension}, defaulting to PNG")
        
        # Split into 4 panels (2x2 grid: 2 on top, 2 on bottom)
        panel_width = width // 2  # 500px
        panel_height = height // 2  # 600px
        
        print(f"\nSplitting into 4 panels in 2x2 grid ({panel_width}x{panel_height}px each):")
        
        # Define panel positions (left, top, right, bottom)
        panels = [
            (0, 0, panel_width, panel_height),              # Panel 1: Top left
            (panel_width, 0, width, panel_height),          # Panel 2: Top right
            (0, panel_height, panel_width, height),         # Panel 3: Bottom left
            (panel_width, panel_height, width, height)      # Panel 4: Bottom right
        ]
        
        for i, crop_box in enumerate(panels, start=1):
            # Crop the panel
            panel = img.crop(crop_box)
            
            # Save the panel with original filename prefix and extension
            output_path = os.path.join(output_dir, f"{base_filename}-panel-{i}{extension}")
            
            # Save with appropriate format and options
            if save_format == 'JPEG':
                panel.save(output_path, save_format, optimize=True, quality=95)
            else:
                panel.save(output_path, save_format, optimize=True)
            
            print(f"  ✓ Saved: {output_path}")
        
        print(f"\n✅ Successfully split comic into 4 panels (2x2 grid)!")
        print(f"📁 Output directory: {output_dir}")
        
        return True
        
    except FileNotFoundError:
        print(f"❌ Error: File not found: {input_path}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Split "Then This Happened" comics into 4 mobile-friendly panels',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Split a comic (panels saved in same directory)
  python split_comic_panels.py assets/images/my-comic.jpg
  
  # Split and save to specific directory
  python split_comic_panels.py assets/images/my-comic.jpg \\
      --output-dir assets/images/then-this-happened/my-comic/
  
  # Process with custom panel height
  python split_comic_panels.py assets/images/my-comic.jpg --panel-height 400
        """
    )
    
    parser.add_argument('input', help='Path to the comic image to split')
    parser.add_argument(
        '-o', '--output-dir',
        help='Directory to save panel images (default: same as input file)'
    )
    parser.add_argument(
        '--panel-height',
        type=int,
        default=300,
        help='Height of each panel in pixels (default: 300)'
    )
    
    args = parser.parse_args()
    
    # Validate input file exists
    if not os.path.isfile(args.input):
        print(f"❌ Error: Input file does not exist: {args.input}")
        sys.exit(1)
    
    # Split the comic
    success = split_comic_into_panels(
        args.input,
        args.output_dir,
        args.panel_height
    )
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
