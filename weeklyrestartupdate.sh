#!/bin/sh

# Inform the users on how long its going to take before the server reboots
function notify {
  screen -S mcserver -X stuff "say The server will perform it's weekly restart. $1 until reboot$(echo '\015')"
  if [[ "$2" == "" ]]; then
    sleep 1
  else
    sleep "$2"
  fi
}

notify "5 minutes" "4m"
notify "1 minutes" "30"
notify "30 seconds" "20"
notify "10 seconds" "5"
notify "5 seconds"
notify "4 seconds"
notify "3 seconds"
notify "2 seconds"
notify "1 second"

python3.6 /root/MinecraftServer/update.py
