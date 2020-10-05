#!/bin/bash

numlockx on
function run {
  if ! pgrep -f $1 ;
  then
    $@&
  fi
}
~/.bin/mouse.sh
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
run flameshot &
#run steam -silent &
run pnmixer &
run picom --experimental-backends &
run redshift-gtk &
run xfce4-power-manager &
#run discord --start-minimized &
#run lutris &
run dunst &
run nitrogen --restore &
#run variety
