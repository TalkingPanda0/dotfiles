set fish_greeting ""
# Start X at login
if [ (pgrep qtile | wc -l ) -lt 1 ]
             exec startx -- -keeptty 
   end



