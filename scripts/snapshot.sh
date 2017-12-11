#!/bin/bash

gnome-screenshot -a -c
xclip -selection clipboard -t image/png -o > /tmp/snapshot.png
python upload.py /tmp/snapshot.png | xclip -selection clipboard
