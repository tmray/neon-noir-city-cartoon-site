# Mobile Panel Splitting Guide for Comics

This guide explains how to automatically split your comics into mobile-friendly panels using the `split_comic_panels.py` script.

## Quick Start

For "Then This Happened" comics (1000x1200px with 2x2 panel layout):

```bash
# Split your comic into 4 panels
python3 split_comic_panels.py assets/images/your-comic.jpg -o assets/images/then-this-happened/comic-name/
```

## Complete Workflow

### 1. Add Your Comic Image

Place your full comic image in the `assets/images/` directory:
```
assets/images/251225-then-this-happened.jpg
```

### 2. Run the Panel Splitter

```bash
cd /home/tom/Public/neon-noir-city-vibe-site

python3 split_comic_panels.py \
    assets/images/251225-then-this-happened.jpg \
    -o assets/images/then-this-happened/christmas-chaos/
```

This will create:
```
assets/images/then-this-happened/christmas-chaos/
  ├── 251225-then-this-happened-panel-1.png  (Top left)
  ├── 251225-then-this-happened-panel-2.png  (Top right)
  ├── 251225-then-this-happened-panel-3.png  (Bottom left)
  └── 251225-then-this-happened-panel-4.png  (Bottom right)
```

### 3. Create the Comic Post

Create a new markdown file in `_then_this_happened/`:

```markdown
---
title: "Christmas Chaos"
date: 2025-12-25
issue_number: 5
series: "Then This Happened"
series_slug: "then-this-happened"
layout: comic-page
comic_image: /assets/images/251225-then-this-happened.jpg
alt_text: "A four-panel comic about holiday shopping madness"
panel_images:
  - /assets/images/then-this-happened/christmas-chaos/251225-then-this-happened-panel-1.png
  - /assets/images/then-this-happened/christmas-chaos/251225-then-this-happened-panel-2.png
  - /assets/images/then-this-happened/christmas-chaos/251225-then-this-happened-panel-3.png
  - /assets/images/then-this-happened/christmas-chaos/251225-then-this-happened-panel-4.png
---

Your creator's notes go here! Talk about what inspired this comic or any behind-the-scenes details.
```

### 4. Test Your Comic

View the comic page to verify:
- **Desktop**: Shows full traditional comic page
- **Mobile**: Panel-by-panel swipe view + zoom/pan toggle

## Panel Reading Order

The script splits comics in reading order for a 2x2 grid:

```
┌─────────┬─────────┐
│ Panel 1 │ Panel 2 │  Top row (left to right)
├─────────┼─────────┤
│ Panel 3 │ Panel 4 │  Bottom row (left to right)
└─────────┴─────────┘
```

## File Naming Convention

**Original comic**: `YYMMDD-then-this-happened.jpg`

**Generated panels**: `YYMMDD-then-this-happened-panel-N.png`

This ensures:
- ✅ Unique filenames for each comic
- ✅ No accidental overwrites
- ✅ Easy to identify which panels belong to which comic

## Comic Requirements

For "Then This Happened" series:
- **Dimensions**: 1000px wide × 1200px tall
- **Layout**: 2×2 grid (4 equal panels)
- **Panel size**: Each panel becomes 500×600px

## Optional: Skip Panels

If you want to display only the full page on mobile (no panel splitting), simply omit the `panel_images` field:

```yaml
---
title: "My Comic"
comic_image: /assets/images/my-comic.jpg
# No panel_images field = mobile users see zoom/pan view only
---
```

## Troubleshooting

**Wrong dimensions?**
The script will show warnings if your comic isn't 1000×1200px.

**Panels in wrong order?**
Make sure your comic follows the 2×2 reading order (top-left, top-right, bottom-left, bottom-right).

**Need to regenerate panels?**
Just run the script again - it will overwrite the existing panels.

## Script Options

```bash
# View all options
python3 split_comic_panels.py --help

# Basic usage (saves in same directory as input)
python3 split_comic_panels.py path/to/comic.jpg

# Specify output directory
python3 split_comic_panels.py path/to/comic.jpg -o path/to/output/

# Alternative long form
python3 split_comic_panels.py path/to/comic.jpg --output-dir path/to/output/
```

## Example: Complete New Comic

```bash
# 1. Split the panels
python3 split_comic_panels.py \
    assets/images/251230-then-this-happened.jpg \
    -o assets/images/then-this-happened/new-years-eve/

# 2. Create _then_this_happened/2025-12-30-new-years-eve.md
# 3. Add the front matter with panel_images paths
# 4. Commit and push!
```

---

**Pro tip**: You can batch process multiple comics by creating a simple shell script!
