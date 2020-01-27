import os
from datetime import datetime as dt
import shutil


def copything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc: # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else: raise


currenttime = dt.now().strftime("%y%m%d%H%M%S")
copything("/root/MinecraftServer/mcserver/world", "/root/MinecraftServer/mcbackups/" + currenttime + "/world")
copything("/root/MinecraftServer/mcserver/world_nether", "/root/MinecraftServer/mcbackups/" + currenttime + "/world_nether")
copything("/root/MinecraftServer/mcserver/world_the_end", "/root/MinecraftServer/mcbackups/" + currenttime + "/world_the_end")


for directory in os.listdir("/root/MinecraftServer/mcbackups/"):
    if int(directory) + 5000010 <  int(currenttime):
        shutil.rmtree("/root/MinecraftServer/mcbackups/" + directory)
