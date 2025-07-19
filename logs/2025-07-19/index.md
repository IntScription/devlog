---
layout: default
permalink: /logs/2025-07-19/
---

# Devlog - 2025-07-19

## 🚀 What I Did
- Went on trying to better my GitHub pages.
- Struggled for more than 5 hours I suppose.
- Well in the end I just concluded on not using any styling for time being since its anyways following minima's base configuration.

## 🧠 What I Learned
- Jekyll Language is written in Ruby.
- Bundler(Ruby tool) - manages packages and correct versions of gems.
- Gemfile lists all the gems(eg. Jekyll, minima).
- `bundle install` - installs exactly what's in the gemfile and locks in Gemfile.lock so site works consistently on your machine.
- `bundle exec jekyll serve` - Jekyll using the versions specified in your bundle.
- `bundle exec jekyll clean` - It clears out the _site/ directory (or any other temporary files Jekyll creates during builds).
- `bundle exec jekyll build` - It builds your static site from your source files (Markdown, SCSS, layouts, etc.) and outputs it into the _site/ directory.

```bash
bundle exec jekyll clean   # Clean up old site
bundle exec jekyll build   # Build the site fresh
bundle exec jekyll serve   # Run the local dev server to preview
```

### What is Minima ?
- Minima is the default Jekyll theme.
- It's a minimal, clean theme designed to help you get started fast with blogging.
- 📂 Files you often see from minima:

```text
_layouts/
    default.html
    home.html
    post.html
    page.html

_includes/
    header.html
    footer.html
    social.html
```


## 🔥 What's Next
- Data Structures and Algorithms.
- CS50 Harvard.

---

<div class="nav-links">
<a href="{{ site.baseurl }}/logs/2025-07-18/">← Previous</a>

</div>
