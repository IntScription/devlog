---
tags:
  - html-css
  - programming
---
## Definition and Usage

The `animation` property is a shorthand property for:

- animation-name
- animation-duration
- animation-timing-function
- animation-delay
- animation-iteration-count
- animation-direction
- animation-fill-mode
- animation-play-state

**Note:** Always specify the animation-duration property, otherwise the duration is 0, and will never be played.

### Animation Delay

- The `animation-delay` property specifies a delay for the start of an animation.
- The animation-delay value is defined in seconds (s) or milliseconds (ms).

#### Property Values

| Value | Description |
| ---- | ---- |
| _time_ | Optional. Defines the number of seconds (s) or milliseconds (ms) to wait before the animation will start. Default value is 0. Negative values are allowed. If you use negative values, the animation will start as if it had already been playing for _N_ seconds/milliseconds. |
| initial | Sets this property to its default value. |
| inherit | Inherits this property from its parent element. |

Eg:

```css
div {  
 animation-delay: -2s;
}
```

### Animation Direction

The `animation-direction` property defines whether an animation should be played forwards, backwards or in alternate cycles.

#### Property Values

| Value | Description |
| ---- | ---- |
| normal | Default value. The animation is played as normal (forwards) |
| reverse | The animation is played in reverse direction (backwards) |
| alternate | The animation is played forwards first, then backwards |
| alternate-reverse | The animation is played backwards first, then forwards |
| initial | Sets this property to its default value.  |
| inherit | Inherits this property from its parent element.  |

Eg:

```css
div {  
 animation-direction: alternate-reverse;
}
```

### Animation Duration

The `animation-duration` property defines how long an animation should take to complete one cycle.

#### Property Values

| Value | Description |
| ---- | ---- |
| _time_ | Specifies the length of time an animation should take to complete one cycle. This can be specified in seconds or milliseconds. Default value is 0, which means that no animation will occur |
| initial | Sets this property to its default value. |
| inherit | Inherits this property from its parent element. |

Eg:

```css
div {  
 animation-duration: 3s;
}
```

### Animation Fill Mode

- The `animation-fill-mode` property specifies a style for the element when the animation is not playing (before it starts, after it ends, or both).
- CSS animations do not affect the element before the first keyframe is played or after the last keyframe is played. The `animation-fill-mode` property can override this behaviour.

#### Property Values

|Value|Description|
|---|---|
|none|Default value. Animation will not apply any styles to the element before or after it is executing|
|forwards|The element will retain the style values that is set by the last keyframe (depends on animation-direction and animation-iteration-count)|
|backwards|The element will get the style values that is set by the first keyframe (depends on animation-direction), and retain this during the animation-delay period|
|both|The animation will follow the rules for both forwards and backwards, extending the animation properties in both directions|
|initial|Sets this property to its default value.  |
|inherit|Inherits this property from its parent element. |

Eg:

```css
div {  
 animation-fill-mode: backwards;
}
```

### Animation Iteration Count

The `animation-iteration-count` property specifies the number of times an animation should be played.

#### Property Values

| Value | Description |
| ---- | ---- |
| _number_ | A number that defines how many times an animation should be played. Default value is 1 |
| infinite | Specifies that the animation should be played infinite times (for ever) |
| initial | Sets this property to its default value. |
| inherit | Inherits this property from its parent element. |
Eg:

```css
div {  
 animation-iteration-count: infinite;
}
```

### Animation Name

The `animation-name` property specifies a name for the [[@keyframes Rule]] animation.

#### Property Values

| Value | Description |
| ---- | ---- |
| _keyframename_ | Specifies the name of the keyframe you want to bind to the selector |
| none | Default value. Specifies that there will be no animation (can be used to override animations coming from the cascade) |
| initial | Sets this property to its default value. |
| inherit | Inherits this property from its parent element. |

Eg:

```css
div{
  animation-name: cabins;
}
```

### Animation Play State

The `animation-play-state` property specifies whether the animation is running or paused.

**Note:** Use this property in a JavaScript to pause an animation in the middle of a cycle.

#### Property Values

| Value | Description |
| ---- | ---- |
| paused | Specifies that the animation is paused |
| running | Default value. Specifies that the animation is running |
| initial | Sets this property to its default value. |
| inherit | Inherits this property from its parent element. |
Eg:

```css
div:hover {  
 animation-play-state: paused;
}
```

### Animation Timing Function

- The `animation-timing-function` specifies the speed curve of an animation.
- The speed curve defines the TIME an animation uses to change from one set of CSS styles to another.
- The speed curve is used to make the changes smoothly.

#### Property Values

| Value | Description |
| ---- | ---- |
| linear | The animation has the same speed from start to end |
| ease | Default value. The animation has a slow start, then fast, before it ends slowly |
| ease-in | The animation has a slow start |
| ease-out | The animation has a slow end |
| ease-in-out | The animation has both a slow start and a slow end |
| step-start | Equivalent to steps(1, start) |
| step-end | Equivalent to steps(1, end) |
| steps(int,start\|end) | Specifies a stepping function, with two parameters. The first parameter specifies the number of intervals in the function. It must be a positive integer (greater than 0). The second parameter, which is optional, is either the value "start" or "end", and specifies the point at which the change of values occur within the interval. If the second parameter is omitted, it is given the value "end" |
| cubic-bezier(_n_,_n_,_n_,_n_) | Define your own values in the cubic-bezier function  <br>Possible values are numeric values from 0 to 1 |
| initial | Sets this property to its default value. |
| inherit | Inherits this property from its parent element. |

Eg:

```css
#div1 {animation-timing-function: linear;}  
#div2 {animation-timing-function: ease;}  
#div3 {animation-timing-function: ease-in;}  
#div4 {animation-timing-function: ease-out;}  
#div5 {animation-timing-function: ease-in-out;}
```

---
