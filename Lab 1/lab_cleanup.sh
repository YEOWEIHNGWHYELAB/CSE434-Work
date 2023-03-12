#!/bin/bash

# reset the bash prompt
PS1="[\u@\h \W]\$"

# reset addresses of both interfaces to garbage
ifconfig p2p1 10.10.10.10 netmask 255.255.255.255
ifconfig p2p2 10.10.10.10 netmask 255.255.255.255

# ensure both interfaces are up to avoid confusion for the next group
ifconfig up p2p1
ifconfig up p2p2

# this should remove all routes but ymmv
ip route flush


echo "Interfaces should now be cleaned up, you may wish to verify by running \"ifconfig\"."