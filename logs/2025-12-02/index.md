---
layout: default
permalink: /logs/2025-12-02/
---

# Devlog - 2025-12-02

## 🚀 What I Did

- Gradebook.
- Codewars

## 🧠 What I Learned

### Var

```javascript
var x = 10;

if (true) {
  var x = 20;
  console.log(x);
}

console.log(x); // outputs 20 20
```

- It allows you to redeclare the same variable multiple times without throwing an error.
- Not used in modern browsers anymore.
- Hoising - allows declaration to be on top scope regardless if it is passed on later.

```javascript
// example to Hoising
console.log(x);
var x = 3;
console.log(x) // outputs 3
```

- `localeCompare()` - compares two strings alphabetically.

## 🔥 What's Next

- Some theory and coding.

---

[← Previous]({{site.baseurl}}/logs/2025-11-28/)
