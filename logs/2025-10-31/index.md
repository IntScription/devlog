---
layout: default
permalink: /logs/2025-10-31/
---

# Devlog - 2025-10-31

## 🚀 What I Did

- Leap year calculator.
- String Truncating algorithm.
- Sting Ending confirm.

## 🧠 What I Learned

### String Truncating

- str.length first.
- if it is > num then you should return str.slice(pos, num) + '...'
- if str.length is not > num then just return the str.

```javascript
const strTrun = (str, num) => {
  return str.length > num ? str.slice(0, num) + "..." : str
}
console.log(strTrunc("Hello World", 8));
```

## 🔥 What's Next

- Arrays.

---

[← Previous]({{site.baseurl}}/logs/2025-10-30/) | [Next →]({{site.baseurl}}/logs/2025-11-03/)
