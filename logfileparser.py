#Project 3 by Jared Crummey
#TCMG 412 w/ Prof. Mikeal

import urllib
import os
import re
import collections

#File Setup and Variable Reset
loopCount = 0
redirects = 0
errors = 0
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
months_count = {"Jan": 0, "Feb": 0, "Mar": 0, "Apr": 0, "May": 0, "Jun": 0, "Jul": 0, "Aug": 0, "Sep": 0, "Oct": 0, "Nov": 0, "Dec": 0}
jan_logs = open("janLog.txt", "a+");
feb_logs = open("febLog.txt", "a+");
mar_logs = open("marLog.txt", "a+");
apr_logs = open("aprLog.txt", "a+");
may_logs = open("mayLog.txt", "a+");
jun_logs = open("junLog.txt", "a+");
jul_logs = open("julLog.txt", "a+");
aug_logs = open("augLog.txt", "a+");
sep_logs = open("sepLog.txt", "a+");
oct_logs = open("octLog.txt", "a+");
nov_logs = open("novLog.txt", "a+");
dec_logs = open("decLog.txt", "a+");

#Setting up File Length Counter
def file_len(LOCAL_FILE):
    with open(LOCAL_FILE) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


#Finding Get Requests and HTTP
def fileCounter():
    filelog = []
    with open(LOCAL_FILE) as logs:
        for line in logs:
            try:
                filelog.append(line[line.index("GET") + 4:line.index("HTTP")])
            except:
                pass
    counter = collections.Counter(filelog)
    least_common = collections.Counter(filelog).most_common()[-1]
#Most Commonly Requested File Finder
    for count in counter.most_common(1):
        print("Most commonly requested file: {} with {} requests.".format(str(count[0]), str(count[1])))
#Least Commonly Requested File Finder
    for count in counter.most_common(-1):
        print("Least commonly requested file: {} with {} requests.".format(str(count[0]), str(count[1])))
        
 #Timestamp Parser for Log Subdivision
    timestamp = match.group(3)
    month = timestamp[3:6]
    months_count[month] += 1
    match.group(7)
 #ReDirect Counter, Error Counter, and Log Subdivider
    if (match.group(7)[0] == "3"):
        redirects += 1
    elif (match.group(7)[0] == "4"):
        errors += 1
    if (month == "Jan"):jan_logs.write(line)
    elif (month == "Feb"):feb_logs.write(line)
    elif (month == "Mar"):mar_logs.write(line)
    elif (month == "Apr"):apr_logs.write(line)
    elif (month == "May"):may_logs.write(line)
    elif (month == "Jun"):jun_logs.write(line)
    elif (month == "Jul"):jul_logs.write(line)
    elif (month == "Aug"):aug_logs.write(line)
    elif (month == "Sep"):sep_logs.write(line)
    elif (month == "Oct"):oct_logs.write(line)
    elif (month == "Nov"):nov_logs.write(line)
    elif (month == "Dec"):dec_logs.write(line)
    else:
        continue
        
#Output
print("Executing...")
print("Total Log Length" file_len(LOCAL_FILE))
totalEntries = file_len(LOCAL_FILE)
print("Daily Average: " round(totalEntries / 365, 2))
print("Weekly Average: " round(totalEntries / 52, 2))
print("Monthly Average:" round(totalEntries / 12, 2))
print("Monthly Breakdown:" months_count)
print("Redirects:" redirects)
print("Redirect Percentage (3-Series Code): {0:.2%}".format(redirects / totalEntries))
print("Errors:" errors)
print("Client Error (4-Series Code) requests: {0:.2%}".format(errors / totalEntries))
fileCounter()

