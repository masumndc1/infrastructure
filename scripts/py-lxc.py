#!/usr/bin/env python3

import os
import subprocess

host = {}

if os.path.exists('/usr/bin/incus'):
    out = subprocess.getoutput("sudo incus list -f csv")
else:
    out = subprocess.getoutput("sudo lxc list -f csv")

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
            if k and v:
                file.write(f"{v} {k}\n")
