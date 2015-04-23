#!/usr/bin/bash

DATE=$(date +%Y%m%d%H%M%S)
NAME=$DATE"main.json"
cp ../main.json .
cp ../main.json ./backup/$NAME

python poster.py
