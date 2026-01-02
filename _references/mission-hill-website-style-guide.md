# mission hill themed site style guide

Creating a website based on *Mission Hill* is a fantastic idea. The show’s aesthetic is a perfect blend of **1990s indie "slacker" culture**, **Silver Age comic book tributes**, and a **vibrant, neon-noir city vibe**.

Since you are using Jekyll, you can lean into a "lo-fi" but highly structured CSS approach. Here is a style guide to help you capture that specific "Cosmopolis" look.

---

## 1. The Color Palette: "Electric Slacker"

*Mission Hill* used a very specific color theory where shadows aren't just "darker"—they are often saturated purples, blues, or pinks.

| Element | Hex Code | Usage |
| --- | --- | --- |
| **Bling-Blau Blue** | `#3252E0` | Main accent, link colors, or Kevin’s hair. |
| **Neon Orchid** | `#C743E1` | Deep shadows, hover states, or "night mode" UI. |
| **Toxic Lime** | `#B6F54D` | Call-to-action buttons or highlights. |
| **Goldenrod Yellow** | `#FFD200` | Headers or paper-texture backgrounds. |
| **Heavy Ink Black** | `#1A1A1A` | Borders and body text (never use pure #000). |

---

## 2. Typography: The Comic Influence

The show’s title card features a mix of Art Nouveau and hand-drawn comic styles.

* **Headings (The "Title" Look):** Use a font that feels like a 1920s/30s tall serif or a chunky comic font.
* *Google Font Suggestions:* **"Bangers"** (for energy) or **"Della Respira"** (for that eccentric title card feel).


* **Body Text:** You want something highly readable but slightly "off-beat."
* *Google Font Suggestions:* **"Patrick Hand"** (for a sketchbook feel) or **"Courier Prime"** (for that typewriter/zine aesthetic).



---

## 3. Visual Language & UI Components

To make it feel like an indie comic, you need to use **thick, inconsistent line weights.**

* **The "Double Border" Effect:** Give your containers a thick black border, but offset a second colorful border behind it to mimic the show's "bleeding" color style.
* **Halftone Patterns:** Use a subtle "Ben-Day dot" (halftone) pattern for background sections or hover effects. This screams "printed comic book."
* **Non-Right Angles:** The world of *Mission Hill* is slightly wonky. Use CSS `clip-path` or `transform: rotate(-1deg)` on images and blog cards so they don't look perfectly straight.

---

## 4. Jekyll-Specific Layout Ideas

Since you are posting blogs, videos, and drawings:

* **The "Zine" Grid:** Instead of a clean modern grid, give your blog previews different-sized "panels" like a comic book page.
* **Navigation:** Use "Signpost" icons. Instead of a standard menu, use a navigation bar that looks like the neon "Mission Hill Market" sign from your second image.
* **The "Sketchbook" Archive:** For your drawings, use a polaroid or "taped-to-the-wall" CSS effect where images have white borders and slight drop shadows.

---
