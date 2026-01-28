from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self):
        self.driver.find_element(By.ID, "first-name").send_keys("Татьяна")
        self.driver.find_element(By.ID, "last-name").send_keys("Абрамова")
        self.driver.find_element(By.ID, "postal-code").send_keys("618200")
        self.driver.find_element(By.ID, "continue").click()

    def total_price(self):
        total = self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))).text

        return total
