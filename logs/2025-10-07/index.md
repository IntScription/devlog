---
layout: default
permalink: /logs/2025-10-07/
---

# Devlog - 2025-10-07

## 🚀 What I Did

- Playing cards.

## 🧠 What I Learned

### Flexbox and Flexmodel

- Main axis – direction of items (set by flex-direction).
- Cross axis – perpendicular to the main axis.

#### flex-direction

Defines the direction of flex items:

- row → horizontal (default)
- row-reverse → horizontal reversed
- column → vertical
- column-reverse → vertical reversed

#### flex-wrap

Controls whether items wrap when space runs out:

- nowrap → no wrapping (default)
- wrap → moves items to a new line when needed
- wrap-reverse → wraps in reverse order

```css
flex-flow: column wrap-reverse;
```

#### justify-content

Aligns items along the main axis:

- flex-start → start
- flex-end → end
- center → center
- space-between → equal space between items
- space-around → space around each item
- space-evenly → equal space between and around

#### align-items

Aligns items along the cross axis:

- flex-start → start of cross axis
- center → centered vertically/horizontally
- stretch → items stretch to fill space

### Typography

- The art of arranging text to make it readable and visually appealing.

#### Font Properties

- Weight: Thickness (light, bold).
- Style: Italic or normal.
- Width: Condensed or expanded.

#### Text Anatomy

- Baseline: Line letters sit on.
- Cap Height: Height of uppercase letters.
- X-height: Height of lowercase letters.
- Ascenders/Descenders: Parts extending above or below main body.

#### Spacing

- Kerning: Space between pairs of letters.
- Tracking: Space across all letters.
- Leading: Space between lines of text.

#### Best Practices

- Use simple, readable fonts (2–3 max).
- Create hierarchy with font sizes.
- Avoid too many fonts for visual consistency.

```css
font-family: Arial, "Times New Roman", sans-serif;
```

### Accessibility Tree

A structure used by screen readers to interpret and interact with the content on a webpage.

## 🔥 What's Next

- Css - positioning, attribute selectors and responsive design.

---

[← Previous]({{site.baseurl}}/logs/2025-10-06/) | [Next →]({{site.baseurl}}/logs/2025-10-08/)
