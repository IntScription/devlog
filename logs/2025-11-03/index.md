---
layout: default
permalink: /logs/2025-11-03/
---

# Devlog - 2025-11-03

## 🚀 What I Did

-

## 🧠 What I Learned

### Array

- Ordered collection of values, each identified by a numeric value.

```javascript
let fruits = ["apple", "banana", "orange"];
console.log(fruits[0]); // "apple"
console.log(fruits[2]); // "orange"
```

#### Methods for adding and removal

- `push()`
- `pop()`
- `shift()`
- `unshift()`

```javascript
// push
const fruits = ["apple", "banana"];
const newLength = fruits.push("orange");
console.log(newLength); // 3
console.log(fruits); // ["apple", "banana", "orange"]

// pop
let fruits = ["apple", "banana", "orange"];
let lastFruit = fruits.pop();
console.log(fruits); // ["apple", "banana"]
console.log(lastFruit); // "orange"

// shift
let colors = ["red", "green", "blue"];
let firstColor = colors.shift();
console.log(colors); // ["green", "blue"]
console.log(firstColor); // "red"

// unshift
let numbers = [2, 3];
let newLength = numbers.unshift(1);
console.log(numbers); // [1, 2, 3]
console.log(newLength); // 3
```

- Each item in a one-dimensional array is accessed using a single index.
- To access an element in a two-dimensional array, you need two indices: one for the row and one for the column.

```javascript
let chessboard = [
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["r", "n", "b", "q", "k", "b", "n", "r"]
];

console.log(chessboard[0][3]); // Outputs: "Q"
```

- Array de-structuring :

```javascript
let fruits = ["apple", "banana", "orange"];

let [first, second, third] = fruits;

console.log(first);  // "apple"
console.log(second); // "banana"
console.log(third);  // "orange"

let fruits = ["apple", "banana", "orange", "mango", "kiwi"];
let [first, second, ...rest] = fruits;

console.log(first);  // "apple"
console.log(second); // "banana"
console.log(rest);   // ["orange", "mango", "kiwi"]
```

## 🔥 What's Next

- project.

---

[← Previous]({{site.baseurl}}/logs/2025-10-31/)
