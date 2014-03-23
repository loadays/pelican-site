title: Babelfish for DevOps: syslog-ng 
status: hidden
category: proposals


#abstract

Most people still think of syslog-ng as a logging system with a flexible configuration language. It is now databases, message parsing, mongodb, JSON, message queuing and a lot more. Over the years, syslog-ng has evolved from a flexible and reliable logging system into a feature-rich log-processing tool. It's not just store and forward anymore, for example, with syslog-ng you can:
* Process and parse the body of messages to find important information and send e-mail alerts for specific events
* Receive structured JSON messages from your applications and store-them in a schema-free MongoDB NoSQL database
* Publish your messages to different message-queuing systems, for example, STOMP or AMQP
* Collect real-time statistics from your hosts and applications using the redis or riemann destinations ... or just send you an e-mail, when a torrent is downloaded :-)

All of these illustrated with short real life examples, how they can be used during development or operating your servers.

# bio
Peter Czanik is community manager at BalaBit, developers of syslog-ng. In his limited free time he is interested in non-x86 architectures, and works on one of his PPC or ARM machines.
