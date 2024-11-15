# Dockerfile 수정중

FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

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

# install python3.10
