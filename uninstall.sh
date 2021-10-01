#!/bin/bash

sudo systemctl disable power_button.service
sudo systemctl stop power_button.service
sudo rm -rf /etc/systemd/system/power_button.service
sudo rm -rf /usr/local/bin/power_button.py

echo "done."
