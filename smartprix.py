from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('C:/Users/mihir/Desktop/chromedriver.exe')
driver = webdriver.Chrome(service = s)
time.sleep(0.5)

driver.get('https://www.smartprix.com/mobiles')
time.sleep(1)

exclude_out_of_stock = driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input')
exclude_out_of_stock.click()
time.sleep(1)

exclude_upcoming = driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input')
exclude_upcoming.click()
time.sleep(1)

old_height = driver.execute_script('return document.body.scrollHeight')
while True:
    load_more = driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]')
    load_more.click()
    time.sleep(1)

    new_height = driver.execute_script('return document.body.scrollHeight')

    if new_height == old_height:
        break
    old_height = new_height

# copy all HTML source code of all scrolled or loaded pages
html = driver.page_source

# writing above code in a file
with open('smartprix.html','w',encoding='utf-8') as f:
    f.write(html)

time.sleep(5)