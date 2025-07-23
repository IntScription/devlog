---
tags:
  - cnc
---
- It is unreliable and connectionless transport-layer protocol that creates a process-to-process communication, which means it requires little overhead and offers fast delivery
- The UDP packet is called a User Datagram
- Has no flow and error control mechanism (only attempt to error control is checksum)
- Uses multiplexing and demultiplexing to handle outgoing and incoming user datagrams
- A UDP package can involve five components: a control-block table, a control-block module, input queues, an input module, and an output module
- It is fast compared to TCP

## Services of UDP

### 1. Process-to-Process Communication

- Provides using socket addresses (IP addresses + port number)

### 2. Connectionless Service

- Each user datagram is an independent datagram

### 3. Flow Control

- No flow control (no window mechanism)

### 4. Error Control

- No error control except checksum

### 5. Congestion Control

- Since its connectionless protocol, it does not provide congestion control

### 6. Encapsulation and Decapsulation

- To send messages from one user to another user it encapsulates and decapsulates messages

### 7. Queuing

- Here queues are associated with ports

### 8. Multiplexing and Demultiplexing

- Used to handle several processes obtaining this service

---
