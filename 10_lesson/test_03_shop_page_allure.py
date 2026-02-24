import pytest
from selenium import webdriver
from AuthorizationPageAllure import AuthorizationPage
from MainShopPageAllure import MainShopPage
from CartPageAllure import CartPage
from OrderPageAllure import OrderPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера
    """
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Тестирование интернет-магазина")
@allure.description("Тест проверяет корректную работу: авторизацию, "
                    "добавление товаров в корзину и переход в нее, содержимое "
                    "корзины, нажатие кнопки Checkout, оформление заказа "
                    "и проверку итоговой стоимости")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_page(driver):
    """
    Тест проверяет работу интернет-магазина при оформлении заказа
    :param driver: WebDriver — объект драйвера, переданный фикстурой
    """
    auth_page = AuthorizationPage(driver)
    with allure.step("Открытие страницы интернет-магазина"):
        auth_page.open()
    with allure.step("Авторизация пользователя"):
        auth_page.authorization()

    main_page = MainShopPage(driver)
    with allure.step("Добавление товаров в корзину и переход в неё"):
        main_page.main_page()

    cart_page = CartPage(driver)
    with allure.step("Получение списка товаров в корзине "
                     "с названиями и ценами"):
        cart_page.get_cart_items()
    with allure.step("Ожидаемый список товаров в корзине "
                     "с названиями и ценами"):
        expected_items = [
            {'name': 'Sauce Labs Backpack', 'price': '$29.99'},
            {'name': 'Sauce Labs Bolt T-Shirt', 'price': '$15.99'},
            {'name': 'Sauce Labs Onesie', 'price': '$7.99'}
        ]
    with allure.step("Проверка соответствия содержимого корзины ожидаемому"):
        cart_page.should_have_items(expected_items)
        assert cart_page.should_have_items(expected_items), f"Товары в корзине не соответствуют ожидаемым: {expected_items}"
    with allure.step("Инициация процесса оформления заказа"):
        cart_page.checkout()

    order_page = OrderPage(driver)
    with allure.step("Заполнение формы персональными данными"):
        order_page.fill_form()
    with allure.step("Получение итоговой суммы заказа"):
        order_page.total_price()
        total = order_page.total_price()
    with allure.step("Проверка итоговой суммы заказа"):
        assert total == "Total: $58.29"
