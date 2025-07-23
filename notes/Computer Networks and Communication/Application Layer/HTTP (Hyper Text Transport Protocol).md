---
tags:
  - cnc
---
- Port number 80
- Responsible for the communication between web server and clients
- It is stateless (every request is independent)
- It is inband 

## What is HTTPS ?

- It is called Hyper Text Transport Protocol Secure
- It is basically where all the data sent back and forth is encrypted by SSL (Secure Sockets Layer) or TLS (Transport Security Layer)

## HTTP Methods

### GET

- Use to get data from server (retrieving the information)
- Eg: loading standard html page, loading assets like css or images, json data, xml data, etc.

### POST

- Used to posting data or adding a resource to server
- Like a contact form, or a blog post, etc.

### PUT

- Used to update data on a server
- Edit blog post or image

### DELETE

- Deletes the data from server

---
![[HTTP Methods.png]]

---
## HTTP Header Fields

![[HTTP header.png]]

### General 

- Request URL
- Request Method
- Status Code
- Remote Address
- Referrer Policy

### Response

- Server
- Set-Cookie
- Content-Type
- Content-Length
- Date

### Request

- Cookies
- Accept-xxx
- Content-Type
- Content-Length
- Authorization
- User-Agent
- Referrer

---
## Status Codes

### 1xx : Informational

- Request received / processing

### 2xx : Success

- Successfully received, understood and accepted

### 3xx : Redirect

- Further action must be taken / redirect

### 4xx : Client Error

- Request does not have what it needs
### 5xx : Server Error

- Server failed to fulfil an apparent valid request


![[Status Codes.png]]

---
## Requests and Response

![[Request and Response.png]]

- Communication between clients and servers is done through **Request and Response**

1. A client (a browser) sends an **HTTP request** to the web
2. A web server receives the request
3. The server runs an application to process the request
4. The server returns an **HTTP response** (output) to the browser
5. The client (the browser) receives the response

---
