#!/bin/bash
a=0
if [[ $(id -u) == "0" ]]
then
    echo "this script shouldn't run as root"
fi
if ! command -v "yay" &> /dev/null
then
    echo "yay could not be found."
    echo "installing yay"
    sudo pacman -S go --noconfirm --needed
    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -ic --noconfirm --needed
    clear
    echo "yay installed"
fi
echo "yay Found"
cp  -r .bin ~/
chmod +x ~/.bin/*
cp -r .config/* ~/.config/
cd ~/
yay -S picom-jonaburg-git python3-pip qtile rofi picom termite betterlockscreen qtile nemo nitrogen xclip lxsession materia-gtk-theme qt5-styleplugins lxappearance flameshot pnmixer xfce4-volumed-pulse firefox redshift-gtk-git -y
git clone https://github.com/TalkingPanda0/dwm.git && cd dwm && sudo make install
git clone https://github.com/TalkingPanda0/st.git && cd st && sudo make install
echo "done"
