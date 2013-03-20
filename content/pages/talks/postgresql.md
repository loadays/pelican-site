title: bigger data in postgres 9.2  
category: talk
status: hidden
date: 2013-03-20

Abstract
---------

Companies today collect more and more data. And those companies also want to
ask more and more questions to those datawarehouses.
The time that a datawarehouse only needed to be tuned for read queries, and run
the etl / elt once a night is over. This brought us some new challenges.
With databases sizing to over 500GB, doing hundreds, sometimes even thousands
of inserts/updates/deletes every second, and running select queries on the
database who's motto is: the more tables we join, the more fun, it brought us
some new challenged on how to configure and tune those databases (and servers).
Not only dba skills were needed, but good system engineering skills were used
too, to get the db running smooth under the heavy workload.
We discovered that we needed more than one server. luckily postgres 9 now
provides us with streaming replication too. In this talk I will discuss how we
took on all challenges, how we setup up our backup / replication strategy, and
that all with as little effort as possible by using the right tools for the
job.

Speaker
-------

Bert Desmet

Slides
------
will be added after talk
