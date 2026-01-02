# Bobert and the Monster Comics

## Mobile-Friendly Comic Structure

This folder contains comic images for the "Bobert and the Monster" series, optimized for both desktop and mobile viewing.

### Directory Structure

```
bobert/
  monster-roommate/
    full-page.png       # Traditional full comic page (desktop)
    panel-1.png         # Individual panel 1 (mobile)
    panel-2.png         # Individual panel 2 (mobile)
    panel-3.png         # Individual panel 3 (mobile)
    panel-4.png         # Individual panel 4 (mobile)
```

### How to Add New Comics

1. Create a folder for your comic: `assets/images/bobert/your-comic-name/`
2. Add your full-page comic as `full-page.png`
3. Export individual panels as `panel-1.png`, `panel-2.png`, etc.
4. Create a markdown file in `_bobert_and_the_monster/` with:

```yaml
---
title: "Your Comic Title"
date: 2025-12-30
issue_number: 3
series: "Bobert and the Monster"
series_slug: "bobert-and-the-monster"
layout: comic-page
comic_image: /assets/images/bobert/your-comic-name/full-page.png
alt_text: "Description of the comic for accessibility"
panel_images:
  - /assets/images/bobert/your-comic-name/panel-1.png
  - /assets/images/bobert/your-comic-name/panel-2.png
  - /assets/images/bobert/your-comic-name/panel-3.png
---
```

### Mobile Features

- **Desktop**: Shows full traditional comic page
- **Mobile**: 
  - **Panel View** (default): Swipe through panels one at a time
  - **Full Page View**: Scroll and pinch to zoom on the full page
  - Toggle button to switch between views

### Tips

- Panel images should be readable on their own
- Typical size: 800x600 or similar aspect ratio
- Full page is stacked panels for vertical reading
- Export with clear borders matching the Mission Hill style
