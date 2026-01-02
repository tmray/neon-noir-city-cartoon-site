# Mission Hill Indie Comic Site

A Jekyll-based website inspired by the vibrant, neon-noir aesthetic of the Mission Hill cartoon. Perfect for indie artists, comic creators, and anyone who wants a site with personality and visual punch.

## 🎨 Features

- **Mission Hill Color Palette**: Bling-Blau Blue, Neon Orchid, Toxic Lime, Goldenrod Yellow, and Heavy Ink Black
- **Comic Book Aesthetic**: Thick double borders, halftone patterns, wonky angles
- **Three Content Types**:
  - Blog posts for written content
  - Video posts for embedded videos
  - Drawing posts for artwork showcases
- **Zine-Style Grid Layout**: Content cards arranged like comic panels
- **Neon Signpost Navigation**: Bold, eye-catching menu design
- **Fully Responsive**: Looks great on all devices

## 🚀 Quick Start

### Prerequisites

- Ruby (version 2.7 or higher)
- RubyGems
- GCC and Make

### Installation

1. **Install Jekyll and Bundler**

```bash
gem install jekyll bundler
```

2. **Navigate to the project directory**

```bash
cd neon-noir-city-vibe-site
```

3. **Install dependencies**

```bash
bundle install
```

4. **Run the development server**

```bash
bundle exec jekyll serve
```

5. **View your site**

Open your browser and go to `http://localhost:4000`

## 📝 Creating Content

### Blog Posts

Create a new file in `_posts/` following the naming convention: `YYYY-MM-DD-title.md`

```markdown
---
layout: post
title: "Your Post Title"
date: 2025-12-20 10:00:00 -0500
---

Your content here...
```

### Video Posts

Create a new file in `_videos/` with your video embed URL:

```markdown
---
title: "Your Video Title"
date: 2025-12-20 10:00:00 -0500
video_url: "https://www.youtube.com/embed/VIDEO_ID"
---

Description of your video...
```

### Drawing Posts

Create a new file in `_drawings/` with your image path:

```markdown
---
title: "Your Drawing Title"
date: 2025-12-20 10:00:00 -0500
image: "/assets/images/your-image.jpg"
---

Description of your artwork...
```

## 🎨 Customization

### Updating Site Information

Edit `_config.yml` to update:
- Site title
- Description
- Author name
- Base URL

### Adding Images

Place your images in `/assets/images/` and reference them in your posts.

### Modifying Colors

The color palette is defined in `/assets/css/main.css` using CSS variables:

```css
:root {
  --bling-blau: #3252E0;
  --neon-orchid: #C743E1;
  --toxic-lime: #B6F54D;
  --goldenrod: #FFD200;
  --heavy-ink: #1A1A1A;
}
```

### Changing Fonts

The site uses Google Fonts:
- **Bangers** for headings
- **Patrick Hand** for body text

To change fonts, update the Google Fonts link in `_layouts/default.html` and the font families in the CSS.

## 📁 Project Structure

```
neon-noir-city-vibe-site/
├── _config.yml           # Site configuration
├── _includes/            # Reusable components
│   ├── header.html
│   └── footer.html
├── _layouts/             # Page layouts
│   ├── default.html
│   ├── post.html
│   ├── video.html
│   └── drawing.html
├── _posts/               # Blog posts
├── _videos/              # Video posts
├── _drawings/            # Drawing posts
├── assets/
│   ├── css/
│   │   └── main.css     # Main stylesheet
│   └── images/          # Your images
├── index.html            # Homepage
├── blog.html             # Blog archive
├── videos.html           # Videos archive
├── drawings.html         # Drawings archive
├── Gemfile               # Ruby dependencies
└── README.md             # This file
```

## 🛠️ Building for Production

To build a production-ready version of your site:

```bash
bundle exec jekyll build
```

The static site will be generated in the `_site/` directory.

## 📦 Deployment

This site can be deployed to:
- GitHub Pages
- Netlify
- Vercel
- Any static hosting service

For GitHub Pages, simply push to a repository and enable Pages in the settings.

## 🎯 Style Guide Reference

The design is based on Mission Hill's aesthetic:
- **Double borders** create depth
- **Halftone patterns** add texture
- **Wonky angles** (slight rotations) add personality
- **Bold typography** commands attention
- **High contrast colors** create visual impact

## 🤝 Contributing

Feel free to customize this template for your own needs! Some ideas:
- Add new content types
- Create custom page layouts
- Implement additional JavaScript interactions
- Add more comic-inspired visual effects

## 📄 License

This project is open source and available for personal and commercial use.

## 🎭 Credits

Inspired by the aesthetic of *Mission Hill* created by Bill Oakley and Josh Weinstein.

---

**Happy creating! Keep it indie, keep it real.** 🎨✨
