#!/usr/bin/env python

"""
Python must be installed before hand. 
Run OS command to install python first.
for Freebsd run (pkg install python36) first
for Ubuntu16  run: sudo python3 ansible_install.py
for Centos7   run: sudo ./ansible_install.py
for Freebsd12 run: sudo ./ansible_install.py
"""

import os
import platform

def ansible_install():
# Ubuntu 
    if 'Linux' in platform.system():
      if 'Ubuntu' in platform.dist():
        ubuntu_commands = [ "apt update", 
            "apt install -y software-properties-common", 
            "apt-add-repository --yes --update ppa:ansible/ansible",
            "apt install -y ansible"
           ]

        for command in ubuntu_commands:
          os.system(command)

# CentOS
      elif 'centos' in platform.dist():
        centos_commands = [ "yum install -y epel-release",
                          "yum -y update",
                          "yum install -y ansible" 
                        ]

        for command in centos_commands:
          os.system(command)

# FreeBSD
    elif 'FreeBSD' in platform.system():
      freebsd_commands = ["pkg update -f -q",
                         "pkg install -y py37-ansible"
                        ]
      
      for command in freebsd_commands:
         os.system(command)
      
# DragonFly
    elif 'DragonFly' in platform.system():
      dragonfly_commands = [ "pkg install -y py37-ansible"
                         ]
      
      for command in dragonfly_commands:
         os.system(command)

# OpenBSD
    elif 'OpenBSD' in platform.system():
      openbsd_commands = [ "pkg_add ansible"
                       ]
      
      for command in openbsd_commands:
         os.system(command)

    
ansible_install()


