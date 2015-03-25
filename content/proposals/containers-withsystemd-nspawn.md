title: Containers with systemd-nspawn
status: hidden
category: proposals

# Abstract

While probably the most prominent, Docker is not the only tool for building
and managing containers. Originally meant to be a "chroot on steroids" to
help debug systemd, systemd-nspawn provides a fairly uncomplicated approach
to work with containers. Being part of systemd, it is available on most
recent distributions out-of-the-box and requires no additional dependencies.

This talk will introduce the concepts involved in containers and will guide
you through the steps of building a container from scratch. The payload
will be a simple service, which will be activated when the first connection
request arrives.


# Bio

Gábor is a long time user and advocate of Linux and Open Source Software.
As an independent Linux server infrastructure expert he enjoys working with
customers committed to increase operational excellence by turning mundane
administrative effort into the ability to innovate. In numerous roles
ranging from operations, architecture and technical project management, he
has over 15 years of experience in large enterprise data centers. He is an
active member of the Dutch openSUSE community, where he helps organizing
local events.

