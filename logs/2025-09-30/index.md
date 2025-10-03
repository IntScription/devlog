---
layout: default
permalink: /logs/2025-09-30/
---

# Devlog - 2025-09-30

## 🚀 What I Did

- [Todo list](https://github.com/IntScription/web-development/tree/main/html-css/todo-list)
- [Blog Post](https://github.com/IntScription/web-development/tree/main/html-css/General-Blog-Post)

## 🧠 What I Learned

```html
<a href="https://example.com" target="_blank" rel="noopener noreferrer">Example</a>
```

- Secure (no window.opener hijacking).
- Private (no referrer info leaked).

### 🔒 `rel="noopener"`

- Prevents the new page from having access to window.opener.
- That means the new site cannot run malicious JavaScript to, for example:
- Redirect your original page to a phishing site.
- Read or manipulate content on your page.

### 🚀 `rel="noreferrer"`

- Does the same as noopener, but also removes the HTTP referrer header.
- That means the site you open won’t see the URL of the page it was opened from.
- It’s a privacy measure — the target site won’t know exactly where the user came from.

## 🔥 What's Next

- Flexbox and grids.

---

[← Previous]({{site.baseurl}}/logs/2025-09-27/) | [Next →]({{site.baseurl}}/logs/2025-10-03/)
