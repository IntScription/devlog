---
tags:
  - html-css
  - programming
---
Gradients in CSS are a way to transition between colours across the distance of an element. They are applied to the `background` property and the syntax looks like this:

```css
gradient-type(
  color1,
  color2
);
```

CSS defines three types of gradients:

- **Linear Gradients (goes down/up/left/right/diagonally)**
- **Radial Gradients (defined by their center)**
- **Conic Gradients (rotated around a center point)**

## CSS Linear Gradients

To create a linear gradient you must define at least two colour stops. Colour stops are the colours you want to render smooth transitions among. You can also set a starting point and a direction (or an angle) along with the gradient effect.

```css
background-image: linear-gradient(direction, color-stop1, color-stop2, ...);
```

### Using Angles

If you want more control over the direction of the gradient, you can define an angle, instead of the predefined directions (to bottom, to top, to right, to left, to bottom right, etc.). A value of 0deg is equivalent to "to top". A value of 90deg is equivalent to "to right". A value of 180deg is equivalent to "to bottom".

```css
background-image: linear-gradient(angle, color-stop1, color-stop2);
```

### Using Transparency

CSS gradients also support transparency, which can be used to create fading effects.

To add transparency, we use the rgba() function to define the colour stops. The last parameter in the rgba() function can be a value from 0 to 1, and it defines the transparency of the colour: 0 indicates full transparency, 1 indicates full colour (no transparency).

Eg:

```css
#grad {  
background-image: linear-gradient(to right, rgba(255,0,0,0), rgba(255,0,0,1));
}
```

### Repeating a linear-gradient

The repeating-linear-gradient() function is used to repeat linear gradients

Eg:

```css
#grad {  
background-image: repeating-linear-gradient(red, yellow 10%, green 20%);
}
```

---
## CSS Radial Gradients

A radial gradient is defined by its center. To create a radial gradient you must also define at least two colour stops.

```css
background-image: radial-gradient(shape size at position, start-color, ..., last-color);
```


### Set Shape

The shape parameter defines the shape. It can take the value circle or ellipse. The default value is ellipse.

Eg:

```css
#grad { 
 background-image: radial-gradient(circle, red, yellow, green);
}
```

### Use of Different Size Keywords

The size parameter defines the size of the gradient. It can take four values:

- **closest-side**
- **farthest-side**
- **closest-corner**
- **farthest-corner**

#### Example:

```css
#grad1 {  
background-image: radial-gradient(closest-side at 60% 55%, red, yellow, black);
}  
  
#grad2 {  
background-image: radial-gradient(farthest-side at 60% 55%, red, yellow, black);
}
```

### Repeating a radial-gradient

The repeating-radial-gradient() function is used to repeat radial gradients

Eg:

```css
#grad {  
background-image: repeating-radial-gradient(red, yellow 10%, green 15%);
}
```

---
## CSS Conic Gradients

A conic gradient is a gradient with colour transitions rotated around a center point.

```css
background-image: conic-gradient([from angle] [at position,] color [degree], color [degree], ...);
```

Eg:

```css
#grad { 
 background-image: conic-gradient(red, yellow, green);
}
```

### Conic Gradient: Three Colours and Degrees

Eg:

```css
#grad {
background-image: conic-gradient(red 45deg, yellow 90deg,    green 210deg);
}
```

### Create Pie Charts

Just add `border-radius: 50%` to make the conic gradient look like a pie

Eg:

```css
#grad {  
  background-image: conic-gradient(red, yellow, green, blue,  black);  
  border-radius: 50%;
}
```

### Conic Gradient With Specified From Angle

The `[from angle]` specifies an angle that the entire conic gradient is rotated by.

Eg:

```css
#grad { 
 background-image: conic-gradient(from 90deg, red, yellow, green);
}
```

## Conic Gradient With Specified Center Position

The `[at position]` specifies the center of the conic gradient.

Eg:

```css
#grad {  
 background-image: conic-gradient(at 60% 45%, red, yellow, green);
}
```

### Repeating a Conic Gradient

The `repeating-conic-gradient()` function is used to repeat conic gradients

Eg:

```css
#grad {  
 background-image: repeating-conic-gradient(red 10%, yellow 20%);  
  border-radius: 50%;
}
```

---
## CSS Gradient Functions

The following table lists the CSS gradient functions:

|Function|Description|
|---|---|
|[conic-gradient()](https://www.w3schools.com/cssref/func_conic-gradient.asp)|Creates a conic gradient. Define at least two colors (around a center point)|
|[linear-gradient()](https://www.w3schools.com/cssref/func_linear-gradient.asp)|Creates a linear gradient. Define at least two colors (top to bottom)|
|[radial-gradient()](https://www.w3schools.com/cssref/func_radial-gradient.asp)|Creates a radial gradient. Define at least two colors (center to edges)|
|[repeating-conic-gradient()](https://www.w3schools.com/cssref/func_repeating-conic-gradient.asp)|Repeats a conic gradient|
|[repeating-linear-gradient()](https://www.w3schools.com/cssref/func_repeating-linear-gradient.asp)|Repeats a linear gradient|
|[repeating-radial-gradient()](https://www.w3schools.com/cssref/func_repeating-radial-gradient.asp)|Repeats a radial gradient|

---
