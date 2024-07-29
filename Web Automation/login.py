from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('https://technologychannel.github.io/SampleWebsite/')
username = browser.find_element(by=By.NAME,value="username")
time.sleep(2)
username.send_keys("rajat@gmail.com"+ Keys.RETURN)
password = browser.find_element(by=By.NAME,value="password")
password.send_keys("12345666"+ Keys.RETURN)
time.sleep(2)

button = browser.find_element(by=By.TAG_NAME("button"))
button.click()
# Write a Automation Script that open technologychannel.org

# Open amazon.com search for The Lean Startup and show first result on screen.
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

