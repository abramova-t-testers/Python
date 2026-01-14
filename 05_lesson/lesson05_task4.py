from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get("http://the-internet.herokuapp.com/login")
sleep(5)

input_Username = driver.find_element(By.CSS_SELECTOR, "#username")
input_Username.send_keys("tomsmith")
sleep(5)

input_Password = driver.find_element(By.CSS_SELECTOR, "#password")
input_Password.send_keys("SuperSecretPassword!")
sleep(5)

driver.find_element(By.CLASS_NAME, "radius").click()
sleep(3)

print(driver.find_element(By.CSS_SELECTOR, "#flash").text)

driver.quit()
sleep(5)
