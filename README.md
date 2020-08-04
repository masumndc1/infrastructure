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


