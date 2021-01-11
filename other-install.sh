#!/bin/bash
cp  -r .bin ~/
chmod +x ~/.bin/*
cp -r .config/* ~/.config/
cd ~/
git clone https://github.com/TalkingPanda0/dwm.git && cd dwm && sudo make install
git clone https://github.com/TalkingPanda0/st.git && cd st && sudo make install
git clone https://github.com/TalkingPanda0/tabbed.git && cd tabbed && sudo make install
git clone https://github.com/TalkingPanda0/surf.git && cd surf && sudo make install

echo "done"
