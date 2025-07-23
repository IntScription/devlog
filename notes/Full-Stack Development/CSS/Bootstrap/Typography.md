---
tags:
  - html-css
  - programming
---
## Bootstrap's Default Settings

Bootstrap's global default font-size is 14px, with a line-height of 1.428.

This is applied to the `<body>` element and all paragraphs (`<p>`).

In addition, all `<p>` elements have a bottom margin that equals half their computed line-height (10px by default).

## `<small>`

In Bootstrap the HTML `<small>` element is used to create a lighter, secondary text in any heading:

# h1 heading secondary text

## h2 heading secondary text

### h3 heading secondary text

#### h4 heading secondary text

##### h5 heading secondary text

###### h6 heading secondary text

## `<mark>`

Bootstrap will style the HTML `<mark>` element in the following way:

Eg: Use the mark element to ==highlight== text.

## `<pre>`

Bootstrap will style the HTML `<pre>` element in the following way:

```text
Text in a pre element
is displayed in a fixed-width
font, and it preserves
both      spaces and
line breaks.
```

## Contextual Colours and Backgrounds

Bootstrap also has some contextual classes that can be used to provide "meaning through colours".

The classes for text colours are:`.text-muted`, `.text-primary`, `.text-success`, `.text-info`, `.text-warning`, and `.text-danger`

- The classes for background colours are:`.bg-primary`, `.bg-success`, `.bg-info`, `.bg-warning`, and `.bg-danger`


## More Typography Classes

The Bootstrap classes below can be added to style HTML elements further:

| Class              | Description                                                                                                                                                                                                                                                     |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `.lead`            | Makes a paragraph stand out                                                                                                                                                                                                                                     |
| `.small`           | Indicates smaller text (set to 85% of the size of the parent)                                                                                                                                                                                                   |
| `.text-left`       | Indicates left-aligned text                                                                                                                                                                                                                                     |
| `.text-center`     | Indicates center-aligned text                                                                                                                                                                                                                                   |
| `.text-right`      | Indicates right-aligned text                                                                                                                                                                                                                                    |
| `.text-justify`    | Indicates justified text                                                                                                                                                                                                                                        |
| `.text-nowrap`     | Indicates no wrap text                                                                                                                                                                                                                                          |
| `.text-lowercase`  | Indicates lowercased text                                                                                                                                                                                                                                       |
| `.text-uppercase`  | Indicates uppercased text                                                                                                                                                                                                                                       |
| `.text-capitalize` | Indicates capitalized text                                                                                                                                                                                                                                      |
| `.initialism`      | Displays the text inside an `<abbr>` element in a slightly smaller font size                                                                                                                                                                                    |
| `.list-unstyled`   | Removes the default list-style and left margin on list items (works on both `<ul>` and `<ol>`). This class only applies to immediate children list items (to remove the default list-style from any nested lists, apply this class to any nested lists as well) |
| `.list-inline`     | Places all list items on a single line                                                                                                                                                                                                                          |
| `.dl-horizontal`   | Lines up the terms (`<dt>`) and descriptions (`<dd>`) in `<dl>` elements side-by-side. Starts off like default `<dl>`s, but when the browser window expands, it will line up side-by-side                                                                       |
| `.pre-scrollable`  | Makes a `<pre>` element scrollable                                                                                                                                                                                                                              |

---
