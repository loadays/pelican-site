title: Simple system testing with Roundup and Ansible (Pieter Hollants)
slug: ansible_roundup

## Simple system testing with Roundup and Ansible (Pieter Hollants) ##

Automated testing has become a natural part of toolboxes, not only for application developer's toolboxes
but also for sysadmins sailing under the oh-so-misinterpreted DevOps flag. Testing of installed systems
goes along with configuration management just nicely and has been introduced e.g. at CfgMgmtCamp for Ansible in
combination with Inspec.

In this talk I want to introduce you to a much simpler alternative that doesn't require a dedicated
programming language stack such as Python or Ruby: roundup. roundup is a really itsy-bitsy-tiny little
rapper that adds just enough around your off-the-shelf Bash test functions to run isolated and get
easy overviewable test results. If this doesn't make you immediately roll with your eyes for fear of
a maintenance nightmare, let me remind you how our well-established Un*x heritage of tools and plumbing
allows us to even test our mail server's basic functionality without needing 31337 add-on libraries.
For the bravest (or craziest, depending on the viewpoint) among you, I will show how dynamic test generation
takes us close to the border of language abuse.

In the second part I will then also show how I integrate roundup with my Ansible playbooks, giving instant
feedback that desired configuration has not only been applied successfully but also yielded the intended
system state. And this all without fancy setup steps and orphaned test artifacts lingering around on tested
systems.

## Pieter Hollands ##

Pieter Hollants solaced himself over the downfall of Commodore and the beloved Amiga world by discovering
the Un*x/Linux world at the end of the 90s. After fulfilling his duties at the IT support front, promoting
himself to "Senior Intern" at Linux outlet SUSE and abusing his position as Linux Systems Engineer at
German Air Traffic Control to become a resident conference visitor, Pieter has returned to enjoying the
freedom as an independent Linux developer, consultant and occasional involuntary sysadmin. He runs some
small Open Source projects of his own but mostly contributes every now and then, here and there and
blogs at http://www.0xf8.org.

