
# Probabilistic Programming for Deep Learning

## running

we will use primarly `manim` community: https://github.com/ManimCommunity/manim/


build the docker image

      cd bin
       ./build-docker-image
      cd ..

make sure it is properly registered with your local docker installation (the image name is `manim`)

      docker image ps


render any video

      ./bin/run manim -ql src/videos/talking_about_probability/talking_about_probability.py

notes:

- change `-ql` with `-qh` for rendering in high quality (takes longer)
- the folder `$HOME/Media` is mounted on the container as `/media` by the run script `bin/run`.
- place audio files under `$HOME/Media/audio` (thus, outside github)
- place images under `src/imgs` and include them in the github commits
- use `common.objects.find_imgfile` and `find_audiofile` in your code to locate imgs or audio  on those folders.
- place there any files you might need for rendering 


## OBS configuration

      audio input capture built-it mic vol = -30
                          mic/aux vol = -20
                          filter noise supression RNNoise

      window capture composite
      video settings at 1920x1080, 60 FPS
      output encoder x264


## Intro music

seek for music which is royalty free, with no copyright.

https://www.youtube.com/watch?v=5_ps9cvmiTs&ab_channel=OblivionEpiphany


## manimgl

`manimgl` (the original package by 3b1b) contains examples, objects, etc. that could be useful.

- github repo: https://github.com/3b1b/manim
- github videos of the youtube channel: https://github.com/3b1b/videos
- a mirror github: https://gitcode.net/mirrors/3b1b/manim

Experiments using `manimgl` can be found under `refs/manimgl`. Use the `docker/Dockerfile` that you can find there to create a docker image with manimgl. Use `docker/run.sh` to render scenes. 

If you have an nvidia card, change the `FROM` line in `Dockerfile` and the `run.sh` script. 

include these lines in the main scene file to avoid over logging of debug from opengl

     import pyglet
     pyglet.options['debug_gl'] = False


