#!/usr/bin/env lua

local list_lxd = "lxc list -f yaml"

print(os.execute(list_lxd))
