---
title: usages of various playbook
---

#  infrastructure

This repository has gone through many changes. Now, it is mainly used
to setup an infra with incus system containers.

- Before running any playbook of this repository its better to copy pub key
  your hosts so that host does not ask for password during login anymore.
  `ssh-copy-id user@host` can be an easy fix.

- If you have automated image creation script like packer or so you can
  add user public key in user's home directory. Another way to create image
  by [ansible-role-packer-incus](https://github.com/masumndc1/ansible-role-packer-incus)

- Run housekeeping.yml playbook to setup user, some required packages etc.
  Run users.yml to target host and run this playbook to give user admin privilege.

```
ansible-playbook -i inventories/hosts housekeeping.yml -l ubu-lxd
```

- Edit all related yml file in host_vars,group_vars and inventories/hosts.

- Copy ansible_install.py script at target node to install ansible it (optional).

##  lxd container specific which also applicable to incus containers.

- SideNote: How to remove lxd/incus service from a node.

    ```
    sudo lxc list
    sudo lxc stop <lxd_container_name>
    sudo lxc delete <lxd_container_names>
    sudo zfs list
    sudo zfs destroy -r <pool_name>
    sudo zpool list
    sudo zpool destroy -f <pool_name>
    sudo lxd cluster remove -f <node_name>
    sudo snap remove lxd
    ```

## Infra pics
<img src = "pics/infra.png">

## usages
```
ansible-playbook -i inventories/hosts site.yml -l lap-macmini
```
