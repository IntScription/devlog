---
layout: default
permalink: /logs/2025-09-17/
---

# Devlog - 2025-09-17

## 🚀 What I Did

- Video Compilation.

## 🧠 What I Learned

### Replacement element

- Style layout and positioning.
- It is replaced with an external object.

```html
<iframe
  src="video-url"
  width="width-value"
  height="height-value"
  allowfullscreen
></iframe>
```

- `iframe` - inline frame(element used to embed other HTML content directly within the HTML page).
- `allowfullscreen` attribute allows the user to display the iframe in full screen mode.
- If you want to embed direct HTML within the iframe element you have to use the `srcdoc` attribute instead of `src`.

### Target values

```html
<a href="https://freecodecamp.org" target="_blank">Visit freeCodeCamp</a>
```

- `_self` → default, opens in the same tab/window.
- `_blank` → opens in a new tab (or window, depending on browser).
- `_parent` → opens in the parent frame (useful inside iframes).
- `_top` → opens in the full tab/window, ignoring nested frames.
- `_unfencedTop` → experimental, for FencedFrame API.

### Path

- Simple string that tells where a file or directory is located.

1. Absolute Path = full address (good for external links).
2. Relative Path = shortcut (good for internal project files).

### Order of styling links

`:link` → default state (not yet visited or clicked).
`:visited` → link already visited (default purple).
`:hover` → when cursor is over the link.
`:focus` → when the link is focused (e.g., via keyboard/tab).
`:active` → when the link is being clicked/activated.

## 🔥 What's Next

- Semantic HTML.

---

[← Previous]({{site.baseurl}}/logs/2025-09-16/) | [Next →]({{site.baseurl}}/logs/2025-09-19/)
