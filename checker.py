#!/usr/bin/python3

import logging
import re
import socket
import subprocess
import sys
import urllib.request
from datetime import date

#logging.basicConfig(filename="checker.log", level=logging.INFO)
FORMAT = "%(asctime)-15s %(message)s"
logging.basicConfig(filename="checker.log", format=FORMAT,level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S')

# GET Target Version - from file "checker.conf".
try:
    result = open("checker.conf",'r')
    target_version = result.readline().strip()
except Exception as e:
    #print("EXCEPTION READING: version.conf. EXCEPTION IS: %s" % (e))
    logging.critical("EXCEPTION READING: checker.conf")
    sys.exit(1)

# GET APP DNS NAME
state=0
with open('terraform.tfstate', 'r') as searchfile:
    for line in searchfile:
        if re.search( r'instance_state', line, re.M|re.I):
            state="running"

if state == "running":
    result = subprocess.run(['terraform', 'output', 'aws_instance_public_dns'], stdout=subprocess.PIPE)
    name = result.stdout.decode('utf-8').strip()
else:
    logging.critical("EXCEPTION: terraform.tfstate file shows not running")
    sys.exit(1)

# TEST Port 80
s = socket.socket()
address = socket.gethostbyname(name)
port = 80  # port number is a number, not string
try:
    s.connect((address, port))
    logging.info("SUCCESS: " + name + " port 80 is up")
except Exception as e: 
    logging.critical("EXCEPTION: Something's wrong with %s:%d. Exception is %s" % (address, port, e))    
    sys.exit(1)
finally:
    s.close()

# Get version.txt page and check version
version_page="http://" + name + "/version.txt"
try:
    url = urllib.request.urlopen(version_page)
    vbytes = url.read()
    found_version = vbytes.decode("utf8").strip()
    logging.info("SUCCESS: " + version_page + " found")
except Exception as e:
    logging.critical("EXCEPTION READING: version.txt")
    #print("EXCEPTION READING: version.txt. EXCEPTION IS: %s" % (e))
    sys.exit(1)
finally:
    url.close()

if target_version == found_version:
    logging.info("SUCCESS: version " + found_version + " found")
else:
    logging.error("FAILED: Found " + found_version + ", expected " + target_version)
