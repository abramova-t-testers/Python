from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class CartPage:
    def __init__(self, driver):
        """
        Конструктор класса CartPage
        :param driver: WebDriver — объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Получение списка товаров в корзине с названиями и ценами")
    def get_cart_items(self) -> list:
        """
        Получает список товаров в корзине, включая их названия и цены
        :return: Список словарей, каждый из которых содержит:
            - 'name' (str): название товара;
            - 'price' (str): цена товара
        (в формате строки, например, '$29.99').
        """
        items = []
        cart_item_elements = self.driver.find_elements(
            By.CLASS_NAME, 'cart_item_label')
        for item in cart_item_elements:
            name = item.find_element(By.CLASS_NAME, 'inventory_item_name').text
            price = item.find_element(
                By.CLASS_NAME, 'inventory_item_price').text
            items.append({'name': name, 'price': price})

        return items

    @allure.step("Проверка соответствия содержимого корзины ожидаемому")
    def should_have_items(self, expected: list) -> bool:
        """
        Верифицирует, что в корзине находятся ожидаемые товары
        :param expected: ожидаемый список
        """
        actual = self.get_cart_items()
        return actual == expected

    @allure.step("Инициация процесса оформления заказа")
    def checkout(self):
        """
        Нажимает кнопку Checkout для перехода к оформлению заказа
        """
        self.driver.find_element(By.ID, "checkout").click()
