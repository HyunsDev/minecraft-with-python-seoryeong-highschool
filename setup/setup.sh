#!/bin/sh

cd ~
sudo apt update -y
sudo apt upgrade -y
sudo apt install -y fonts-unfonts-core
git clone https://github.com/HyunsDev/minecraft-with-python-seoryeong-highschool
cd minecraft-with-python-seoryeong-highschool
ECHO "Install Finish"