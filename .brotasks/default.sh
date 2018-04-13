#!/bin/sh

project=$(basename `pwd`)

init () {
  tmux new-session -A -s rango1 \; send-keys 'cd /home/jturi/dev/rango; source /home/jturi/venv/rango36/bin/activate' C-m \;
}

$@
