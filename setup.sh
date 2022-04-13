#!/bin/bash
# Set up the python project.
#
# Usage:
#   bash setup.sh
#
# author: andreasl

python -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install --upgrade -r requirements.txt
