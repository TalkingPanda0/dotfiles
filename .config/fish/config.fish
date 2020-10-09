set fish_greeting ""
# Start X at login
if [ (ps ax | grep $fish_pid | awk '{print $2}' | grep tty1 | wc -l) -gt 1 ]
	if [ (pgrep qtile | wc -l ) -lt 1 ]
        	     exec startx -- -keeptty 
	   end
end
