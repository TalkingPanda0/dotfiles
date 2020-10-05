function clean
sudo  pamac clean --no-confirm && sudo pacman -Scc --noconfirm && sudo rm -rf ~/.cahche && paccache -r && sudo pacman -Rns (pacman -Qtdq) && rm -rf ~/.cache/* && sudo rm -rf ~/.cache/* && sudo journalctl --vacuum-time=4weeks
end
