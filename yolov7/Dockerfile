FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

ARG FCM_VERSION=main
ENV FCM_VERSION=${FCM_VERSION}

# install required packages (apt, python)
RUN apt-get clean && apt-get -y update
RUN apt-get -y upgrade && apt-get install -y sudo apt-utils

RUN apt-get install -y wget build-essential checkinstall && \
  apt-get install -y libreadline-dev \
  libncursesw5-dev \
  libssl-dev \
  libsqlite3-dev \
  tk-dev \
  libgdbm-dev \
  libc6-dev \
  libbz2-dev \
  zlib1g-dev \
  libncurses5-dev \
  libnss3-dev \
  libffi-dev \
  liblzma-dev \
  git
RUN apt-get install -y cmake protobuf-compiler

# install python3.8
RUN sudo apt update && sudo apt install -y python3-pip python3-dev python3-setuptools
RUN pip3 install --upgrade pip
RUN apt-get install -y python3-dev python3-venv python3-tk

RUN sudo apt -y update && sudo apt -y upgrade
RUN sudo apt install -y software-properties-common
RUN sudo add-apt-repository ppa:deadsnakes/ppa
RUN sudo apt-cache policy python3.8
RUN sudo apt install -y python3.8
RUN sudo apt install -y python3.8-dev python3.8-venv python3.8-tk

# compressai
RUN apt-get install -y gawk bison

RUN mkdir /workspace
WORKDIR /workspace

CMD ["/bin/bash"]
