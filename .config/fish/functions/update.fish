function update
 pamac update --no-confirm && notify-send "Your Computer Will Shutdown in 10 Seconds" && echo "Your Computer Will Shutdown in 10 Seconds" && sleep 10 && shutdown now
end
