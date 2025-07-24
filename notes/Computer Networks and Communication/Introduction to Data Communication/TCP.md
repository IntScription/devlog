---
tags:
  - cnc
---
- Known as Transmission Control Protocol or Internet Protocol
- Developed by ARPANET
- Support client-server and peer-to-peer

![TCP.png](TCP.png)

## 1. Physical Layer

- Responsible for carrying individual bits in a frame across the link
- Communication between two devices at physical later is logical because there is another hidden layer

## 2. Data-link Layer

- It is responsible for taking the datagram and moving across the link

## 3. Network Layer

- Responsible for creating a connection between the source computer and the destination computer
- It is a host-to-host communication

## 4. Transport Layer

- It is end-to-end
- Source host gets the message from the application layer; encapsulates it in a transport-layer packer (called a segment or a user datagram); and sends it through the logical (imaginary) connection, to the transport layer at the destination host

## 5. Application Layer

- Logical connection between the two application layers is end-to-end
- The two applications exchange messages as though they have a bridge between them

---

