---
tags:
  - cnc
---
## There are of two types:

1. Intra-domain protocol : 
     - communication happens within the autonomous system
     - RIP, OSPF
2. Inter-domain protocol :
     - communication between two or more autonomous system
     - BGP


## Unicast Routing Protocols

1. RIP (Routing Information Protocol) - uses distance vector algorithm (Bellman-Ford)
2. [OSPF (Open Shortest Path First)](OSPF-(Open-Shortest-Path-First)) - uses link state algorithm (Dijkstra's Algorithm)
3. BGP (Border Gateway Protocol) - uses path vector algorithm 

### OSPF

- We use Dijkstra's algorithm to find out the cost
- Maintains a database called as Link State Database (LSDB)
- Large networks are divided into small areas to avoid traffic (main area is Backbone area - has WAN connection, and is 0)

### BGP

- Embedded in the borders of the autonomous systems
     1. iBGP - internal
     2. eBGP - external
- Determines the best path in a network
- Path attributes - determines the cost or the next network through the next host and forwarding table (its the associated cost) - path at which data has to be transmitted 

#### Messages :-

- Hello message (Type 1)
- Database description (Type 2)
- Link-state request (Type 3)
- Link-state update (Type 4)
- Link-state (Type 5)

---

>[! imp for third unit]
>  - HTTP request and response
>  - DNS and FTP

---

