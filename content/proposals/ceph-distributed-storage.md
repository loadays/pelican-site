title: Ceph distributed storage
status: hidden
category: proposals

# Abstract

Abstract for the talk: We're building clouds these days, we can add RAM and CPU power as we want, but what about storage?

Almost every NAS and SAN has a limitation. Could be the amount of drives, shelfs, network connections or something else. The bottom-line is, they all have limitations.

What if you want to build a cloud with 1PB of storage behind it. What if you want to do that on commodity hardware and with open source software? Then you probably want Ceph.

Ceph is an open source distributed storage platform which allows you to scale online into the PetaBytes.

It has been integrated into CloudStack and OpenStack to run your cloud directly from Ceph.

## Audience

The audience must be familiar with storage in general.


Speaker
-------
"Wido den Hollander (1986) is born and raised in the Netherlands.

In 2004 he co-founded a webhosting company which grew out to be one of the largest.

He was always searching for storage solutions for his hosting company and found Ceph in 2010.

His role as CTO brought him into contact with the CloudStack project in the early months of 2012.

Wido had searching for the best cloud orchestration software for his company which could be combined with the distributed storage platform Ceph.

Eventually Wido developed the Ceph integration for CloudStack which lead him to being a committer and eventually PMC member of the project.