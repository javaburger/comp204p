#!/bin/bash

LOCAL_SSH_PORT=1234
VM_HOSTNAME=studbenkhamg-p.cs.ucl.ac.uk
TUNNEL_USERNAME=benkhamg
TUNNEL_HOSTNAME=newgate.cs.ucl.ac.uk

# Kill existing SSH tunnel
killall ssh

# Setup SSH tunnel
ssh -N -L${LOCAL_SSH_PORT}:${VM_HOSTNAME}:22 ${TUNNEL_USERNAME}@${TUNNEL_HOSTNAME} -f

# Run Fabric script
fab -f ~/www/comp204p/bin/deploy.py deploy

# Close SSH tunnel
killall ssh