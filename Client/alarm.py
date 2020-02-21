
import datetime
import requests
import time
from playsound import playsound
import os

timeHour = 0
timeMinute = 0
second = 0
serverPath = "http://localhost:8080"
schedule = "/schedule"
now = datetime.datetime.now()

def getData():
    URL_SCHEDULE = serverPath + schedule
    r = requests.get(url=URL_SCHEDULE)
    data = r.json()
    name = data["name"]
    timeHour = int(data["hour"])
    timeMinute = int(data["minute"])
    fileType = data["type"]

    filePath = '../downloads/'+ name
    if not os.path.exists(filePath):
        r = requests.get(serverPath+"/"+ name)
        with open('../downloads/'+ name,'wb') as f:
            f.write(r.content)
    return timeHour, timeMinute, fileType, filePath

def playFile(filePath):
    print filePath
    if filePath is not None and os.path.exists(filePath):
        playsound(filePath)

while True:
    try:
        timeHour, timeMinute, fileType, filePath= getData()
    except NameError:
        print ("Server Error:", NameError)
    now = datetime.datetime.now()
    nowhour = now.hour.__int__()
    nowminute = now.minute.__int__()
    nowsecond = now.second.__int__()
    print timeHour
    print timeMinute
    print fileType
    if nowhour == timeHour and nowminute == timeMinute and second <= nowsecond <= second +5 :
        print ("den gio")
        playFile(filePath)
    time.sleep(5)
















