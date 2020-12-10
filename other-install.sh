#!/bin/bash
cp  -r .bin ~/
chmod +x ~/.bin/*
cp -r .config/* ~/.config/
cd ~/
pip3 install psutil
wget -qO- https://git.io/papirus-icon-theme-install | sh
sed -i "s/user/$USER/gi" ~/.config/qtile/qtile.py
echo "done"
