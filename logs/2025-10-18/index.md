---
layout: default
permalink: /logs/2025-10-18/
---

# Devlog - 2025-10-18

## 🚀 What I Did

- Timetable using HTML.

## 🧠 What I Learned

### JavaScript

```JavaScript
let greeting = "hello";
console.log(greeting[greeting.length - 1]); // Output: "o"

let firstTwo = greeting[0] + greeting[1]; // Output: "he"
console.log(firstTwo);
```

- Bracket notation - Access specific characters in the string using their index.

```JavaScript
let statement = "She said, \"Hello!\"";
console.log(statement); // Output: She said, "Hello!"
```

- We can use `\\` and place our quotes in it.

### Template Literal

```JavaScript
const name = "Alice";
const age = 25;
const message = `My name is ${name} and I am ${age} years old.`;
console.log(message);
```

- String Interpolation - Inserting variables and expressions directly into a string.
- Template literals preserve line breaks without needing escape characters.

```JavaScript
let sentence = "JavaScript is awesome!";
let position = sentence.indexOf("awesome!");
console.log(position); // 14
```

- `indexOf()` - used to find the index.

```JavaScript
let sentence = "JavaScript is awesome!";
let position = sentence.indexOf("fantastic");
console.log(position); // -1
```

### Prompt

```JavaScript
let age = prompt("How old are you?");
if (age !== null) {
  console.log("You are " + age + " years old.");
} else {
  console.log("User canceled the prompt.");
}
```

- Displays a pop-up asking for user input and returns the input as a string.
- If you cancel prompt it returns null.
- Second argument is setting a default value in the input field.

## 🔥 What's Next

- Advance strings.

---

[← Previous]({{site.baseurl}}/logs/2025-10-12/)
