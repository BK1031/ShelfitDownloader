import webbrowser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import requests
import keyboard
import urllib
import time
from secret import password

bookID = 87272

startPage = 1
lastPage = 274

currPage = startPage

loginUrl = "https://dashboard.shelfit.com"
baseUrl = "https://reader.shelfit.com/active_textbooks/"

# driver = webdriver.Chrome(r'/Users/bharat/chromedriver')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_window_size(700, 1200)

driver.get(loginUrl)
elem = driver.find_element_by_id("username")
elem.send_keys("bharat.kathi@warriorlife.net")
elem = driver.find_element_by_id("password")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)

time.sleep(0.5)
driver.get("https://dashboard.shelfit.com/site/go-to-reader")

time.sleep(0.5)
driver.get("https://reader.shelfit.com/active_textbooks/" + str(bookID))
time.sleep(0.5)

while currPage <= lastPage:
    driver.get(baseUrl + str(bookID) + "/pg" + str(currPage) + "/large.jpg")
    driver.save_screenshot(str(currPage) + '.png')
    print("Downloaded Page " + str(currPage))
    currPage += 1