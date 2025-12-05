---
layout: default
permalink: /logs/2025-12-03/
---

# Devlog - 2025-12-03

## 🚀 What I Did

- Title case conversion using for loops and maps.
- Inventory Management.
- Codewars.

## 🧠 What I Learned

- Boolean - converter function.
- boolean - data type.

```javascript
typeof true   // "boolean"
typeof false  // "boolean"

Boolean(10)      // true
Boolean(0)       // false
Boolean("hi")    // true
Boolean("")      // false
Boolean(null)    // false
Boolean(true)    // true
```

### Class

| Use Case            | Better Choice |
| ------------------- | ------------- |
| Object blueprints   | ✅ `class`     |
| Utilities / helpers | ✅ `function`  |
| Modern projects     | ✅ `class`     |
| Legacy code         | ✅ `function`  |

- class is just a blueprint for creating objects.

```javascript
class Car {
  constructor(name, speed) {
    this.name = name;
    this.speed = speed;
  }
}

const car1 = new Car("BMW", 120);
const car2 = new Car("Audi", 150);
```

- constructor runs automatically when you create a new object.
- properties - variables that belong to the object.
- methods - function inside a class.
- this - means this current object.

| Use Case               | Use Class? |
| ---------------------- | ---------- |
| Many similar objects   | ✅          |
| Game characters        | ✅          |
| API models             | ✅          |
| Data structures        | ✅          |
| One small object       | ❌          |
| Simple helper function | ❌          |

- `module` - provides a powerful way to organize and structure js.

```javascript

import anyName from './module.js';
```

## 🔥 What's Next

- mini projects.
- theory.

---

[← Previous]({{site.baseurl}}/logs/2025-12-02/)
