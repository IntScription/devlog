---
tags:
  - html-css
  - programming
---
## Definition and Usage

The `transform` property applies a 2D or 3D transformation to an element. This property allows you to rotate, scale, move, skew, etc., elements.

## Property Values

|Value|Description|Demo|
|---|---|---|
|none|Defines that there should be no transformation|[Demo ❯](https://www.w3schools.com/CSSREF/playdemo.php?filename=playcss_transform&preval=none)|
|matrix(_n,n,n,n,n,n_)|Defines a 2D transformation, using a matrix of six values|[Demo ❯](https://www.w3schools.com/CSSREF/playdemo.php?filename=playcss_transform&preval=matrix(0.866,0.7,-0.8,0.866,0,0))|
|matrix3d  <br>(_n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n_)|Defines a 3D transformation, using a 4x4 matrix of 16 values||
|translate(_x,y_)|Defines a 2D translation|[Demo ❯](https://www.w3schools.com/CSSREF/playdemo.php?filename=playcss_transform&preval=translate(20px,10px))|
|translate3d(_x,y,z_)|Defines a 3D translation||
|translateX(_x_)|Defines a translation, using only the value for the X-axis||
|translateY(_y_)|Defines a translation, using only the value for the Y-axis||
|translateZ(_z_)|Defines a 3D translation, using only the value for the Z-axis||
|scale(_x,y_)|Defines a 2D scale transformation|[Demo ❯](https://www.w3schools.com/CSSREF/playdemo.php?filename=playcss_transform&preval=scale(2,3))|
|scale3d(_x,y,z_)|Defines a 3D scale transformation||
|scaleX(_x_)|Defines a scale transformation by giving a value for the X-axis||
|scaleY(_y_)|Defines a scale transformation by giving a value for the Y-axis||
|scaleZ(_z_)|Defines a 3D scale transformation by giving a value for the Z-axis||
|rotate(_angle_)|Defines a 2D rotation, the angle is specified in the parameter|[Demo ❯](https://www.w3schools.com/CSSREF/playdemo.php?filename=playcss_transform&preval=rotate(45deg))|
|rotate3d(_x,y,z,angle_)|Defines a 3D rotation||
|rotateX(_angle_)|Defines a 3D rotation along the X-axis|[Demo ❯](https://www.w3schools.com/CSSREF/playdemo.php?filename=playcss_transform&preval=rotateX(45deg))|
|rotateY(_angle_)|Defines a 3D rotation along the Y-axis|[Demo ❯](https://www.w3schools.com/CSSREF/playdemo.php?filename=playcss_transform&preval=rotateY(80deg))|
|rotateZ(_angle_)|Defines a 3D rotation along the Z-axis||
|skew(_x-angle,y-angle_)|Defines a 2D skew transformation along the X- and the Y-axis|[Demo ❯](https://www.w3schools.com/CSSREF/playdemo.php?filename=playcss_transform&preval=skew(20deg,20deg))|
|skewX(_angle_)|Defines a 2D skew transformation along the X-axis|[Demo ❯](https://www.w3schools.com/CSSREF/playdemo.php?filename=playcss_transform&preval=skewX(30deg))|
|skewY(_angle_)|Defines a 2D skew transformation along the Y-axis|[Demo ❯](https://www.w3schools.com/CSSREF/playdemo.php?filename=playcss_transform&preval=skewY(40deg))|
|perspective(_n_)|Defines a perspective view for a 3D transformed element||
|initial|Sets this property to its default value.  ||
|inherit|Inherits this property from its parent element. ||

---
