title: Troubleshooting Network Services (Bert Van Vreckem)
slug: network-troubleshooting

## Troubleshooting Network Services (Bert Van Vreckem) ##

This workshop introduces basic troubleshooting skills for setting up network services (e.g. web, database, fileserver, DHCP, DNS, etc.) on Linux. The TCP/IP protocol stack forms the scaffolding, each layer from bottom to top being a consecutive phase in the process. At each level, the most important items to check are discussed, along with the most suitable commands for modern Linux distributions (specifically, `systemd`-based ones).  
In the workshop, we'll work with CentOS 7, but the underlying principles can be applied to any Linux distribution, or even any operating system in general.  
Topics that will be discussed:

- General guidelines
- Checks for each TCP/IP layer:
    - Link/network access layer (network adapter settings)
    - Internet layer (IP address, gateway, DNS settings, routing within the LAN)
    - Transport layer (service status, server sockets, firewall settings)
    - Application layer (logs, configuration files)
- SELinux troubleshooting
- If time permits, and depending on the preference of the participants, some application specific troubleshooting tips for:
    - Samba
    - BIND
    - `dhcpd`

During the session, participants will troubleshoot a badly configured web server on CentOS 7.

#### Requirement ####

Participants need to bring a laptop (with the OS of *their* choice) with the following software installed:

- Git client
- VirtualBox
- Vagrant

Participants are expected to have basic knowledge about:

- The TCP/IP protocol stack
- Basic Linux command line skills
- Linux file permissions

#### Preperation ####

It's important to do the following steps *before* the conference, as it involves downloading large files.

1. Ensure the **software** listed above is installed on your system.
2. Check your **VirtualBox settings**:
    - Ensure the *Extension Pack* is installed
    - Ensure you have a *Host Only network* configured with the following settings:
        - On recent VirtualBox versions, go to Global Tools > Host Network Manager
        - On older versions, go to File > Preferences > Network > Host Only networks
        - You should have at least one Host-Only network, with following settings:
            - IPv4 Address: 192.168.56.1
            - Network Mask: 255.255.255.0
            - DHCP server (optional): 192.168.56.100
            - Lower address bound: 192.168.56.101
            - Upper address bound: 192.168.56.254
3. Clone the **repository** with slides & demo/assignment code

    ```shell
    $ git clone https://github.com/bertvv/presentation-network-troubleshooting.git
    ```

4. Ensure you have the Vagrant base box used in the session installed (~520MB download):

    ```shell
    $ vagrant box add --provider virtualbox bento/centos-7.4
    ```

Do not hesitate to contact the speaker if you run into problems.

#### Additional Information ####

- Slides and code: <https://github.com/bertvv/presentation-network-troubleshooting>
- Linux Network Troubleshooting guide: <https://bertvv.github.io/linux-network-troubleshooting/>

## Bert Van Vreckem ##

Bert is lecturer ICT at [University College Ghent](https://hogent.be/fbo) and [CVO Panta Rhei](http://www.avondschool.be/), where he teaches a.o. Linux, System Engineering project, Research Techniques, etc.

His open source contributions include a.o.

- Ansible roles for network services, focus on EL7 (e.g. Apache, BIND, dhcpd, PXEBoot server, Vsftpd, Samba, etc)
- Scripts & tools for managing Vagrant & Ansible
- Learning materials (e.g. cheat sheets and checklists, syllabus Enterprise Linux, assignments, etc.)

Github : <https://github.com/bertvv/> and <https://github.com/hogenttin>

Twitter : [@bertvanvreckem](http://twitter.com/bertvanvreckem)

