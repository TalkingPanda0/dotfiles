#!/bin/bash
if [[ $(id -u) == "0" ]]
then
    echo "this script shouldn't run as root"
fi
cp  -r .bin ~/
chmod +x ~/.bin/*
cp -r .config/* ~/.config/
cd ~
sudo add-apt-repository ppa:regolith-linux/unstable -y
sudo apt-get upgrade
sudo apt-get install qtile nitrogen termite fonts-roboto rofi picom python-pip i3lock nemo xclip qt5-style-plugins materia-gtk-theme lxappearance xbacklight kde-spectacle nautilus xfce4-power-manager pnmixer network-manager-applet firefox redshift-gtk lxsession fish -y
pip3 install psutil
wget -qO- https://git.io/papirus-icon-theme-install | sh
sed -i "s/user/$USER/gi" ~/.config/qtile/qtile.py
sudo echo "XDG_CURRENT_DESKTOP=Unity
QT_QPA_PLATFORMTHEME=gtk2"  >> /etc/environment
echo "done"
