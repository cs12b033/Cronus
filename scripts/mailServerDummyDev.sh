#!/bin/bash
source ../.cronusVE/bin/activate
python -m smtpd -n -c DebuggingServer localhost:1025
echo "Exiting now..."