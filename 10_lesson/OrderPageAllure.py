from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class OrderPage:
    def __init__(self, driver):
        """
        Конструктор класса OrderPage
        :param driver: WebDriver — объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполнение формы персональными данными")
    def fill_form(self):
        """
        Заполняет форму данными (имя, фамилия, почтовый индекс)
        и переходит на итоговую страницу
        """
        self.driver.find_element(By.ID, "first-name").send_keys("Татьяна")
        self.driver.find_element(By.ID, "last-name").send_keys("Абрамова")
        self.driver.find_element(By.ID, "postal-code").send_keys("618200")
        self.driver.find_element(By.ID, "continue").click()

    @allure.step("Получение итоговой суммы заказа")
    def total_price(self) -> str:
        """
        Получает итоговую сумму заказа, отображаемую на странице
        :return: 'Total' (str) - итоговая стоимость
        (в формате строки, например, '$58.29').
        """
        total = self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))).text

        return total
