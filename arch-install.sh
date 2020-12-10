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
echo "Type a Desktop Environment Package name "
read de
echo "Type Terminal Package name"
read term
echo "Type Browser Package name"
read www
echo "Installing:
Desktop Env ironment: $de
Terminal: $term
Browser: $www "
yay -S python3-pip qtile rofi picom termite betterlockscreen qtile nemo nitrogen xclip lxsession materia-gtk-theme qt5-styleplugins lxappearance flameshot pnmixer xfce4-volumed-pulse firefox redshift-gtk-git $de $term $www -y
pip3 install psutil
wget -qO- https://git.io/papirus-icon-theme-install | sh
sed -i "s/user/$USER/gi" ~/.config/qtile/qtile.py
echo "done"
