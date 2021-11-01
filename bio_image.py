import matplotlib.pyplot as plt
from math import sin, pi
from datetime import datetime


currntDay = str(datetime.date(datetime.now()))
currntDay = list(map(int,currntDay.split("-")))

def leapYear(year=currntDay[2]):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def daysFromBirthday(birthDay):
    days = 0

    if leapYear():
        months = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        months = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    for i in range(birthDay[0], currntDay[0]):
        if leapYear(i):
            days += 366
        else:
            days += 365


    if currntDay[1] > birthDay[1] or (currntDay[1] == birthDay[1] and currntDay[2] > birthDay[2]):
        for i in range(birthDay[1], currntDay[1]):
            days += months[i-1]

    
        if currntDay[2] < birthDay[2]:
            days -=  (birthDay[2] - currntDay[2])
        else:
            days += months[currntDay[1]] + (birthDay[2] - currntDay[2])

    else:
        counter = 0
        for i in range(currntDay[1], birthDay[1]):
            counter += months[i-1]

        if currntDay[2] < birthDay[2]:
            counter -= (currntDay[2] - birthDay[2])
        else:
            counter -= (currntDay[2] - birthDay[2])

        days -= counter

    return days-1

def createImage(date, name):
    plt.clf()
    
    date = list(map(int,date.split(".")))
    x = []
    emotional = []
    intellectual = []
    physical = []

    for i in range(daysFromBirthday(date),daysFromBirthday(date)+7):
        emotional.append(sin(2*pi*i/23)*100)
        intellectual.append(sin(2*pi*i/28)*100)
        physical.append(sin(2*pi*i/33)*100)
        a = i-daysFromBirthday(date)
        x.append(a)

    plt.ylim([-100,100])
    plt.xlabel('One week forecast (started from today)')
    plt.ylabel('Percentage')

    plt.plot(x, emotional, color="red", label="Emotional")
    plt.plot(x, intellectual, color="green", label="Intellectual")
    plt.plot(x, physical, color="blue", label="Physical")

    plt.legend();

    plt.savefig(name)
