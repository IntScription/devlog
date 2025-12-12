# devlog

Welcome to my public developer log — a space where I document my daily progress, learning, and projects in software engineering, AI, and development tools.

You can visit the live site here:
🔗[IntScription](https://intscription.github.io/devlog/)

---

## ✨ Features

- **Dark/Light Mode Toggle** — Instantly switch between beautiful dark and light themes with a single click (icon in the header).
- **Live Typing Effect** — The home screen welcome message is animated with a live typing effect for a modern, dynamic feel.
- **Modern Navigation** — Clean, always-visible navigation for Home and Archive, with a sticky header and responsive design.
- **Beautiful Tables** — All markdown tables are styled for clarity, contrast, and mobile-friendliness.
- **Syntax Highlighting** — Code blocks are colored by language, supporting both dark and light modes.
- **Responsive & Accessible** — Looks great on desktop, tablet, and mobile.
- **Connect With Me** — Footer links to GitHub and YouTube.

---

## Folder Structure

```text
devlog/
├─ logs/           # Daily devlog entries
│   ├─ 2025-07-17/
│   │   └─ index.md
│   ├─ 2025-07-18/
│   │   └─ index.md
│   └─ ...
├─ scripts/        # Python automation scripts
│   ├─ fix_navigation.py      # Fix navigation links in devlog entries
│   ├─ fix_markdownlint.py    # Auto-fix markdownlint errors
│   ├─ convert_wikilinks.py   # Convert Obsidian wiki links to Markdown
│   └─ add_front_matter.py    # Add Jekyll front matter to notes
├─ index.md        # Main page (with live typing effect)
├─ assets/
│   ├─ css/
│   │   └─ main.scss   # All custom styles (dark/light, tables, code, etc.)
│   └─ js/
│       ├─ theme-toggle.js   # Dark/light mode toggle logic
│       └─ typed-home.js     # Live typing effect for home screen
├─ _layouts/
│   └─ default.html   # Custom layout with modern header/footer
├─ _config.yml     # Jekyll config
└─ README.md       # This file
```

---

## 🛠 How I Work on This

- Written entirely in [Neovim](https://github.com/IntScription/dotfiles/tree/main/config/nvim).
- Managed with git and lazygit.
- Hosted via GitHub Pages.

---

## 🚀 Quick Start (Local Dev)

```bash
bundle install
bundle exec jekyll serve
```

Then visit [http://localhost:4000/devlog/](http://localhost:4000/devlog/) in your browser.

---

## 🔧 Automation Scripts

The `scripts/` folder contains Python automation tools:

- **`fix_navigation.py`** — Fixes navigation links in all devlog entries
- **`fix_markdownlint.py`** — Automatically corrects markdownlint formatting errors
- **`convert_wikilinks.py`** — Converts Obsidian wiki links (`[[Link]]`) to standard Markdown
- **`add_front_matter.py`** — Adds Jekyll front matter to notes for proper rendering

These scripts run automatically via Git hooks to maintain code quality.
