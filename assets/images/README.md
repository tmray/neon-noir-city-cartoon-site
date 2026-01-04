# Images Directory

## OpenGraph / Social Media Images

For best sharing results on social media, create these images at **1200×630px**:

- `og-default.jpg` - Default image for home page and posts without specific images
- `site-logo.png` - Site logo (also used by SEO tag)

### Adding Images to Posts

Add an `image:` field to any post's front matter:

```yaml
---
title: "My Post Title"
date: 2026-01-04
image: /assets/images/my-post-preview.jpg
---
```

If no image is specified, the site will use `/assets/images/og-default.jpg` as configured in `_config.yml`.

## Subdirectories

- `bobert/` - Bobert and the Monster comic panels
- `then-this-happened/` - Then This Happened comic panels
- `book-covers/` - Book cover images for the books page

## Supported Formats

JPG, PNG, GIF, SVG

