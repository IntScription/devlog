---
layout: default
permalink: /logs/2026-02-05/
---

# Devlog - 2026-02-05

## 🚀 What I Did

- Theory.

## 🧠 What I Learned

### Higher Order Functions

- Higher order functions make code more flexible and reusable.

#### Map

- Map method creates new array by applying a given function to each original array.

```javascript
const numbers = [3, 4, 5, 6, 7].map((element, index) => {
  console.log("Element:", element);
  console.log("Index:", index);
  return element * 2;
});
```

- Removing a specific element from an array is not a correct way to use map.
- Current element, its index and the original array - arguments for map.

#### filter()

- Is used to create a new array with elements that pass a specified test.
- Returns an empty array if no elements in array pass the test.

```javascript
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const evenNumbers = numbers.filter((num) => num % 2 === 0);

console.log(evenNumbers); // [2, 4, 6, 8, 10]
```

#### reduce()

- `reduce` method allows to process an array and condense into a single value.

```javascript
const numbers = [1, 2, 3, 4, 5];
const sum = numbers.reduce(
  (accumulator, currentValue) => accumulator + currentValue,
  0
);

console.log(sum); // 15
```

#### Method chaining

- A technique where you call several methods one after another.

```javascript
const result = "  Hello, World!  "
  .trim()
  .toLowerCase()
  .replace("world", "JavaScript");

console.log(result); // "hello, JavaScript!"
```

#### sort()

- Used to arrange the elements of an array and returns a reference to the sorted array.

```javascript
const numbers = [414, 200, 5, 10, 3];
numbers.sort();

console.log(numbers); // [10, 200, 3, 414, 5]
```

#### every() and sum()

- `every` - tests whether all elements in an array pass a test implemented by a provided function.

```javascript
const numbers = [2, 4, 6, 8, 10];
const hasAllEvenNumbers = numbers.every((num) => num % 2 === 0);

console.log(hasAllEvenNumbers); // true
```

- `some`() - checks if at least one element passes the test.

```javascript
const numbers = [1, 3, 5, 7, 8, 9];
const hasSomeEvenNumbers = numbers.some((num) => num % 2 === 0);

console.log(hasSomeEvenNumbers); // true
```

## 🔥 What's Next

- Practice problems.
- Theory.
- Codewars.

---

[← Previous]({{site.baseurl}}/logs/2025-12-12/)
