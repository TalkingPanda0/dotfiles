set fish_greeting ""
# Start X at login
if [ (ps ax | grep $fish_pid | awk '{print $2}' | grep tty1 | wc -l) -gt 1 ]
	if [ (pgrep sway | wc -l ) -lt 1 ]
       startx --keeptty
	   end
end

pfetch
alias mount "sudo mount"
alias umount "sudo umount"
starship init fish | source
