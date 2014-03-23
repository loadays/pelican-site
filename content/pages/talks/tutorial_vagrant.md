title: Vagrant tutorial
status: hidden
category: proposals

# abstract
Vagrant provides easy to configure, reproducible, and portable work environments built on top of industry-standard technology and controlled by a single consistent workflow to help maximize the productivity and flexibility of you and your team.

To achieve its magic, Vagrant stands on the shoulders of giants. Machines are provisioned on top of VirtualBox, VMware, AWS, or any other provider. Then, industry-standard provisioning tools such as shell scripts, Chef, or Puppet, can be used to automatically install and configure software on the machine.

This tutorial will highlight the following topics

- Introduction to Vagrant, setting up a new box
- Configuring Vagrant boxes (Vagrantfile)
- Provisioning Vagrant boxes
    - Puppet
    - Ansible
- Tips and tricks
- Getting base boxes
- Creating custom base boxes with Packer

If you want to follow along, it's highly recommended to have following software installed in advance:

- VirtualBox - https://www.virtualbox.org/
- Vagrant - http://www.vagrantup.com/
- Download this CentOS base box: http://packages.vstone.eu/vagrant-boxes/centos-6.x-64bit-latest.box


# bio
Bert Van Vreckem - <bert.vanvreckem@hogent.be>, [@bertvanvreckem](https://twitter.com/bertvanvreckem)

Bert Van Vreckem is a Lecturer in Computer Science at [University College Ghent](http://fbo.hogent.be/) where he now mainly teaches Linux System Administration. 
