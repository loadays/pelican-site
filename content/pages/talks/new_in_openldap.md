title: What's New in OpenLDAP 
status: hidden
category: proposals


# abstract
The Lightning Memory-Mapped Database was introduced at the previous LDAPCon and has been enjoying tremendous success in the intervening two years.  The success of LMDB has led down many different paths:

1. Use of LMDB eliminated bottlenecks at the database level but revealed the presence of other bottlenecks in the slapd code. Recently a number of these other bottlenecks have also been removed, yielding even greater performance gains.
2. LMDB has proved to be a superior database engine for many other projects and uses, and its adoption outside the OpenLDAP Project continues to grow.
3. Use of LMDB in NoSQL projects like HyperDex presents us with the opportunity to again address horizontal scaling, replacing the previous work on back-ndb with a clustered backend that uses OpenLDAP technology at both the highest and lowest layers of the solution.

The talk will discuss some of the internal improvements in slapd due to LMDB, as well as the impact of LMDB on other projects. Also the new HyperDex backend will be presented, as well as new interoperability work with Samba.
