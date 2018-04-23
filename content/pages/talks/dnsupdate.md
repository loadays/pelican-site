title: Is Your DNS Server Up-To-Date (Pieter Lexis)
slug: dnsupdate

## Is Your DNS Server Up-To-Date (Pieter Lexis) ##

Coming February 2019, all Open Source nameservers will [start removing work-arounds](https://en.blog.nic.cz/2018/03/14/together-for-better-stability-speed-and-further-extensibility-of-the-dns-ecosystem/) related to EDNS in their resolvers.
These changes might lead to domains becoming unreachable, as the current implementations will retry without EDNS or probe for EDNS support.
In short, "upgrade to a modern version of your authoritative nameserver" is the advice.
This presentation discusses what EDNS actually is, the background of this decision by the standards and development community and what you can do to check and prevent your domains from going dark.

[Slides](/files/plexis-edns-workaround-removal-loadays-2018.pdf)

## Pieter Lexis ##

Educated as a Systems and Network Engineer and having dabbled with DevOps-y things for years, Pieter's official title now is "Senior PowerDNS Engineer".
As such, he works on the PowerDNS source code, the build/CI/packaging pipeline and running the infrastructure around the PowerDNS open source project.
He is also involved in the broader DNS operations and standards communities to make the Internet a better place.

- Twitter: [@lieter_](https://twitter.com/lieter_)
- GitHub: [@pieterlexis](https://github.com/pieterlexis)

