from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("http://the-internet.herokuapp.com/inputs")
sleep(5)

input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("Sky")
sleep(5)

input_field.clear()
sleep(5)

input_field.send_keys("Pro")
sleep(5)

driver.quit()
sleep(5)
