import pytest
from selenium import webdriver
from CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_cal_page(driver):
    cal_page = CalculatorPage(driver)
    cal_page.open()
    cal_page.fill_field()
    cal_page.button()
    cal_page.result_cal()
    result = cal_page.result_cal()
    assert result == "15"
