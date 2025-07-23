---
tags:
  - javascript
  - programming
---
All objects in JavaScript have a `prototype`. The `prototype` is another object that the original object _inherits_ from, which is to say, the original object has access to all of its `prototype`’s methods and properties.

- All objects have a prototype
- The prototype is another object

## Prototype Inheritance

1. We can define properties and functions common among all objects on the `prototype` to save memory. Defining every property and function takes up a lot of memory, especially if you have a lot of common properties and functions, and a lot of created objects! Defining them on a centralized, shared object which the objects have access to, thus saves memory.
2. The second reason is the name of this section, **Prototypal Inheritance**

Essentially, this is how JavaScript makes use of `prototype` - by having the objects contain a value - to point to `prototype`s and inheriting from those prototypes, and thus forming a chain. This kind of inheritance using prototypes is hence named as Prototypal inheritance. JavaScript figures out which properties exist (or do not exist) on the object and starts traversing the chain to find the property or function.

Note:

1. Every `prototype` object inherits from `Object.prototype` by default.
2. An object’s `Object.getPrototypeOf()` value can only be _one_ unique `prototype` object.

---
