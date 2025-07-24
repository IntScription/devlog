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
├─ notes/           # Personal notes, organized by topic/folder
│   ├─ Computer Networks and Communication/
│   ├─ Git/
│   ├─ Java/
│   ├─ Full-Stack Development/
│   ├─ Google Cybersecurity/
│   └─ ...
│
│   # Each folder contains Markdown notes, which are grouped and listed on the Notes index page
│   # To add new notes, place a .md file in the appropriate folder
│
│   # The Notes section is accessible from the site header and is organized by these folders
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

## 📝 Notes Section

- All notes are organized by topic in the `notes/` directory (see above).
- The Notes index page automatically groups notes by folder (e.g., Java, Git, Full-Stack Development, etc.).
- To add a new note, simply add a Markdown file to the appropriate folder in `notes/`.
- The Notes section is accessible from the site header navigation.
