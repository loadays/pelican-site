title: syslog-ng from log collecting to log processing and information extraction
slug: syslog_ng
status: hidden
category: proposals

 # Abstract
After a short introduction to system logging, we will show how the current log
messages look like, and what the problem is with this free text format.
Next, we will introduce you the powerful concept of name-value pairs, and how
you can extract useful information from your logs by parsing log messages into
name-value pairs. Next we will demonstrate the flexibility of syslog-ng's
message parsers (patterndb, csv and JSON parsers), and show you how to
create patterns using a text editor or a GUI. This can also be used to
overwrite sensitive information due to privacy regulations. At the end, you will
learn about the Perl/Python/Lua/Java bindings of syslog-ng Open Source
Edition, how value pairs can be passed to them, and some reference
applications written for syslog-ng.

 # Bio
 Peter is community manager at BalaBit, developers of syslog-ng. He helps
 distributions to maintain the syslog-ng package, follows bug trackers,
 helps users. In his limited free time he is interested in non-x86
 architectures, and works on one of his PPC or ARM machines.
