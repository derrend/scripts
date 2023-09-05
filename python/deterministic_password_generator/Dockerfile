### IMAGE SETUP ###

## select base image
FROM ubuntu:22.04

## copy files
COPY README.txt deterministic_password_generator.py /root/

## initialise base image
RUN apt-get update && \
    apt-get install -y python3=3.10.6-1~22.04 && \
    apt-get autoclean && \
    apt-get autoremove

## set home dir
WORKDIR /root/

