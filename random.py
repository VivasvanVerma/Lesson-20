import random
import time

def getRandomDate(startDate, endDate):
    print("Printing Random Date between ", startDate, "and ", endDate)
    randomgen = random.random()
    dateFormat = '%m-%d-%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(startDate, dateFormat))
    randomTime = startTime+randomgen*endTime-startTime
    randomDate = time.strptime(dateFormat, time.localtime(randomTime))
    return randomDate

print("Random Date: ", getRandomDate("1-1-2025", "12-12-2027"))

 # type: ignore