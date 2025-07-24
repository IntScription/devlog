---
tags:
  
- programming
  
- html-css
---
## 1. External 

- File that HTML files link to
- Contains separate CSS files that contain only style properties with the help of tag attributes

### Example :

```html
<!DOCTYPE html>
<html>

<head>
	<title>Internal CSS</title>
	<link rel="stylesheet" href="style.css">
</head>

<body>
	<div class="main">
		<div class="GFG">GeeksForGeeks</div>

		<div class="geeks">
			A computer science portal for geeks
		</div>
	</div>
</body>

</html>

```

```CSS
body {
	background-color: powderblue;
}

.main {
	text-align: center;
}

.GFG {
	color: #009900;
	font-size: 50px;
	font-weight: bold;
}

#geeks {
	font-style: bold;
	font-size: 20px;
}

```

## 2. Inline

- Method of styling where CSS properties are directly applied to HTML elements within the body section by using the “style” attribute

### Example :

```html
<!DOCTYPE html>
<html>

<head>
	<title>Inline CSS</title>
	<style>
		p {
			color:#009900;
			font-size:50px;
			font-style:italic;
			text-align:center;
			}
	</style>

</head>

<body>
	<p>
		GeeksForGeeks
	</p>
</body>

</html>

```

## 3. Internal or Embedded

- Used when single html document must be styled uniquely

### Example :

```html
<!DOCTYPE html>
<html>

<head>
	<title>Internal CSS</title>
	<style>
		.main {
			text-align: center;
		}

		.GFG {
			color: #009900;
			font-size: 50px;
			font-weight: bold;
		}

		.geeks {
			font-style: bold;
			font-size: 20px;
		}
	</style>
</head>

<body>
	<div class="main">
		<div class="GFG">GeeksForGeeks</div>

		<div class="geeks">
			A computer science portal for geeks
		</div>
	</div>
</body>

</html>

```

---
