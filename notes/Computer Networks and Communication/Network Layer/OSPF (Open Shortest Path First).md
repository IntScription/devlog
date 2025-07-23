---
tags:
  - cnc
---
- It is an intra-domain protocol (exchanging information between dynamic routers within the autonomous system)
- Uses link-state routing algorithm
- Here each router has information about its neighbouring routers and uses this information to determine the shortest path

## Working

- Establish relationship between OSPF neighbours that are running on the same link
- Exchange the database information between the routers; i.e. LSDB with each other
- Selects the best route to add to the routing table

## Links in OSPF

1. Point-to-point : Connects two routers with any host in between
2. Transient Link : Network with several routers attached to it 
3. Stub Link : Network that is connected to one router, data packets enter the network through single router and leave through the same route
4. Virtual Link  : When the link between two routers is broken, the administration may create a virtual link between them

## Message Format

- Version
- Type
- Message length
- Source router IP address
- Area identification
- Checksum
- Authentication type

## Message Type

- Hello
- Database Description
- Link state Request update
- Link state Acknowledgement

---

