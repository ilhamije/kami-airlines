#!/bin/bash

PWD_DIR="$(pwd)"
PROJECT_DIR="$PWD_DIR/airlines"
VENV_DIR="$PWD_DIR/venv"

if [ -d "$VENV_DIR" ]; then
    echo $VENV_DIR
    source "$VENV_DIR/bin/activate" && echo "Existing venv activated"
else
    python3 -m venv "$VENV_DIR"
    echo $VENV_DIR
    source "$VENV_DIR/bin/activate" && echo "New venv activated"
    pip install -r requirements.txt
fi

# cd "$PROJECT_DIR" || exit

# echo "Running ./manage runserver..."
# ./manage runserver
