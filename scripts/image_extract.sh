#!/bin/bash

# copy image from server1 to server2
# export and image to /tmp dir image-server1
incus image export 270d829dccdb /tmp
# download it to the local machine
scp user@image-server1:/tmp/270d829dccdbc.tar.gz .
# up load it another image server
scp 270d829dccdbc.tar.gz user@image-server2:/tmp
# export this image to image store
incus image import /tmp/270d829dccdbc.tar.gz
# make an alias
incus image alias create 270d829dccdb ubu24-packer
