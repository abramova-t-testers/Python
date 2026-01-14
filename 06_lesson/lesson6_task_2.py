from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")

txt_input = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
txt_input.send_keys("SkyPro")

WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element_value((By.ID, "newButtonName"), "SkyPro"))

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

element = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
print(element.text)

driver.quit()
