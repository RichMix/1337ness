#!/bin/bash

git clone https://github.com/BrohdeXC/1337ness.git
cd 1337ness && chmod +x 1337NESS LeetSpeak.py
rm LICENSE README.md
sudo mv ../1337ness/* /usr/local/bin/ && cd .. && rm -rf 1337ness/
