---
tags:
  - html-css
  - programming
---
- There are different types of units that can be defined

### Absolute Units

- Always same in any content

 `px` is an absolute unit because the size of a pixel doesn’t change relative to anything else on the page. In fact, `px` is the only absolute unit you should be using for web projects. The rest of them make more sense in a print setting because they are related to physical units such as `in` (inch) and `cm` (centimeter).

### Relative Units

- Can be changed based on their content

#### em and rem

- `em` and `rem` both refer to a font size, though they are often used to define other sizes in CSS
- `1em` is the `font-size` of an element (or the element’s parent if you’re using it to set `font-size`). So, for example, if an element’s `font-size` is `16px`, then setting its width to `4em` would make its width `64px` (`16 * 4 == 64`)
- `1rem` is the `font-size` of the root element (either `:root` or `html`). The math works the same with `rem` as it did with `em`, but without the added complexity of keeping track of the parent’s font size. Relying on `em` could mean that a particular size could change if the context changes, which is very likely not the behaviour you want
- The rem unit is only relative to the document's root element, while the em unit is only relative to the immediate parent of the targeted element

#### Viewport Units

- The units `vh` and `vw` relate to the size of the viewport
- Specifically, `1vh` is equal to `1%` of the viewport height and `1vw` is equal to `1%` of the viewport width

---


