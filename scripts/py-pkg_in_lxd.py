#!/usr/bin/env python3
# useradd masum
# echo masum ALL=\(ALL\) NOPASSWD: ALL > /etc/sudoers.d/10_masum",

import os
import subprocess

host = []
out = subprocess.getoutput("lxc list -f csv")


for vm in out.splitlines():
    name = vm.split(',')[0]
    host.append(name)

def run_command(os_pkg, vm_name):
    lxd_cmd = [ f"{os_pkg} update -y",
           f"{os_pkg} install -y openssh-server",
           f"{os_pkg} install -y ansible",
           "systemctl start sshd" ]

    for cmd in lxd_cmd:
        subprocess.run(f"lxc exec {vm_name} -- {cmd}", shell=True)

def run():
    for vm_name in host:
        if 'net' in vm_name or 'puppetmaster' in vm_name:
            os_pkg = 'apt-get'
        if 'sys' in vm_name or 'saltmaster' in vm_name:
            os_pkg = 'zypper'
        else: 
            continue

        c, _ = os.get_terminal_size()
        print(vm_name)
        print("+" * c)
        run_command(os_pkg, vm_name)


if __name__ == "__main__":
    run()
