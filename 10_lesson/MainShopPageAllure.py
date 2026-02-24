from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainShopPage:
    def __init__(self, driver):
        """
        Конструктор класса MainShopPage
        :param driver: WebDriver — объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавление товаров в корзину и переход в неё")
    def main_page(self):
        """
        Выполняет добавление трёх товаров в корзину и переход в корзину
        """
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-onesie"))).click()

        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
