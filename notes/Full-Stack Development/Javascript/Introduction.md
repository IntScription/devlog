---
tags:
  
- javascript
  
- programming
---
- It is a scripting language used to develop web pages
- It adds interactivity in the websites
- Is a [prototype-based](https://developer.mozilla.org/en-US/docs/Glossary/Prototype-based_programming), multi-paradigm, [single-threaded](https://developer.mozilla.org/en-US/docs/Glossary/Thread), [dynamic](https://developer.mozilla.org/en-US/docs/Glossary/Dynamic_typing) language, supporting object-oriented, imperative, and declarative (e.g. functional programming) styles

---
## NOTE:

- The `let` keyword tells JavaScript you are declaring a variable.
- JavaScript interacts with the HTML using the Document Object Model, or DOM. The DOM is a tree of objects that represents the HTML. You can access the HTML using the `document` object, which represents your entire HTML document.
- One method for finding specific elements in your HTML is using the `querySelector()` method. The `querySelector()` method takes a CSS selector as an argument and returns the first element that matches that selector. For example, to find the `<h1>` element in your HTML, you would write:

```js
let h1 = document.querySelector("h1");
```

- Scope is the term used to describe where a variable can be accessed. If a variable is declared inside a block of code, it is only accessible to the code inside that block. This is called block scope.

  ```js
let num = 1;
if (num === 1) {
  let num = 2; // this num is scoped to the if statement
  console.log(num); // expected output: 2
}
console.log(num); // expected output: 1 (the global variable)
```

- The `shift()` method on an array removes the first element in the array and returns it.

```js
const numbers = [1, 2, 3];
const firstNumber = numbers.shift(); // returns 1
```

- The `Math` object in JavaScript contains static properties and methods for mathematical constants and functions. One of those is `Math.random()`, which generates a random number from `0` (inclusive) to `1` (exclusive). Another is `Math.floor()`, which rounds a given number down to the nearest integer. Using these, you can generate a random number within a range. For example, this generates a random number between `1` and `5`: `Math.floor(Math.random() * 5) + 1;`.

- The `innerHTML` property allows you to access or modify the content inside an HTML element using JavaScript.

Here is an example of updating the content for this paragraph element using the `innerHTML` property.

```html
<p id="demo">This is a paragraph.</p>
```

```js
document.querySelector("#demo").innerHTML ="Hello, innerHTML!"; 
```

- Functions run specific blocks of code when they are called, but they can also return a value. This value can be assigned to a variable and used elsewhere in your code.
- The `ternary operator` is a conditional operator and can be used as a one-line `if-else` statement. The syntax is: `condition ? expressionIfTrue : expressionIfFalse`.

Here is an example of returning a value using an `if-else` statement and a refactored example using a ternary operator:

```js
// if-else statement
if (score > 0) {
  return score
} else {
  return default_score
}

// ternary operator
score > 0 ? score : default_score
```

- The `g` flag, which stands for "global", will tell the pattern to continue looking after it has found a match. Here is an example:

```js
const helloRegex = /hello/g;
```

- JavaScript has a feature called template literals, which allow you to interpolate variables directly within a string. Template literals are denoted with backticks ` `` `, as opposed to single or double quotes. Variables can be passed in to a template literal by surrounding the variable with `${}` – the value of the variable will be inserted into the string.

For example:

```js
const name = "Naomi";
const templateLiteral = `Hello, my name is ${name}~!`;
console.log(templateLiteral);
```

The console will show the string "Hello, my name is Naomi~!".
- `${example}` 
- behaves like a placeholder
- A `for...of` loop is used to iterate over elements in an iterable object like an array. The variable declared in the loop represents the current element being iterated over.

```js
for (const element of elementArray) {
  console.log(element);
}
```

- The `Number` constructor is a function that converts a value to a number. If the value cannot be converted, it returns `NaN` which stands for "Not a Number".

Here is an example:

```js
Number('10'); // returns the number 10
Number('abc'); // returns NaN
```

---
>[!IMP]
>Templates and literals

