

I would use the open source Prometheus  (event monitoring and alerting) and Grafana  (metric analytics &amp; visualization suite) to monitor the server.

 The challenges of monitoring  this server  is to be able to predict anomaly detection on metrics collected, without human interaction. For example a server that gets suspiciously busy or idle, being able to find metrics that are behaving unusually at the moment of a problem is a valuable way to narrow the search of an issue. Of course hardware monitoring is set and is there for common hardware issues, e.g the system has a failed disk, and calls home, or generate alerts that humans should interact and take care, but is the other kind  that is challenging

 Another challenge is to avoid false alerts, based on day of the week, backup times, or expected load on specific time of day/period.

Encrypting and decrypting network traffic is a very CPU-intensive task. The  initial session setup demands the most.There will be a big significant performance hit when  2048-bit keys are used ,as the CPU usage typically increases 4-7 times  compared with 1024-bit keys

Logging can be done based on size available depending on the volume of log you want to keep but  threat detection might be a challenge. With the network bandwidth available with 25000 Connection/sec the average size of each can be around 50KBytes , in order not to saturate the 10Gbit Controller&#39;s available bandwidth, of course many will be smaller than that, but others will be bigger depending on object size.

  I understand that one  10Gbit connection  is used for communicating with the internal network ( unencrypted traffic) and the other one will be connected to the clients.

Metrics to be gathered:

- Session Rate:  It directly determines when the load balancer will not be able to distribute all the requests it receives. It is mostly dependant in CPU. Session rates around 100.000 session/s can be achieved on Xeon E5 systems in 2014
- Session Concurrency: This factor is tied to the previous one. The session rate will drop when the number of concurrent sessions increases. If a load balancer receives 10000 session per second and the servers respond in 100ms, then the load balancer will have 1000 concurrent sessions.Some sessions might stay open for longer and waste cpu and memory
- Data forwarding rate:  Measured in Gb/s. Highest data rates are achieved with large objects.However this increases the memory used  as the server has  to copy the data from the input interface to memory and then to the output device.

- Number of failed requests.  If there are a lot of failed requests , there might be an issue that needs to be handled.
- Requests per second, Connections Per second, Sessions Per Second
- CPU Busy time: Indicates if the systems lacks cpu resources at the moment
- Number of tcp\_established connections  ( sum of inbound + outbound): It shows that data can be moved around
- RAM used: It always makes sense to monitor  how much memory is used, and by what process.
- Packets  and Bytes send and received: Shows that communication exists inbound and outbound
- File-descriptors used , file descriptors available: Indication of how many connections can be made
- Server&#39;s, hardware condition, disks, memory, ecc errors, network interface errors, power supply errors.

LOGGING:

 Source IP and port of requestor make it possible to  find their origin in firewall logs;

 Session setup will match generally the firewall logs, and teardown date often matches proxies date

 Proper request encoding will ensure the requestor cannot hide non-printable characters , nor fool  a terminal

 Arbitrary request and response header and cookie capture help to detect scan attacks, proxies, and infected hosts.

 Timers will help to differentiate hand-typed requests from normal browser operation
