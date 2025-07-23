---
tags:
  - cnc
---
- It is a phonebook of the internet
- Humans access information online through domain names
- DNS translates domain names to IP addresses so browsers can load internet resources

## How does DNS work ?

- It involves converting a hostname (www.example.com) into a computer-friendly IP address (such as 198.168.1.1)

## Types of Domains

![[_attach/CNC/Domain Name System/DNS.png]]

### 1. Generic Domain 

- .com(commercial), .edu(educational), .mil(military), .org(nonprofit organization), .net(similar to commercial)

### 2. Country Domain

- .in (India) .us .uk

### 3. Inverse Domain

- It is used for mapping an address to a name
- Sends query to DNS server
---

![[DNS 1.png]]

## DNS Server

### DNS Resolver

- DNS cache (sometimes called DNS resolver cache) - It is a temporary database maintained by computer operating system that contains records of all recent visits and attempted visits to websites and other internet domains
- It receives the request to resolve the domain name with the IP address
### Root Name Server

- 13 sets of servers named as `letter.root-servers.net` 
- Details of all root name servers can be found at `www.root-servers.org`
- It receives the first request and lets the DNS resolver know the address of the Top Level Domain (TLD) that stores information about the site
- `.com and .net` are like TLDs`

### TLD name server

- The DNS resolver then queries this server, returning the Authoritative Name Server where the site is returned

### Authoritative Name Server (ANS)

- Finally, the DNS resolver queries this server to learn the actual IP address of the website you're trying to deliver

---
