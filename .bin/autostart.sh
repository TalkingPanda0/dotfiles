#!/bin/bash

numlockx on
function run {
  if ! pgrep -f $1 ;
  then
    $@&
  fi
}
~/.bin/mouse.sh
run lxsession &
run flameshot &
#run steam -silent &
run pnmixer &
run picom &
run kdeconnect-indicator &
run /usr/lib/kdeconnectd
run redshift-gtk &
run xfce4-power-manager &
#run discord --start-minimized &
#run lutris &
run dunst &
run nitrogen --restore &
#run variety
