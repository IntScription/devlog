---
tags:
  
- programming
  
- html-css
---
- Much more tolerant and an handle markup from all the prior versions
- HTML (Hyper Text Markup Language)
- Defines the meaning and structure of web content

## What is HTML5 ?

- Incorporates all the features from earlier versions
- Adds a diverse set of new tools for the web developer

### Goals of HTML5

- Support all existing web pages; no requirement to go back and revise older websites
- Reduce the need for external plugins and scripts to show website content
- Improve the semantic definition (i.e. meaning and purpose) of page elements
- Make the rendering of web content universal and independent of the device being used
- Handle web documents errors in a better and more consistent fashion

---
## **Note**

- Navigation is a core part of accessibility, and screen readers rely on you to provide the structure of your page. This is accomplished with semantic HTML elements.
- To increase the page accessibility, the `role` attribute can be used to indicate the purpose behind an element on the page to assistive technologies. The `role` attribute is a part of the _Web Accessibility Initiative_ (WAI), and accepts preset values.
- Every `region` role requires a label, which helps screen reader users understand the purpose of the region. One method for adding a label is to add a heading element inside the region and then reference it with the `aria-labelledby` attribute.
- It is important to link each `input` to the corresponding `label` element. This provides assistive technology users with a visual reference to the input. This is done by giving the `label` a `for` attribute, which contains the `id` of the `input`.
- Although not required for `label` elements with a nested `input`, it is still best-practice to explicitly link a `label` with its corresponding `input` element.
- The `footer` element is a container for a collection of content that is related to the page, and the `address` element is a container for contact information for the author of the page.
- The `address` element does not have to contain a physical geographical location. It can be used to provide a link to the subject.

---

>[!Knowledge]
>[HTML elements reference ](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)
>[Wrap with abbreviations](https://docs.emmet.io/actions/wrap-with-abbreviation/)
>[Remove Tag](https://docs.emmet.io/actions/remove-tag/)
>

---
