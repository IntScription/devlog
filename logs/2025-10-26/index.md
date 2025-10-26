---
layout: default
permalink: /logs/2025-10-26/
---

# Devlog - 2025-10-26

## 🚀 What I Did

-

## 🧠 What I Learned

- NaN - Not a number.

```javascript
let result = 0 / 0;
console.log(result); // Output: NaN
```

- isNaN - used to find if it is NaN or not.

```javascript
console.log(isNaN(NaN));       // true
console.log(isNaN(undefined)); // true
console.log(isNaN({}));        // true

console.log(isNaN(true));      // false
console.log(isNaN(null));      // false
console.log(isNaN(37));        // false

console.log(isNaN("37"));      // false: "37" is converted to 37
console.log(isNaN("37.37"));   // false: "37.37" is converted to 37.37
console.log(isNaN(""));        // false: empty string is converted to 0
console.log(isNaN(" "));       // false: string with a space is converted to 0

console.log(isNaN("blabla"));  // true: "blabla" is not a number
```

- `parseFloat()` and `parseInt()` are two essential methods in JavaScript for converting strings to numbers.
- `.toFixed()` method is a built-in JavaScript function that formats a number using fixed-point notation.

```javascript
console.log((3.14159).toFixed(3));  // Output: "3.142"
console.log((3.14449).toFixed(3));  // Output: "3.144"
console.log((3.14550).toFixed(3));  // Output: "3.146"
```

## 🔥 What's Next

- Functions.

---

[← Previous]({{site.baseurl}}/logs/2025-10-24/)
