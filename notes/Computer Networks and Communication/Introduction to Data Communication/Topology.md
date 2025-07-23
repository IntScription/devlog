---
tags:
  - cnc
---
## What is Topology ?

- Talks about device arrangement

### 1. Mesh Topology

- All devices are interconnected (each node is connected to every other node)
- For eg: 4 devices are interconnected then the number of cables are 6
  ![[Mesh Topology.png]]
  $$Cables = n*(n-1) / 2$$
  $$Ports = n*(n - 1)$$
  - Highest reliability compared to other topology
  - Cost increases when multiple devices are connected due to the increase in number of cables
  - Provides security (eg: we may not know how 'A' communicates with 'D')
  - Maintenance is high
  - Supports point-to-point communication (also known as dedicated communication, like 'LAN')

## 2. Hub Topology

- Also called 'Star Topology'
- Hub is a multiport device (multiple devices are connected through hub)
- Number of cables = Number of Ports = n
- No reliability (if there is a problem in hub then there is no communication)
- Cost is normal or genuine (compared to mesh it is low)
- Security is low (since it broadcasts the message)
 
![[Hub Topology.png]]

- Also a point-to-point communication (direct communication)

## 3. Bus Topology

![[Bus Topology.png]]

- Number of Cables = n + 1
- The horizontal line is called as 'Backbone Cable'
- Number of Ports = n
- No reliability (since there is a single point of failure)
- No security (since the cable cannot decide / filter the information, only a switch  or router can)
- Cost - cheap
- Terminator or Repeater in the ends of the cable(it increase the signal strength so it can cover more distances)
- This is a multi-point (here collision rate is also high = 'n')

## 4. Ring Topology

- In simple words its the end-to-end connection of the bus topology
 ![[Ring Topology.png]]
- Number of Cables = n + 1
- Number of Ports = n
- Less reliable (single point of failure)
- No security
- Cost - cheap
- It is uni-directional (we use token ring to reduce collision)

#### NOTE :- 'n' means Node
---

