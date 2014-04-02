title: Vagrant tutorial
status: hidden
category: proposals

# abstract
Vagrant provides easy to configure, reproducible, and portable work environments built on top of industry-standard technology and controlled by a single consistent workflow to help maximize the productivity and flexibility of you and your team.

To achieve its magic, Vagrant stands on the shoulders of giants. Machines are provisioned on top of VirtualBox, VMware, AWS, or any other provider. Then, industry-standard provisioning tools such as shell scripts, Chef, or Puppet, can be used to automatically install and configure software on the machine.

This tutorial will highlight the following topics

- Introduction to Vagrant
- Setting up boxes, finding and using base boxes
- Configuring Vagrant boxes (Vagrantfile)
- Provisioning
    - Shell
    - Puppet
    - Ansible
- Tips and tricks
- Creating custom base boxes with Packer

If you want to follow along, it's highly recommended to have following software installed in advance:

- Git
- VirtualBox (4.3.x) - https://www.virtualbox.org/
- Vagrant (1.5.x) - http://www.vagrantup.com/
- Initialise the base box 'alphainternational/centos-6.5-x64' so you don't have to download it via the conference wifi: `vagrant box add alphainternational/centos-6.5-x64`

# presentation

- Slides: https://github.com/bertvv/vagrant-presentation
- Demo/Example: https://github.com/bertvv/vagrant-example

# bio
Bert Van Vreckem - <bert.vanvreckem@hogent.be>, [@bertvanvreckem](https://twitter.com/bertvanvreckem)

Bert Van Vreckem is a Lecturer in Computer Science at [University College Ghent](http://fbo.hogent.be/) where he now mainly teaches Linux System Administration. 
