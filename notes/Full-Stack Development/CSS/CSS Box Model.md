---
tags:
  - programming
  - html-css
---
- Is a container that contains multiple properties including borders, margins, padding, and the content itself

![CSS Box Model.png](CSS-Box-Model.png)

- **Content Area:** This area consists of content like text, images, or other media content. It is bounded by the content edge and its dimensions are given by content-box width and height.
- **Padding Area:** It includes the element’s padding. This area is actually the space around the content area and within the border-box. Its dimensions are given by the width of the padding-box and the height of the padding-box.
- [**Border Area:**](https://www.geeksforgeeks.org/css-border-property/) It is the area between the box’s padding and margin. Its dimensions are given by the width and height of the border.
- **Margin Area:** This area consists of space between the border and the margin. The dimensions of the Margin area are the margin-box width and the margin-box height. It is useful to separate the element from its neighbours.

### Example :

```css
p {  
    width: 80px;  
    height: 70px;  
    margin: 0;  
    border: 2px solid black;  
    padding: 5px;  
}
```

---
