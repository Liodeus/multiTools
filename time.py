#!/usr/bin/env Python
# -*- coding:utf_8 -*-

import time
import calendar


def temps():
    localtime = time.localtime(time.time())

    if localtime[6] == "1":
        contraction = str(localtime[6]) + "st"
    elif localtime[6] == "2":
        contraction = str(localtime[6]) + "nd"
    elif localtime[6] == "3":
        contraction = str(localtime[6]) + "nd"
    else:
        contraction = str(localtime[6]) + "st"

    print("We're the", contraction, "day of the week.")
    print("Day since 1st january : ", localtime[7])

    localtime = time.asctime(time.localtime(time.time()))
    print ("Local current time :", localtime)


def calendarOfTheMonth():
    localtime = time.localtime(time.time())

    year = int(localtime[0])
    month = int(localtime[1])

    print(calendar.month(year, month))


def calendarOfTheYear():
    print(calendar.calendar(2017))


def epoch():
    ticks = time.time()
    print("Number of ticks since 12:00am, January 1, 1970:", ticks)


temps()
