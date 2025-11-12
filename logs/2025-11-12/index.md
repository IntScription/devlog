---
layout: default
permalink: /logs/2025-11-12/
---

# Devlog - 2025-11-12

## 🚀 What I Did

- Some lab work on boolean and numbers.

## 🧠 What I Learned

### Objects in JS

```javascript
const exampleObject = {
  propertyName: value;
}
```

- To access most common is dot notation `objectName.propertyName`.

```javascript
// bracket notation
const person = {
  name: "Alice",
  age: 30,
  city: "New York"
};

console.log(person["name"]); // Alice
console.log(person["age"]); //  30
```

- Functions and object methods are both ways to encapsulate reusable code.
- `Object()` - when you want to create an object wrapper for a primitive value.
- Recipe Tracker.

### JSON

- `JSON` - javascript object notation.
- Is a lightweight data format used for data exchange between servers and web applications.

```javascript
{
  "name": "Alice",
  "age": 30,
  "isStudent": false,
  "list of courses": ["Mathematics", "Physics", "Computer Science"]
}
```

- `JSON.stringify()` is used to convert a JavaScript object into a JSON string.

```javascript
const developerObj = {
  firstName: "Jessica",
  isAwesome: true,
  isMusician: true,
  country: "USA",
};

// result: {"firstName":"Jessica","country":"USA"}
console.log(JSON.stringify(developerObj, ["firstName", "country"]));
```

- Also accepts an optional parameter called a `replacer`, which can be a function or an array.
- `JSON.parse()` converts a JSON string back into a JavaScript object.

```javascript
const jsonString = '{"name":"John","age":30,"isAdmin":true}';
const userObject = JSON.parse(jsonString);
console.log(userObject);

// Result:
// { name: 'John', age: 30, isAdmin: true }
```

- Optional chaining operator - `?.` is a useful tool in JavaScript that lets you safely access object properties or call methods without worrying whether they exist.

## 🔥 What's Next

- Objects.

---

[← Previous]({{site.baseurl}}/logs/2025-11-10/)
