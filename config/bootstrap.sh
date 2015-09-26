#!/bin/bash

# Update the box
# --------------
# Downloads the package lists from the repositories
# and "updates" them to get information on the newest
# versions of packages and their dependencies
apt-get update

# Install curl
apt-get install -y curl

# Install Vim
apt-get install -y vim

# Install Python
apt-get install -y  python
apt-get install -y  python-dev
apt-get install -y  python-pip

apt-get install -y sqlite3

# Install requirements.txt
pip install -r /vagrant/config/requirements.txt

# Install Docker
curl -sSL https://get.docker.com/ | sh
service restart docker

exit 0
