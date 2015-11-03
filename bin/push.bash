#!/bin/bash

LOCAL_SSH_PORT=1234
VM_HOSTNAME=studbenkhamg-p.cs.ucl.ac.uk
TUNNEL_USERNAME=benkhamg
TUNNEL_HOSTNAME=newgate.cs.ucl.ac.uk

# Kill existing SSH tunnel
EXISTING_PID=$(lsof -i:${LOCAL_SSH_PORT} -t)
if [ ! -z "$VAR" ]; then
	kill -9 $(lsof -i:1234 -t);
fi

# Setup SSH tunnel
ssh -N -L${LOCAL_SSH_PORT}:${VM_HOSTNAME}:22 ${TUNNEL_USERNAME}@${TUNNEL_HOSTNAME} -f

# Run Fabric script
fab deploy

# Close SSH tunnel
EXISTING_PID=$(lsof -i:${LOCAL_SSH_PORT} -t)
if [ ! -z "$VAR" ]; then
	kill -9 $(lsof -i:1234 -t);
fi