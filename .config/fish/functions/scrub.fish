function scrub
    sudo btrfs scrub start / && watch sudo btrfs scrub status -d / && sudo btrfs scrub start /home && sudo btfs scrub status -d /home
end
