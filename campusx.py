# OUR TASK
# Automatic open Google.com
# Search campusx
# learnwith.campusx.in
# dsmp login page

import time
# Import Selenium 'webdriver' method
from selenium import webdriver
# Import Selenium 'Service' class
from selenium.webdriver.chrome.service import Service
# Import 'By' class
from selenium.webdriver.common.by import By
# Import 'Keys' method, so that we can press any Key of computer.
from selenium.webdriver.common.keys import Keys

# Create a Service which is using 'chromedriver'.
# define an object of 'Service' class & pass path of 'chromedriver'.
# convert every backward slash into forward slash.
s = Service("C:/Users/mihir/Desktop/chromedriver.exe")

# Passing Service to below code
# to open new Chrome window automatically, pass 'chromedriver' as a service
driver = webdriver.Chrome(service = s)

# to open any URL
driver.get('http://google.com')
time.sleep(1.5)

# fetch the 'search input box' of google using xpath which is found using inspect.
user_input = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
# below code is used to write something on Google 'search input box'
user_input.send_keys('Campusx')
time.sleep(1)

# now I want to press enter use 'Keys' method.
user_input.send_keys(Keys.ENTER)
time.sleep(1)

# code which automatically find 'learnwith.campusx.in' link.
link = driver.find_element(by=By.XPATH,value='//*[@id="rso"]/div[2]/div/div/div[1]/div/div/div[1]/div/a')
# to click above link
link.click()
time.sleep(1)

# code which automatically find 'login'.
link2 = driver.find_element(by=By.XPATH,value='/html/body/div[1]/header/section[2]/a[5]')
link2.click()
time.sleep(200)