from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s = Service('C:/Users/mihir/Desktop/chromedriver.exe')
driver = webdriver.Chrome(service = s)

# PAGINATION - Infinite Scrolling, I have to fetch whole HTML of the webpage by doing infinite scrolling up-to the end & saving that HTML.

# open Ajio website
driver.get('https://www.ajio.com/men-backpacks/c/830201001')
time.sleep(2)

# tell current window (1st page) height in Pixels
old_height = driver.execute_script('return document.body.scrollHeight')  # --> 9000 pixels

# running infinite loop for infinite scrolling
while True:
    # using 'driver' I can use JavaScript code to scroll page
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')  # --> 0 pixels to 9000 pixels & 9000 more pixels got generated.
    time.sleep(3)

    new_height = driver.execute_script('return document.body.scrollHeight')  # --> 18000 pixels

    if new_height == old_height:
        break

    old_height = new_height

# copy all HTML source code of all scrolled or loaded pages
html = driver.page_source

# writing above code in a file
with open('ajio.html','w',encoding='utf-8') as f:
    f.write(html)

# After doing above code I can use BeautifulSoup library to scrap data.

