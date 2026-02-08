import pytest
from selenium import webdriver
from AuthorizationPage import AuthorizationPage
from MainShopPage import MainShopPage
from CartPage import CartPage
from OrderPage import OrderPage


@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_page(driver):
    auth_page = AuthorizationPage(driver)
    auth_page.open()
    auth_page.authorization()

    main_page = MainShopPage(driver)
    main_page.main_page()

    cart_page = CartPage(driver)
    cart_page.get_cart_items()
    expected_items = [
        {'name': 'Sauce Labs Backpack', 'price': '$29.99'},
        {'name': 'Sauce Labs Bolt T-Shirt', 'price': '$15.99'},
        {'name': 'Sauce Labs Onesie', 'price': '$7.99'}
    ]
    cart_page.should_have_items(expected_items)
    assert cart_page.should_have_items(expected_items), f"Товары в корзине не соответствуют ожидаемым: {expected_items}"
    cart_page.checkout()

    order_page = OrderPage(driver)
    order_page.fill_form()
    order_page.total_price()
    total = order_page.total_price()
    assert total == "Total: $58.29"
