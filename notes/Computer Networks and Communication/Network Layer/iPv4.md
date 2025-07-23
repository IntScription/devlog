---
tags:
  - cnc
---
## What is it ?

- It is a connectionless protocol (when packets travel there is no connection)
- It is a datagram service (can connect to destination through different ways) - technically packets follow any route
- Header talks about how the packet moves and its characteristics ( more like destination address)

### Header Diagram
 
![[iPv4.png]]
#### Explanation :

1. VER(Version): 
     - 4 bit (0100)      
2. HLEN(Header Length):
     - 4 bit
     - Talks about the length of the head and its significance
     - Header size from 20-60 bytes
3. Type of Service (DSCP) :
     - 8 bit, first 3 defines the precedence, DTRC(Delay, Throughput, Reliability, Cost) defines the next 4 bits, last bit is reserved for future purpose
     - For less Delay make it 1
     - Rate of transfer (Throughput) should be more than 1 otherwise 0
     - Reliability(Packets should be transferred properly), high ->1, otherwise 0
     - Cost - using the shortest path so 1, otherwise 0
     - Differentiated Services Code Point - 6 bits reserved, rest 2 bits for ECN (Explicit Congestion Notification)
 4. Datagram Length (Total Length): 16 bit (header + payload)
 5. Fragmentation:
     - Identification - identifies datagram originating from source
     - Flags - 3 bit, defines 3 flags
     - Fragmentation offset - 13 bit, defines the relative position of fragment w.r.t datagram
     - Dividing the entire network into small fragments
 6. TTL (Time To Live):  
     - 8 bit 
     - We use this when data is in a loop
 7. Protocol : 8 bit, usage of different protocols will be mentioned
 8. Header Checksum : 16 bit, checksum is used for error detection
 9. Source IP Address : 32 bit
 10. Destination IP Address : 32 bit
 11. Options + Padding : 
     - To add extra data only when its not in 32 bit multiplication
     - 40 bytes

### Class Ranges

![[Class Range.png]]

- Class A (0-127 bytes)
- Class B (128-191 bytes)
- Class C (192-223 bytes)
- Class D (224-239 bytes)
- Class E (240-255 bytes)
---

