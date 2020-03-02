#Project 3 by Jared Crummey
#TCMG 412 w/ Prof. Mikeal

from urllib.request import urlretrieve
import os
import re
import collections

redirectCounter = 0
errorCounter = 0
URL = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

#File Checker
if not os.path.isfile(LOCAL_FILE):urlretrieve(URL, LOCAL_FILE)

#Regex Pattern
pattern = r'(.*?) - (.*) \[(.*?)\] \"(.*?) (.*?)\"? (.+?) (.+) (.+)'

#Line Reader
lineRead = open(LOCAL_FILE, 'r').readlines()
