#!/usr/bin/env python3

import subprocess

host = {}
out = subprocess.getoutput("sudo incus list -f csv")


def main():
    for vm in out.splitlines():
        name = vm.split(",")[0]
        ip = vm.split(",")[2].split(" ")[0]
        host[name] = ip

    with open("/etc/hosts", "r+") as file:
        lines = file.readlines()
        for k, v in host.items():
            match = 0
            for line in lines:
                if k in line:
                    match = match + 1

            if not match:
                if k and v:
                    file.write(f"{v} {k}\n")


if __name__ == "__main__":
    main()
