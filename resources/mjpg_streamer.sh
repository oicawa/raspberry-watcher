#!/bin/sh
cd /home/pi/Sources/mjpg-streamer/mjpg-streamer-experimental
#./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so"
./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so -x 640 -y 480 -fps 30 -q 10"
