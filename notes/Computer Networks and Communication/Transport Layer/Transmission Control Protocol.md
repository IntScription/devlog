---
tags:
  - cnc
---
- TCP is a connection-oriented transfer layer protocol and a most commonly used protocol
- Uses a combination of the Go-Back-N (GBN) and Selective-Repeat (SR) protocols to provide reliability
- It is slow compared to UDP
- TCP packet is called Segment

## Features 

### Stream Data Transfer

- Sends data in streams and allows it to receive in streams as well
- Sending and Receiving buffer

### Process-to-Process Communication

- From one process to another using port numbers
### Reliability

- Uses GBN and SR

### Flow Control

- Flow Control using a window mechanism

### Error Control

- Delivers entire stream to the application without any error

### Multiplexing and Demultiplexing

- Multiplexing at sender
- Demultiplexing at receiver

### Connection-Oriented Services

1. Establish logical connections
2. Data exchange in both direction
3. Connection is terminated

### Full Duplex Communication

- Offers communication from both directions at same time

### Congestion Control

- Congestion window
- Congestion detection
- Congestion policies

---
