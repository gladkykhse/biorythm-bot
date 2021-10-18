import matplotlib.pyplot as plt
from math import sin, pi
from datetime import datetime

def daysFromBirthday(birthDay):
    currntDay = str(datetime.date(datetime.now()))
    currntDay = list(map(int,currntDay.split("-")))
    birthDay = list(map(int,birthDay.split(".")))

    days = 0

    currentYear = currntDay[2]
    leap = False

    if currentYear % 4 == 0:
        if currentYear % 100 == 0:
            if currentYear % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
            
    if leap:
        months = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        months = [31,28,31,30,31,30,31,31,30,31,30,31]

    
    for i in range(birthDay[0], currntDay[0]):
        if i % 4 == 0:
            if i % 100 == 0:
                if i % 400 == 0:
                    days += 366
                else:
                    days += 365
            else:
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

x = []
y1 = []
y2 = []
y3 = []

birthDay = "2004.12.1"

for i in range(daysFromBirthday(birthDay),daysFromBirthday(birthDay)+7):
    y1.append(sin(2*pi*i/23)*100)
    y2.append(sin(2*pi*i/28)*100)
    y3.append(sin(2*pi*i/33)*100)
    x.append(i)

plt.plot(x, y1, color="red")
plt.plot(x, y2, color="green")
plt.plot(x, y3, color="blue")

plt.show()