#!usr/bin/env Python
# -*- coding:utf_8 -*-

import sys
import temps
import ip
import weather


def main():
    print("1. Time")
    print("2. Ip")
    print("3. Weather \n")

    choice = input("Choice : ")
    print()

    if choice == "1":
        print("1. Time")
        print("2. Calendar of the month")
        print("3. Calendar of the year")
        print("4. Epoch \n")

        scdChoice = input("Choice : ")
        print()

        if scdChoice == "1":
            temps.temps()
        elif scdChoice == "2":
            temps.calendarOfTheMonth()
        elif scdChoice == "3":
            temps.calendarOfTheYear()
        elif scdChoice == "4":
            temps.epoch()
        else:
            print("Error !")

    elif choice == "2":
        ip.ipInfo()

    elif choice == "3":
        weather.weather()

    else:
        print("Error !")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
        sys.exit(0)
