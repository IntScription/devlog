---
tags:
  
- html-css
  
- programming
---
The `position` property specifies the type of positioning method used for an element (static, relative, fixed, absolute or sticky).

## The position Property

The `position` property specifies the type of positioning method used for an element.

There are five different position values:

- `static`
- `relative`
- `fixed`
- `absolute`
- `sticky`

Elements are then positioned using the top, bottom, left, and right properties. However, these properties will not work unless the `position` property is set first. They also work differently depending on the position value.

## position: static;

HTML elements are positioned static by default.

Static positioned elements are not affected by the top, bottom, left, and right properties.

An element with `position: static;` is not positioned in any special way; it is always positioned according to the normal flow of the page:

This `<div>` element has `position: static;`

#### Example:

```css
div.static {
  position: static;  
  border: 3px solid #73AD21;
}
```

## position: relative;

An element with `position: relative;` is positioned relative to its normal position.

Setting the top, right, bottom, and left properties of a relatively-positioned element will cause it to be adjusted away from its normal position. Other content will not be adjusted to fit into any gap left by the element.

This `<div>` element has `position: relative;`

#### Example:

```css
div.relative {
  position: relative;  
  left: 30px;  
  border: 3px solid #73AD21;
}
```

## position: fixed;

An element with `position: fixed;` is positioned relative to the viewport, which means it always stays in the same place even if the page is scrolled. The top, right, bottom, and left properties are used to position the element.

A fixed element does not leave a gap in the page where it would normally have been located.

Notice the fixed element in the lower-right corner of the page. Here is the CSS that is used:

#### Example:

```css
div.fixed {  
  position: fixed;  
  bottom: 0;  
  right: 0;  
  width: 300px;  
  border: 3px solid #73AD21;
}
```

## position: absolute;

An element with `position: absolute;` is positioned relative to the nearest positioned ancestor (instead of positioned relative to the viewport, like fixed).

However; if an absolute positioned element has no positioned ancestors, it uses the document body, and moves along with page scrolling.

**Note:** Absolute positioned elements are removed from the normal flow, and can overlap elements.

#### Example:

```css
div.relative {  
  position: relative;  
  width: 400px;  
  height: 200px;  
  border: 3px solid #73AD21;
}  
  
div.absolute {  
  position: absolute;  
  top: 80px;  
  right: 0;  
  width: 200px;  
  height: 100px;  
  border: 3px solid #73AD21;
}
```

## position: sticky;

An element with `position: sticky;` is positioned based on the user's scroll position.

A sticky element toggles between `relative` and `fixed`, depending on the scroll position. It is positioned relative until a given offset position is met in the viewport 
- then it "sticks" in place (like position:fixed).

#### Example:

```css
div.sticky {  
  position: -webkit-sticky; /* Safari */  
  position: sticky;  
  top: 0;  
  background-color: green;  
  border: 2px solid #4CAF50;
}
```

---

## All Properties :

|Property|Description|
|---|---|
|[bottom](https://www.w3schools.com/cssref/pr_pos_bottom.php)|Sets the bottom margin edge for a positioned box|
|[clip](https://www.w3schools.com/cssref/pr_pos_clip.php)|Clips an absolutely positioned element|
|[left](https://www.w3schools.com/cssref/pr_pos_left.php)|Sets the left margin edge for a positioned box|
|[position](https://www.w3schools.com/cssref/pr_class_position.php)|Specifies the type of positioning for an element|
|[right](https://www.w3schools.com/cssref/pr_pos_right.php)|Sets the right margin edge for a positioned box|
|[top](https://www.w3schools.com/cssref/pr_pos_top.php)|Sets the top margin edge for a positioned box|

---

## **NOTE : 

- `fixed` is a `position` property value that lets you make an element fixed to the page no matter where the user scrolls to on the page.

---
