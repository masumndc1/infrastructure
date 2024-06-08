#!/bin/bash
# a bash script to install ansible in various linux machines

if [[ -f /usr/bin/apt ]]; then
	apt-get update -y
	apt-get install -y ansible
elif [[ -f /usr/bin/yum ]]; then
	yum install -y epel-release
	yum install -y ansible
elif [[ -f /usr/bin/zypper ]]; then
	zypper install -y ansible
fi
