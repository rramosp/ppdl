FROM ubuntu:20.04
#FROM nvidia/cuda:11.0-base

RUN apt update
RUN apt install -y wget

RUN mkdir -p /opt/working
WORKDIR /opt

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.10.3-Linux-x86_64.sh
RUN bash Miniconda3-py38_4.10.3-Linux-x86_64.sh -b
ENV PATH=/root/miniconda3/bin:${PATH} 

WORKDIR /opt/working

RUN apt-get install -y ffmpeg vim xvfb lsb-release
RUN apt-get install -y libglu1-mesa-dev freeglut3-dev mesa-common-dev
RUN apt-get install -y x11-apps mesa-utils
RUN apt install -y libpango1.0-dev pkg-config python3-dev
RUN apt install -y texlive-base texlive-latex-recommended texlive texlive-latex-extra  texlive-fonts-extra texlive-science
RUN apt install -y gcc
RUN pip install manimpango --no-binary :all: --force
RUN pip install PyOpenGL-accelerate
RUN pip install manimgl
RUN pip install gym pyvirtualdisplay
RUN pip install scikit-image scikit-learn matplotlib pandas


# use the manimgl.sh script in this dir
#
#     ./run.sh manimgl example_scenes.py

# if host has nvidia GPU X display
#
#    - install nvidia-docker  
#           https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker
#
#    - uncomment the nvidia-docker line in run.sh
