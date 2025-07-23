---
tags:
  - cnc
---
## Process-to-Process Communication

- Sending the message from one process to another process
- Also called end-to-end or port-to-port communication
- It uses a port number (16-bit address) to deliver the segmented data to the correct process
 ![[Process-to-process.png]]

## Reliability

- Does in-order delivery (loss of data)
- Sequence control
- Loss control
- Duplication control

## Encapsulation and Decapsulation

- Encapsulation happens at sender site
- Decapsulation happens at receiver site

## Multiplexing and Demultiplexing

- Transport layer at source performs multiplexing
- Transport layer at destination performs demultiplexing
 ![[Multiplexing and Demultiplexing.png]]

## Error Control

- Uses checksum to detect errors
- This is end-to-end

## Congestion Control

- Uses open-loop to prevent congestion and close-loop to remove congestion from network once it has occurred

## Flow Control

- Provides flow control mechanism between adjacent layers of TCP/IP
- Uses method of sliding window protocol
- Related to first issue, we must prevent losing the data items at consumer site
- Makes sure that data transmitted at any rate is acceptable by both sender and receiver by managing data flow

---

