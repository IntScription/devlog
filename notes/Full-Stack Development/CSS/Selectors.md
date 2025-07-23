---
tags:
  - html-css
  - programming
---
## CSS Selectors

- Used to find the html element you want to style

### Types of Selectors

- Simple selectors (select elements based on name, id, class)
- [Combinator selectors](https://www.w3schools.com/css/css_combinators.asp) (select elements based on a specific relationship between them)
- [Pseudo-class selectors](https://www.w3schools.com/css/css_pseudo_classes.asp) (select elements based on a certain state)
- [Pseudo-elements selectors](https://www.w3schools.com/css/css_pseudo_elements.asp) (select and style a part of an element)
- [Attribute selectors](https://www.w3schools.com/css/css_attribute_selectors.asp) (select elements based on an attribute or attribute value)

---
## What is `:not` ?

The `:not` pseudo-selector can be used to select all elements that do not match the given CSS rule.

```css
div:not(#example) {
  color: red;
}
```

---

## **NOTE**

- The `:nth-of-type()` pseudo-selector is used to target specific elements based on their order among siblings of the same type.

---
