#!/usr/bin/env python3

import subprocess

out = subprocess.getoutput("sudo lxc list -f csv")
host = {}

for vm in out.splitlines():
    name = vm.split(',')[0]
    ip = vm.split(',')[2].split(' ')[0]
    host[name] = ip

with open("/etc/hosts", "r+") as file:
    match = 0
    lines = file.readlines()
    for k, v in host.items():
        for line in lines:
            if k in line:
                match = match + 1

        if not match:
            file.write(f"{v} {k}\n")
