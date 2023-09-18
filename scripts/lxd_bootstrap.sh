#!/bin/bash

echo -e "Installing python"
yum install -y python || apt-get install -y python
echo -e "downloading ansible python installer"
wget -c https://raw.githubusercontent.com/masumndc1/infrastructure/master/ansible_install.py
curl -O https://raw.githubusercontent.com/masumndc1/infrastructure/master/ansible_install.py
echo -e "Installing ansible"
python ansible_install.py
echo -e "Adding user, public key, installing sudo and openssh-server and running it"
curl -O https://raw.githubusercontent.com/masumndc1/infrastructure/master/pkg_srv.yml 
ansible-playbook pkg_srv.yml
