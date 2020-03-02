#Project 3 by Jared Crummey
#TCMG 412 w/ Prof. Mikeal

from urllib.request import urlretrieve
import os
import re
import collections

#File Setup and Variable Reset
i = 0
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

#Match Finder.
for line in lineRead:
    matchFinder = re.match(pattern, line)
    if not matchFinder:
        continue
        
#Month Breakdown
months_count = {
    "Jan": 0,
    "Feb": 0,
    "Mar": 0,
    "Apr": 0,
    "May": 0,
    "Jun": 0,
    "Jul": 0,
    "Aug": 0,
    "Sep": 0,
    "Oct": 0,
    "Nov": 0,
    "Dec": 0
}

janlogs = open("janLog.txt", "a+");
feblogs = open("febLog.txt", "a+");
marlogs = open("marLog.txt", "a+");
aprlogs = open("aprLog.txt", "a+");
maylogs = open("mayLog.txt", "a+");
junlogs = open("junLog.txt", "a+");
jullogs = open("julLog.txt", "a+");
auglogs = open("augLogs.txt", "a+");
seplogs = open("sepLogs.txt", "a+")
octlogs = open("octLogs.txt", "a+");
novlogs = open("novLogs.txt", "a+");
declogs = open("decLogs.txt", "a+")

