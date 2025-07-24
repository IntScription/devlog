---
tags:
  
- html-css
  
- programming
---
Certain types of motion-based animations can cause discomfort for some users. In particular, people with vestibular disorders have sensitivity to certain motion triggers.

The `@media` at-rule has a media feature called `prefers-reduced-motion` to set CSS based on the user's preferences. It can take one of the following values:

- `reduce`
- `no-preference`

```css
@media (feature: value) {
  selector {
    styles
  }
}
```

## Definition and Usage

Media queries can be used to check many things, such as:

- width and height of the viewport
- width and height of the device
- orientation (is the tablet/phone in landscape or portrait mode?)
- resolution

Using media queries are a popular technique for delivering a tailored style sheet (responsive web design) to desktops, laptops, tablets, and mobile phones.

You can also use media queries to specify that certain styles are only for printed documents or for screen readers (mediatype: print, screen, or speech).

In addition to media types, there are also media features. Media features provide more specific details to media queries, by allowing to test for a specific feature of the user agent or display device. For example, you can apply styles to only those screens that are greater, or smaller, than a certain width.

- The `@media` at-rule, also known as a media query, is used to conditionally apply CSS. Media queries are commonly used to apply CSS based on the viewport width using the `max-width` and `min-width` properties.

```css
@media (max-width: 960px) {
  .card {
    padding: 2rem;
  }
}
```

---


