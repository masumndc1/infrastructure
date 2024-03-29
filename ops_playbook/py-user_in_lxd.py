#!/usr/bin/env python3
# useradd masum
# echo "masum ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/10_masum

import functools
import logging
import os
import subprocess


def logg(*args):
    logging.basicConfig(
        filename='py-user_in_lxd.log',
        format='%(asctime)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.INFO
    )
    return logging.info(*args)


@functools.cache
def hosts():
    out = subprocess.getoutput("lxc list -f csv")
    host = []
    for vm in out.splitlines():
        name = vm.split(',')[0]
        host.append(name)

    return host


def run_command(vm_name, os_pkg):
    lxd_cmd = [f"{os_pkg} update -y",
               f"{os_pkg} install -y openssh-server",
               f"{os_pkg} install -y ansible",
               "systemctl start sshd"]

    for cmd in lxd_cmd:
        subprocess.run(f"lxc exec {vm_name} -- {cmd}", shell=True)


def pkgs():
    dict = {}
    for vm_name in hosts():
        if 'net' in vm_name or 'puppetmaster' in vm_name:
            dict[vm_name] = 'apt-get'
        elif 'sys-dev1' in vm_name or \
            'saltmaster' in vm_name or \
            'sys-prod1' in vm_name or \
                'monitoring' in vm_name:
            dict[vm_name] = 'yum'
        elif 'sys-dev2' in vm_name or 'sys-prod2' in vm_name:
            dict[vm_name] = 'zypper'
        else:
            continue

    return dict


def main():
    c, _ = os.get_terminal_size()
    for k, v in pkgs().items():
        print("+" * c)
        logg(f"{k} {v}")
        run_command(k, v)


if __name__ == "__main__":
    main()
