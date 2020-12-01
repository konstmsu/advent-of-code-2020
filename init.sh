#! /usr/bin/env zsh

python3.9 -m venv venv
. ./venv/bin/activate
pip install wheel
pip install -r ./requirements.txt
