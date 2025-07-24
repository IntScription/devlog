---
tags:
  
- programming
  
- html-css
---
## What is CSS ?

- Cascading Style Sheets (CSS)
- A style sheet language used for specifying the presentation and styling of a document written in a markup language such as HTML or XML
- Describes how html elements are displayed on screen
- Can control multiple web pages at once
- External style sheets are stored in CSS files

### Example :

```CSS
body {  
   background-color: lightblue;
}  
  
h1 { 
   color: white;  
   text-align: center;
}  
  
p {
  font-family: verdana;  
  font-size: 20px;
}
```

---
## **NOTE**

- Typeface plays an important role in the accessibility of a page. Some fonts are easier to read than others, and this is especially true on low-resolution screens.
-  While `ul`/`li` elements are great at providing bullets for list items, your radio buttons don't need them. You can control what the bullets look with the `list-style` property. For example you can turn your bullets into circles with the following:

```css
ul {
  list-style: circle;
}
```

- The `calc()` function is a CSS function that allows you to calculate a value based on other values. For example, you can use it to calculate the width of the viewport minus the margin of an element:

```css
.example {
  margin: 10px;
  width: calc(100% 
- 20px);
}
```

- The `[attribute="value"]` selector targets any element that has an attribute with a specific value.
- The `transform` property allows you to modify the shape, position, and size of an element without changing the layout or affecting the surrounding elements. It has functions such as `translate()`, `rotate()`, `scale()`, `skew()`, and `matrix()`

---

>[!CHEAT SHEET]
>[CSS cheat sheet](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)

---
