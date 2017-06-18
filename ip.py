#!/usr/bin/env Python3
# -*- coding:utf_8 -*-

# recuperer sur internet
# recuperer via subprocess

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re


uClient = uReq("http://www.ip-tracker.org/")
pageSoup = soup(uClient, "html.parser")
ip = pageSoup.find_all("td", {"class":"tracking"})

regex = re.compile("([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})")

result = re.search(regex, str(ip[0]))

print(result.groups())

ip.pop(0)

liste = []

for t in ip:
	liste.append(re.sub('<[^>]*>', "", str(t)).strip())

liste.pop(13)
liste.pop(12)
liste.pop(11)
liste.pop(10)
liste.pop(8)
liste.pop(2)
liste.pop(1)
liste.pop(0)

i = 0
for tt in liste:
	print(i, ":", tt)
	i+=1