---
tags:
  - cnc
---
## What is it ?

- It is a data-link layer protocol
- We use LAN tech
- Uses CSMA / CD
- Uses BUS and STAR topology

## Frame Format

![Ethernet.png](Ethernet.png)

### Preamble 

- 56 constant bits (101010....10)
- Contains 7 bytes of altering 0's and 1's and alerts the receiving system that the frame is coming and enable it to synchronize its clock if its out of synchronization

### SFD (Start Frame Delimiter)

- Also has constant bits
- It was alerting the receiver (preamble + SFD = 8 bytes)
- This field signals the beginning of the frame
- It warns the station that this is the last time for synchronization

### Destination Address

- It is the MAC (Media Access Control) address 
- It is 48-bits and contains the link layer address of the destination station to receive the packet

### Source Address

- Contains link layer address of the sender of a packet
- It is  6 bytes

### Type

- Defines upper-layer protocol whose packet is encapsulated in the frame
- This is used for multiplexing and demultiplexing

### Data and Padding

- 46 Bytes - 1500 Bytes
- If less than 46 then it is padded with extra 0's
- Has a field that defines the length of data

### CRC (Cyclic Redundancy Check)

- Contains error-detection information
-  If receiver calculates CRC and finds that it is not 0 (corruption in transmission), then it discards the frame

---

