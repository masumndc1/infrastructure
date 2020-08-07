# infrastructure

1. first setup ssh with your all hosts
`ssh-copy-id` can be an easy fix.

2. If you have automated image creation script like packer or so you can 
   add user public key in user's home directory.

3. run sudo.yml to give user admin priviledge.

3. Edit all related variables in host_vars,group_vars and hosts.yml accordingly.

4. Run housekeeping.yml playbook.

5. Run puppetcluster.yml to set up puppet master agent.

6. Run r10k.yml to install r10k in puppetmaster.
 
7. Run deployment.yml to deploy environment in agent nodes.

8. Run saltcluster.yml to install salt-master and salt-minion nodes.

9. Run lxd.yml to install lxd package through snap

10. Run `sudo lxd init` manually in all nodes. Currently we have only 3 compute nodes in this cluster. Therefore It will be easier for use to initial this way.When we have many compute nodes we can think of preseed and and using certificate in preseed.
## Infra pics 
![infra pic] (https://raw.githubusercontent.com/masumndc1/infrastructure/master/pics/infra.jpg)
