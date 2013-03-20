title: the Network Block Device: network-based block storage for Linux systems
category: talks
status: hidden
date: 2013-03-20

Abstract
--------
The Network Block Device, or NBD, has been in the Linux kernel since the
2.1 days, far predating similar iSCSI and ATA-over-Ethernet
technologies. Whereas the latter two technologies provide generic
low-level SCSI or ATA access over the network, NBD has a far simpler
protocol.

This talk attempts to explain the benefits of NBD over both iSCSI/AoE as
well as over NFS, and will show how to create a simple NBD export.
Finally, we'll also show how Debian 'wheezy' allows installing the
system to an NBD device, allowing for a simple way to create and manage
a thin client.

Speaker
-------
Wouter Verhelst has been maintaining the NBD userspace utilities in
Debian since 2001, and upstream since 2002 when he took over maintenance
from Pavel Machek, who originally implemented NBD. He's been adding
features to both the upstream code and the Debian package, ever since.

Slides
------
will be added after talk
