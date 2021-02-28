FROM alpine
RUN apk update && apk add python3
COPY ./lab5.py ./home/lab5.py
WORKDIR /home
