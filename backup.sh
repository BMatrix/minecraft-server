#!/bin/bash
name=`date '+%y%m%d%H%M%S'`
mkdir /root/MinecraftServer/mcbackups/$name
cp -r /root/MinecraftServer/mcserver/world/ /root/MinecraftServer/mcbackups/$name/world/
cp -r /root/MinecraftServer/mcserver/world_nether/ /root/MinecraftServer/mcbackups/$name/world_nether/
cp -r /root/MinecraftServer/mcserver/world_the_end/ /root/MinecraftServer/mcbackups/$name/world_the_end/

