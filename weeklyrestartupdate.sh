#!/bin/sh

screen -S mcserver -X stuff "say The server will perform it's weekly restart. 5 minutes untill reboot$(echo '\015')"
sleep 4m
screen -S mcserver -X stuff "say The server will perform it's weekly restart. 1 minute untill reboot$(echo '\015')"
sleep 30
screen -S mcserver -X stuff "say The server will perform it's weekly restart. 30 seconds untill reboot$(echo '\015')"
sleep 20
screen -S mcserver -X stuff "say The server will perform it's weekly restart. 10 seconds untill reboot$(echo '\015')"
sleep 5
screen -S mcserver -X stuff "say The server will perform it's weekly restart. 5 seconds untill reboot$(echo '\015')"
sleep 1
screen -S mcserver -X stuff "say The server will perform it's weekly restart. 4 seconds untill reboot$(echo '\015')"
sleep 1
screen -S mcserver -X stuff "say The server will perform it's weekly restart. 3 seconds untill reboot$(echo '\015')"
sleep 1
screen -S mcserver -X stuff "say The server will perform it's weekly restart. 2 seconds untill reboot$(echo '\015')"
sleep 1
screen -S mcserver -X stuff "say The server will perform it's weekly restart. 1 second untill reboot$(echo '\015')"
sleep 1
python3.6 /root/MinecraftServer/update.py
