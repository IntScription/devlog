---
layout: default
permalink: /logs/2025-11-21/
---

# Devlog - 2025-11-21

## 🚀 What I Did

- Problems on codewars.

## 🧠 What I Learned

### Reduce()

```javascript
array.reduce((accumulator, currentValue) => {
    // logic
}, initialValue)
```

- `accumulator` - Holds the running total or result.
- `currentValue` - The current item in the array during the loop.
- `initialValue` - What the accumulator starts with.

```javascript
const arr = [1, 2, 3];

const sum = arr.reduce((acc, curr) => {
  return acc + curr;
}, 0);

console.log(sum); // 6
```

- Works for numbers, strings, objects, arrays — anything.
- Replaces many loops.
- Very flexible.

## 🔥 What's Next

- Lab projects on FCC.

---

[← Previous]({{site.baseurl}}/logs/2025-11-18/)
