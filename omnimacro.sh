#!/bin/bash
# Activate the correct python virtual environment and run omnimacro.py.
# If the environment was not set up yet set it up.
#
# Usage:
#   omnimacro.sh [-p|--play]
#
# author: andreasl

cd "$(dirname "${BASH_SOURCE[0]}")" || exit 1
source .venv/bin/activate || { bash setup.sh && source .venv/bin/activate; }

python omnimacro.py "$@"
