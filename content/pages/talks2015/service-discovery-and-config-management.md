title: Service discovery and configuration management
slug: service_discovery_cfgmgmt
status: hidden
category: proposals


# Abstract

Service discovery frameworks like Etcd and Consul provide the building blocks
for managing highly dynamic infrastructures, where new machines and services
come and go rapidly. Previously it might have been adequate to store a static
list of hosts in a text file or your config management system, but if you're
to take full advantage of virtualisation and containers you need to react
to change more quickly.

This talk will:

* Briefly introduce service discovery tools like Consul, Etcd, SkyDNS and
  Eureka
* Discuss the two speeds of configuration data
* Demonstrate integrating service discovery tools with the Puppet configuration
  management tool
* Touch on the subject of traditional change control processes in the context
  of service discovery

The audience should:

* Learn about the tools, and more importantly approaches, usefull when building
  responsive infrastructure
* See how to integrate service discovery with existing configuration
  management tools and practices
  

# Bio

Gareth Rushgrove is a senior software engineer at Puppet Labs. He works remotely
from Cambridge, UK, building interesting tools for people to better manage
infrastructure. When not working he can be found writing the Devops Weekly
newsletter or hacking on software in new-fangled programming languages.
