---
layout: default
permalink: /logs/2025-12-12/
---

# Devlog - 2025-12-12

## 🚀 What I Did

- Codewars.
- Random Password generator(using random function, maps, and crypto)

## 🧠 What I Learned

- `Uint32Array` = array of big random numbers (0 to 4.29 billion).
- `Uint8Array` gives only 0–255 (less randomness).
- `Uint16Array` gives 0–65,535.

### Cryptographically random values

- Comes from OS-level secure random generator(Linux /dev/urandom, Windows Cryptographic Provider, macOS SecureRandom)
- non-predictable.
- high entropy.
- designed specifically for passwords, keys, salts, tokens.
- It follows NIST SP 800-90 standards used in cryptography.

```javascript
crypto.getRandomValues(arr);
```

## 🔥 What's Next

- FCC.
- Codewars.
- Theory(Dom).

---

[← Previous]({{site.baseurl}}/logs/2025-12-07/) | [Next →]({{site.baseurl}}/logs/2026-02-05/)
