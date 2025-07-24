---
tags:
  - html-css
  - programming
---
## Definition and Usage

- The `transform-origin` property allows you to change the position of transformed elements.
- 2D transformations can change the x- and y-axis of an element. 3D transformations can also change the z-axis of an element.
- The `transform-origin` property is used to set the point around which a CSS transformation is applied. For example, when performing a `rotate`, the `transform-origin` determines around which point the element is rotated.

**Note:** This property must be used together with the [Transform Property](Transform-Property).

## Property Values

|Property Value|Description|
|---|---|
|_x-axis_|Defines where the view is placed at the x-axis. Possible values:<br><br>- left<br>- center<br>- right<br>- _length_<br>- _%_|
|_y-axis_|Defines where the view is placed at the y-axis. Possible values:<br><br>- top<br>- center<br>- bottom<br>- _length_<br>- _%_|
|_z-axis_|Defines where the view is placed at the z-axis (for 3D transformations). Possible values:<br><br>- _length_|
|initial|Sets this property to its default value. |
|inherit|Inherits this property from its parent element.  |

---
