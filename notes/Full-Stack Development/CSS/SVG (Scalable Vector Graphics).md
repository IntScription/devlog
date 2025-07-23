---
tags:
  - html-css
  - programming
---
A useful property of an _SVG_ (scalable vector graphics) is that it contains a `path` attribute which allows the image to be scaled without affecting the resolution of the resultant image.

Currently, the `img` is assuming its default size, which is too large. CSS has a `max` function which returns the largest of a set of comma-separated values. For example:

```css
img {
  width: max(250px, 25vw);
}
```

In this example, `img` elements will have a minimum width of `250px`. And as the viewport grows, the image will grow accordingly to be 25 percent of the viewport width.

---

## What is SVG ?

SVGs are a _scalable_ image format, which means they will easily scale to any size and retain their quality without increasing their filesize. They’re also very useful if you need to create or modify your images programmatically, because you can change their properties through CSS and JavaScript.

SVGs are often used for:

1. Icons
2. Graphs/Charts
3. Large, simple images
4. Patterned backgrounds
5. Applying effects to other elements via SVG filters


### What is Vector Graphics?

- Vector graphics are images defined by math, as opposed to traditional “raster graphics”, where your image is defined by a grid of pixels
- With raster graphics, the detail is limited to the size of that pixel grid. If you want to increase the size of the image (_scale_ it), you have to increase the size of that grid
- The larger the grid, the bigger your file size grows

---

- SVG's are defined using XML (Extensible Markup Language)

Example:

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
    <rect x=0 y=0 width=100 height=50 />
    <circle class="svg-circle" cx="50" cy="50" r="10"/>
</svg>
```

- SVGs are _great_ for relatively simple images, but because every single detail of the image needs to be written out as XML, they are extremely inefficient at storing complex images

---

## Anatomy of SVG

1. `xmlns` - stands for “XML NameSpace”. This specifies what _dialect_ of XML you’re using. In our case, that dialect is the SVG language spec. Without it, some browsers will not render your image or will render it incorrectly. If you’re interested in a full breakdown of what this attribute is and why it’s necessary, check out [this excellent MDN article](https://developer.mozilla.org/en-US/docs/Web/SVG/Namespaces_Crash_Course).
2. `viewBox` - defines the bounds of your SVG. When you have to define the positions of different points of the elements in your SVG, this is what that’s referencing. It also defines the aspect ratio _and_ the origin of your SVG. So it’s doing quite a lot! Be sure to play around with different values in the example above to get a feel for how it affects the shapes.
3. `class`, `id` - these attributes function just like they do in HTML. Using these in SVGs allows you to easily target an element via CSS or JavaScript, or to reuse an element via the [`use` element](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/use).
4. Elements such as `<circle>`, `<rect>`, `<path>`, and `<text>` are defined by the SVG namespace. These are our basic building-blocks. Although you can make extremely complex images with SVG, they are mostly created with just a dozen or so of these basic elements. You can see a complete list of SVG elements [here](https://developer.mozilla.org/en-US/docs/Web/SVG/Element).
5. Many SVG attributes, such as `fill` and `stroke`, can be [changed in your CSS](https://css-tricks.com/svg-properties-and-css/)

---

