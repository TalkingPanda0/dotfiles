#!/bin/bash
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
yay -S python3-pip qtile rofi picom termite i3lock-fancy qtile nemo nitrogen xclip polkit-gnome materia-gtk-theme qt5-styleplugins lxappearance flameshot pnmixer xfce4-power-manager firefox redshift-gtk-git -y
pip3 install psutil
wget -qO- https://git.io/papirus-icon-theme-install | sh
sed -i "s/user/$USER/gi" ~/.config/qtile/qtile.py
sudo echo "XDG_CURRENT_DESKTOP=Unity
QT_QPA_PLATFORMTHEME=gtk2"  >> /etc/environment
echo "done"
