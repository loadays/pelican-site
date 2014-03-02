title: Inside debian-installer Automation through preseeding, extending, and more!
status: hidden
category: proposals

# abstract
The debian-installer has been the installation program of Debian since
Debian 3.1 "sarge", released in 2005. In addition, it has been used by
Ubuntu since Ubuntu 6.06 "dapper drake", though recently on the
alternate installation image only.

Debian-installer is a modular installer with many features, allowing the
user to easily set up things like software RAID, LVM, full-disk
encryption, a large choice of file systems, and more. Some of its more
recent features include full IPv6 support, btrfs support, WPA encryption
for wireless links, and diskless installation to iSCSI or NBD targets;
and all this on all of the Debian-supported architectures, including
kFreeBSD.

This high number of features is enriched by an ability to fully automate
the installation, through a system known as "preseeding". With
preseeding, one can turn the interactive installer into a fully
automatic installation system; and through the late_command feature, it
is possible to run scripts after the installation, useful for doing
things like chaining a configuration management system.

We will go over how debian-installer is structured internally, how
preseeding works, and then review a small but real-life example of
preseeding.


