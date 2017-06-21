#!/usr/bin/env Python
# -*- coding:utf_8 -*-

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re

from selenium import webdriver


# If this doesn't work you need to install geckodriver
# https://github.com/mozilla/geckodriver
def weather():
    browser = webdriver.Firefox()
    browser.get('https://www.tameteo.com/')


if __name__ == "__main__":
    weather()
