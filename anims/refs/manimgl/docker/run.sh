#!/bin/sh

# use this line if running from a host with non-nvidia gpu X server
docker run -ti --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v `pwd`:/opt/working manimgl $*

# use this line if running from a host with nvidia gpu X server
#nvidia-docker run -ti --rm -e DISPLAY=$DISPLAY -e NVIDIA_VISIBLE_DEVICES=all  -e NVIDIA_DRIVER_CAPABILITIES=compute,utility,display -v /tmp/.X11-unix:/tmp/.X11-unix -v `pwd`:/opt/working manimgl $*

