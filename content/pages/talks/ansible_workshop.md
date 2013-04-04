title: Tutorial about provisioning and management using Ansible
slug: tutorial-about-provisioning-and-management-using-ansible
category: workshop
status: hidden
date: 2013-03-20

Requirements
-------------

```bash
 - Laptop with KVM support 
   - CPU with VMX/SVM CPU instruction
   - VT enabled in the BIOS
 - Libvirt installation with KVM support
 - About 5GB free disk space
```


Abstract
---------

About every year new tools for systems management are being released that fill a certain niche, or exploit the possibilities of configuration management by using yet another implemlentation language or a single compelling feature. And from a cynical point-of-view, Ansible is not different. However the design principles behind Ansible make it an exciting new alternative that simplifies and redefines systems management.

Key features of Ansible:

 - modular design
 - requires no agent, uses SSH (or zeromq)
 - requires no PKI infrastructure
 - multi-tier orechestration
 - dead simple

This tutorial will highlight the following topics:

 - Introduction to Ansible concepts
   - Inventories, Facts, Playbooks, Modules, Plugins
 - Using Ansible for systems management
   - Running commands in parallel
   - Automate using playbooks
   - Reporting using Ansible API
 - Using Ansible for orchestration
   - Creating advanced playbooks
 - Using Ansible for provisioning
   - Integration with EC2, vSphere, KVM or RHEV


Speaker
--------

-   Dag Wieers <dag@wieers.com>
-   Jeroen Hoekx <jeroen@hoekx.be>


Slides
-------

will be added after talk
