title: OpenLDAP's Lightning Memory-Mapped Database
slug: openldap
category: workshop
status: hidden
date: 2013-03-20

Abstract
---------
The Lightning Memory-Mapped Database (LMDB) is a new database library written by Symas Corp. for the OpenLDAP Project. LMDB is a highly optimized B+tree implementation that is orders of magnitude faster and more efficient than everything else in the software world. Reads scale perfectly linearly across arbitrarily many CPUs with no bottlenecks, and data is returned with zero memcpy's. Writes are on average twenty times faster than commonly available databases such as SQLite. The entire library compiles down to only 32K of object code, allowing it to execute completely inside a typical CPU's L1 cache. Backends for OpenLDAP slapd, Cyrus SASL, Heimdal, SQLite, OpenDKIM and many other projects have already been written.

Speaker
-------

Howard Chu is a Founder and the CTO of Symas Corporation and also currently Chief Architect of the OpenLDAP Project. Howard is a prolific contributor to multiple open source projects, and has been writing free software since the early 1980s.

Slides
------
[Slides](/static/slides/20130406-LOADays-LMDB.pdf) _pdf_
