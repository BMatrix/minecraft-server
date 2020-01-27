import os, sys, stat
import json
import time
from urllib.request import Request, urlopen, urlretrieve

currentversion = open("/root/MinecraftServer/currentversion.txt", "r")

versionurl = "https://papermc.io/api/v1/paper/"

versionsearch = json.load(urlopen(Request(versionurl, headers={'User-Agent': 'Mozilla/5.0'})))
latestversion = versionsearch["versions"][0]

buildurl = versionurl + latestversion + "/"

buildsearch = json.load(urlopen(Request(buildurl, headers={'User-Agent': 'Mozilla/5.0'})))
latestbuild = buildsearch["builds"]["latest"]

if currentversion.read() != str(latestversion + "/" + latestbuild):
    print("Updating...")
    currentversion.close()
    os.system('/root/MinecraftServer/stopserver.sh')
    time.sleep(10)
    downloadurl = buildurl + latestbuild + "/download"
    download = urlopen(Request(downloadurl, headers={'User-Agent': 'Mozilla/5.0'})).read()
    os.remove("/root/MinecraftServer/mcserver/paper.jar")
    jar = open("/root/MinecraftServer/mcserver/paper.jar", "wb")
    jar.write(download)
    jar.close()
    os.chmod("/root/MinecraftServer/mcserver/paper.jar", stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    os.system('/root/MinecraftServer/startserver.sh')
    currentversion = open("./currentversion.txt", "w")
    currentversion.write(str(latestversion + "/" + latestbuild))
    currentversion.close()
else:
    print("Already on lastest version")
