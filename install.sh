#!/usr/bin/bash

sudo wget https://raw.githubusercontent.com/edx/configuration/master/util/install/vagrant.sh -O - | bash
sudo cd /var/tmp/configuration/playbooks
sudo ansible-playbook -i localhost, -c local vagrant-devstack.yml --tags=deploy -e configuration_version=release
sudo su edxapp