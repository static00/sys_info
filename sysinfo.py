import platform
import os
import getpass
import subprocess
import socket
import time
import geocoder
import urllib
import re
import json
import sys

from urllib2 import urlopen

subprocess.call("clear")

user = getpass.getuser()
print("username: " +  user)

time.sleep(0.5)

os = platform.system()
print("os: " +platform.node()) + " " +os + " "

time.sleep(0.5)

ver = platform.release()
print("version: " +ver)

time.sleep(0.5)

machine = platform.machine()
print("machine: " +machine)

time.sleep(0.5)

NetworkType = platform.node()
print("Network: " + NetworkType)

time.sleep(0.5)

print("IPv4: " +socket.gethostbyname(socket.getfqdn()))

time.sleep(0.5)

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

country=data['country']

print("Country: {0}".format(country))

time.sleep(1.5)

print("\nDone !")

time.sleep(1.5)

class bcolors:

        OKGREEN = '\033[92m'

subprocess.call("clear")
print(bcolors.OKGREEN +"\nroot@god:#~")
time.sleep(2.5)
subprocess.call("clear")
print(bcolors.OKGREEN +"root@god:#~ exiting.")
time.sleep(0.5)
subprocess.call("clear")
print(bcolors.OKGREEN +"root@god:#~ exiting..")
time.sleep(0.5)
subprocess.call("clear")
print(bcolors.OKGREEN +"root@god:#~ exiting...")


