#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:37:53 2019

@author: lordxuzhiyu
"""

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome('/Users/lordxuzhiyu/Desktop/chromedriver')

chrome_options = Options()
chrome_options.add_argument("--headless")

driver.get("https://www.cityrealty.com/")
driver.find_element_by_id("welcome-autocomplete").click()
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Where in NYC?'])[1]/following::span[2]").click()
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='View Full Listing Info'])[1]/following::span[2]").click()
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Description'])[1]/following::span[2]").click()
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='>'])[1]/following::a[1]").click()
driver.find_element_by_link_text("Roosevelt Island").click()

html = driver.page_source