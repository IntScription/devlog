---
tags:
  
- html-css
  
- programming
---
## Definition and Usage

- The `@keyframes` rule specifies the animation code.
- The animation is created by gradually changing from one set of CSS styles to another.
- During the animation, you can change the set of CSS styles many times.
- Specify when the style change will happen in percent, or with the keywords "from" and "to", which is the same as 0% and 100%. 0% is the beginning of the animation, 100% is when the animation is complete.

>[!NOTE]
>
-  For best browser support, you should always define both the 0% and the 100% selectors.
>
-  Use the animation properties to control the appearance of the animation, and also to bind the animation to selectors.
>
- The !important rule is ignored in a keyframe


## Property Values

|Value|Description|
|---|---|
|_animationname_|Required. Defines the name of the animation.|
|_keyframes-selector_|Required. Percentage of the animation duration.<br><br>Legal values:<br><br>0-100%  <br>from (same as 0%)  <br>to (same as 100%)<br><br>**Note:** You can have many keyframes-selectors in one animation.|
|_css-styles_|Required. One or more legal CSS style properties|

### Example:

```css
@keyframes mymove {  
  0%   {top: 0px; left: 0px; background: red;}  
  25%  {top: 0px; left: 100px; background: blue;}  
  50%  {top: 100px; left: 100px; background: yellow;}  
  75%  {top: 100px; left: 0px; background: green;}  
  100% {top: 0px; left: 0px; background: red;}
}
```

---
