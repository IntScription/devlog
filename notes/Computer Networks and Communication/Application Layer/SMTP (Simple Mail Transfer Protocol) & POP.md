---
tags:
  
- cnc
---
- FTP is synchronous but SMTP and POP are both synchronous and asynchronous
- SMTP port number is 25 for pushing the mail
- By default, POP3 protocol works on two ports : Port 110 
- this is the default  POP3 non-encrypted port
- Port 995 
- this is the port you need to use if you want to connect using POP3 securely
- MIME (Multipurpose Internet Mail Extensions)

![SMTP.png](SMTP.png)

- At first a mail Client comes in, they fetch information from user (their mails)
- This mail goes to MTA (Mail Transfer Agent)
- Now from MTA it goes to another mail server (another MTA) where the mail client collects the mail and then the user gets to view

---
