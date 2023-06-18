FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-runtime
# --> python 3.7

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y tzdata
# timezone setting
ENV TZ=Asia/Tokyo

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /workspace
