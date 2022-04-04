#!/bin/sh

# 1/20 gives 3 imgs per minute, 1/60 gives 1 img per minute, etc.

ffmpeg -i $1 -vf fps=1/20 img%03d.jpg
