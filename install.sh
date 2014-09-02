wget https://raw.githubusercontent.com/edx/configuration/master/util/install/vagrant.sh -O - | bash
cd /var/tmp/configuration/playbooks
ansible-playbook -i localhost, -c local vagrant-devstack.yml --tags=deploy -e configuration_version=release
su edxapp