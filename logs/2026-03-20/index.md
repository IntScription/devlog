---
layout: default
permalink: /logs/2026-03-20/
---

# Devlog - 2026-03-20

# Frontend Frameworks & Build Tools Explained

This guide explains the difference between **frameworks**, **libraries**, and **build tools**, along with when to use each.

---

## 🧠 1. Big Picture

There are 3 main things in modern frontend development:

| Category | Purpose | Examples |
|----------|--------|----------|
| Language | Core programming language | JavaScript |
| UI Library / Framework | Build user interfaces | React, Vue, Svelte |
| Build Tool | Run & bundle your app | Vite, Webpack, Parcel |
| Full-stack Framework | Adds routing, backend, SSR | Next.js, Nuxt, SvelteKit |

---

## ⚙️ 2. UI Libraries / Frameworks

These are used to build the actual interface (buttons, forms, UI).

---

### 🔹 React

- A **JavaScript library** for building UI
- Uses **JSX** (JavaScript + HTML mix)
- Very flexible and widely used

#### Example

```jsx
function App() {
  return <h1>Hello World</h1>;
}
```

#### 👉 Best for

- dashboards
- web apps
- industry projects

### 🔹 Vue

- A progressive framework
- Uses HTML templates + JavaScript

#### Example

```vue
<template>
  <h1>{{ message }}</h1>
</template>

<script>
export default {
  data() {
    return { message: "Hello World" };
  }
};
</script>
```

#### 👉 Best for

- beginners
- structured apps
- clean UI development

### 🔹 Svelte

- A compiler-based framework
- No virtual DOM
- Very lightweight

```svelte
<script>
  let count = 0;
</script>

<button on:click={() => count++}>
  {count}
</button>
```

#### 👉 Best for

- high performance apps
- simple & clean codebases

## 🔥 3. Build Tools

These tools run your app locally and prepare it for production.

---

### 🔹 Vite

- Fast development server
- Simple setup
- Modern build system

#### Example

```bash
npm create vite@latest
npm run dev
```

#### 👉 Best for

- Small to medium apps
- Assignments
- Dashboards

---

### 🔹 Webpack

- Older, very powerful bundler
- Highly configurable

#### 👉 Best for

- Large enterprise apps
- Custom build pipelines

---

### 🔹 Parcel

- Zero-config bundler
- Easy to start

#### 👉 Best for

- Beginners
- Quick prototypes

---

## 🧩 4. Full-Stack Frameworks

These extend UI frameworks and provide routing, server-side rendering, and backend features.

---

### 🔹 Next.js (React)

- Full-stack React framework

#### Supports

- Routing
- API routes
- Server-side rendering

#### Example

```jsx
export default function Page() {
  return <h1>Hello from Next.js</h1>;
}
```

#### 👉 Best for

- SaaS apps
- Production apps
- SEO-heavy websites

#### 🔹 Nuxt (Vue)

- Full-stack framework for Vue
- Similar to Next.js but for Vue

#### 👉 Best for

- Vue-based full apps
- SSR websites

### 🔹 SvelteKit

- Full-stack framework for Svelte
- Supports multiple rendering strategies

#### 👉 Best for

- Performance-focused apps

### 🔹 Astro

- Focused on content websites
- Sends minimal JavaScript

#### 👉 Best for

- Blogs
- Portfolios
- Documentation sites

## ⚖️ 5. Comparison Table

### UI Frameworks

| Feature         | React        | Vue           | Svelte         |
|----------------|-------------|--------------|----------------|
| Type           | Library     | Framework    | Compiler       |
| Learning Curve | Medium      | Easy         | Easy           |
| Performance    | High        | High         | Very High      |
| Flexibility    | Very High   | Medium       | Medium         |
| Ecosystem      | Huge        | Large        | Growing        |
| Best For       | Apps        | Structured UI| Performance apps |

---

### Build Tools

| Feature         | Vite         | Webpack      | Parcel       |
|----------------|-------------|-------------|-------------|
| Speed          | Very Fast    | Slower       | Fast        |
| Config         | Minimal      | Complex      | Zero        |
| Modern Support | Excellent    | Good         | Good        |
| Best For       | Modern apps  | Enterprise   | Beginners   |

---

### Full-Stack Frameworks

| Feature         | Next.js       | Nuxt        | SvelteKit      | Astro           |
|----------------|--------------|------------|----------------|-----------------|
| Based On       | React         | Vue         | Svelte         | Multi-framework |
| SSR Support    | Yes           | Yes         | Yes            | Yes             |
| Backend Support| Yes           | Yes         | Yes            | Limited         |
| Best For       | SaaS / Apps   | Vue Apps    | Performance Apps| Content Sites   |
| Learning Curve | Medium        | Medium      | Easy           | Easy            |

## 🧠 6. How to Choose

Choose based on your project:

| Project Type              | Best Choice        |
|--------------------------|--------------------|
| Small App / Assignment   | React + Vite       |
| Full Product / SaaS      | Next.js            |
| Blog / Portfolio         | Astro              |
| Vue App                  | Nuxt               |
| Performance-focused App  | SvelteKit          |

---

## 🎯 7. Simple Summary

- React / Vue / Svelte → Build UI
- Vite / Webpack / Parcel → Run & build your app
- Next.js / Nuxt / SvelteKit / Astro → Full app frameworks

---

[← Previous]({{site.baseurl}}/logs/2026-02-05/)
