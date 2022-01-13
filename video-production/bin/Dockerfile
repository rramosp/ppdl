FROM manimcommunity/manim

USER root
RUN adduser manimuser sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

RUN apt update
RUN apt install -y wget
RUN apt install -y less
RUN pip install pandas

USER manimuser
