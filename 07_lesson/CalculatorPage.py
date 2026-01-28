from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 49)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def fill_field(self):
        field = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        field.clear()
        field.send_keys("45")

    def button(self):
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

    def result_cal(self):
        self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
        result = self.driver.find_element(By.CLASS_NAME, "screen").text

        return result
