# Email Signup Form Component

A Mission Hill-styled email signup form with toxic lime shadow, thick borders, and a neon comic book aesthetic.

## Basic Usage

Add the following to any post or page:

```liquid
{% include email-signup.html %}
```

This uses default text:
- **Title**: "Join the Mailing List!"
- **Description**: "Get new comics, behind-the-scenes content, and exclusive downloads delivered straight to your inbox."
- **Button**: "Sign Me Up!"

## Custom Usage

Customize the text for promotions or free downloads:

```liquid
{% include email-signup.html 
   title="Download the Free Comic!"
   description="Enter your email to get a free 10-page comic PDF sent straight to your inbox."
   cta="Get My Free Comic" %}
```

## Parameters

All parameters are optional:

- `title` - Heading text for the signup form
- `description` - Descriptive text below the heading
- `cta` - Button text (call-to-action)

## Setup Required

Before going live, update the form action in `_includes/email-signup.html` (around line 55) with your email service provider's endpoint:

### Popular Email Service Providers:

**Buttondown** ($9/mo for 1000 subscribers)
```html
action="https://buttondown.email/api/emails/embed-subscribe/[your-username]"
```

**Mailchimp** (Free up to 500 subscribers)
```html
action="[Your Mailchimp embed form action URL]"
```

**ConvertKit** (Free up to 300 subscribers)
```html
action="[Your ConvertKit form endpoint]"
```

## Styling

Styles are in `assets/css/main.css` under the "EMAIL SIGNUP COMPONENT" section.

The form features:
- Toxic lime shadow with thick black borders
- Blue title with lime text-shadow
- Wonky rotation for hand-drawn feel
- Neon orchid dashed border accent
- Hover effects on input and button
- Fully responsive (stacks on mobile at 640px)

## Example Post

See `_posts/2026-01-04-email-signup-example.md` for a complete example showing different ways to use the signup form.

## Files

- **Include**: `_includes/email-signup.html`
- **Styles**: `assets/css/main.css` (lines 1843-1987)
- **Example**: `_posts/2026-01-04-email-signup-example.md`
