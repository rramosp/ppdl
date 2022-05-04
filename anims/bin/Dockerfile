FROM manimcommunity/manim

USER root
RUN adduser manimuser sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

RUN apt update
RUN apt install -y wget
RUN apt install -y less
RUN apt install -y vim
RUN yes NO  | apt install -y sudo
RUN pip install pandas matplotlib seaborn

USER manimuser
