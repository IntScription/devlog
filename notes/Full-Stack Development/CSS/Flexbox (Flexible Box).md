---
tags:
  
- programming
  
- html-css
---
- Flexbox is a one-dimensional CSS layout that can control the way items are spaced out and aligned within a container
---

Flexbox has a main and cross axis. The main axis is defined by the `flex-direction` property, which has four possible values:

- `row` (default): horizontal axis with flex items from left to right
- `row-reverse`: horizontal axis with flex items from right to left
- `column`: vertical axis with flex items from top to bottom
- `column-reverse`: vertical axis with flex items from bottom to top

**Note**: The axes and directions will be different depending on the text direction. The values shown are for a left-to-right text direction.

---
### What is order ?

- Specifies order of the flex items

Example:

```css
<div class = "flex-container">  
  <div style = "order: 3">1</div>  
  <div style = "order: 2">2</div>  
  <div style = "order: 4">3</div>  
  <div style = "order: 1">4</div>  
</div>
```

### What is flex wrap ?

The `flex-wrap` property determines how your flex items behave when the flex container is too small. Setting it to `wrap` will allow the items to wrap to the next row or column. `nowrap` (default) will prevent your items from wrapping and shrink them if needed.

### What is justify content ?

The `justify-content` property determines how the items inside a flex container are positioned along the main axis, affecting their position and the space around them.

### What is align items ?

The `align-items` property positions the flex content along the cross axis. In this case, with your `flex-direction` set to `row`, your cross axis would be vertical.

### What is `::after` ?

The `::after` pseudo-element creates an element that is the last child of the selected element. You can use it to add an empty element after the last image. If you give it the same `width` as the images it will push the last image to the left when the gallery is in a two-column layout. Right now, it is in the center because you set `justify-content: center` on the flex container.

Example:

```css
.container::after {
  content: "";
  width: 860px;
}
```

---
