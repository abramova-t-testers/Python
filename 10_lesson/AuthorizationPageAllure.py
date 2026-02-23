from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class AuthorizationPage:
    def __init__(self, driver):
        """
        Конструктор класса AuthorizationPage
        :param driver: WebDriver — объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы интернет-магазина")
    def open(self):
        """
        Открывает страницу интернет-магазина
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Авторизация пользователя")
    def authorization(self):
        """
        Выполняет авторизацию пользователя с предустановленными данными
        """
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
