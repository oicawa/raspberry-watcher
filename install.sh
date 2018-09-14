#!/bin/sh

#
# Power Off Switch
# 
mkdir ~/bin/
cp resources/power-off-switch.py ~/bin/
cp resources/power-off-switch.service /lib/systemd/system/
systemctl enable power-off-switch.service

#
# mjpg-streamer
# 
cp resources/mjpg_streamer.sh ~/bin/
cp resources/mjpg_streamer.service /lib/systemd/system/
systemctl enable mjpg_streamer.service

