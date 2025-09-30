---
layout: default
permalink: /logs/2025-09-27/
---

# Devlog - 2025-09-27

## 🚀 What I Did

- CSS Theory.

## 🧠 What I Learned

### Specificity values are calculated as a four-part value (a, b, c, d)

- a: Inline styles (1 or 0).
- b: Number of ID selectors.
- c: Number of class selectors, attribute selectors, and pseudo-classes.
- d: Number of type selectors, pseudo-elements, and universal selectors.

### Each part of the specificity value carries different weight

- Inline styles (a): Highest weight → 1st part of specificity.
- ID selectors (b): Next highest → 2nd part.
- Classes, attributes, pseudo-classes (c): Moderate → 3rd part.
- Type selectors & pseudo-elements (d): Lowest → 4th part.
- Universal selector (*): No weight → 0 contribution.

```css
* {
  margin: 0;
  padding: 0;
}
```

- `!important` - used to give a style rule the highest priority, allowing it to override any other declarations for a property.

```css
.para {
  background-color: black !important;
  color: white !important;
}
```

### Cascade Algorithms

- Cascade = Importance → Specificity → Source order.
- Order of importance:
- `!important (author)` > `!important (user)` > `normal author` > `normal user` > `browser default`
- `Inline styles` > `IDs` > `Classes/Attributes/Pseudo-classes` > `Type selectors/Pseudo-elements` > `Universal *`
- Source order - If two rules have the same importance and specificity, the one written last in the CSS wins.

### `list-style` property

- `list-style-type`
- `list-style-position`
- `list-style-image`

## 🔥 What's Next

- To-Do-List.

---

[← Previous]({{site.baseurl}}/logs/2025-09-25/) | [Next →]({{site.baseurl}}/logs/2025-09-30/)
