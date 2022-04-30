FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y tzdata
RUN ln -fsn /usr/share/zoneinfo/Europe/Moscow /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata
RUN apt-get install -y python3 python3-pip wget git libcurl3-gnutls ffmpeg libsm6 libxext6
RUN python3 -m pip install torch==1.8.1 torchvision==0.9.1 opencv-python

RUN pip install mmcv-full==1.4.0

WORKDIR ./workdir

CMD ["/bin/sh", "./launch.sh"]
