function minecraft 
	sudo cpupower frequency-set -g performance
	killall -9 multimc
	multimc --launch $argv
end
