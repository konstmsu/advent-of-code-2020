#! /usr/bin/env zsh

python3 -m venv venv
. ./venv/bin/activate
python -m pip install --upgrade pip
pip install wheel
pip install -r ./requirements.txt
