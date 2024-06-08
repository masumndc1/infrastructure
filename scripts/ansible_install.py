#!/usr/bin/env python3

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
    if 'Linux' in platform.system():
        if os.path.exists('/usr/bin/apt'):
            ubuntu_commands = [
                "apt update",
                "apt install -y software-properties-common",
                "apt-add-repository --yes --update ppa:ansible/ansible",
                "apt install -y ansible"
            ]

            for command in ubuntu_commands:
                os.system(command)

        elif os.path.exists('/usr/bin/yum'):
            centos_commands = [
                "yum install -y epel-release",
                "yum -y update",
                "yum install -y ansible"
            ]

            for command in centos_commands:
                os.system(command)

        elif os.path.exists('/usr/bin/zypper'):
            opensuse_commands = [
                "zypper update -y",
                "zypper install -y ansible"
            ]

            for command in opensuse_commands:
                os.system(command)

    elif 'FreeBSD' in platform.system():
        freebsd_commands = [
            "pkg update -f -q",
            "pkg install -y py37-ansible"
        ]

        for command in freebsd_commands:
            os.system(command)

    elif 'DragonFly' in platform.system():
        dragonfly_commands = [
            "pkg install -y py37-ansible"
        ]

        for command in dragonfly_commands:
            os.system(command)

    elif 'OpenBSD' in platform.system():
        openbsd_commands = [
            "pkg_add ansible"
        ]

        for command in openbsd_commands:
            os.system(command)


if __name__ == '__main__()':
    ansible_install()
