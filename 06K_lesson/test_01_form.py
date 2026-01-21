from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    service = Service(service_args=["--verbose"])
    driver = webdriver.Edge(service=service)

    wait = WebDriverWait(driver, 10)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    first_name = driver.find_element(By.NAME, "first-name")
    first_name.send_keys("Иван")

    wait.until(EC.text_to_be_present_in_element_value(
        (By.NAME, "first-name"), "Иван"))

    last_name = driver.find_element(By.NAME, "last-name")
    last_name.send_keys("Петров")

    wait.until(EC.text_to_be_present_in_element_value(
        (By.NAME, "last-name"), "Петров"))

    address = driver.find_element(By.NAME, "address")
    address.send_keys("Ленина, 55-3")

    wait.until(EC.text_to_be_present_in_element_value(
        (By.NAME, "address"), "Ленина, 55-3"))

    email = driver.find_element(By.NAME, "e-mail")
    email.send_keys("test@skypro.com")

    wait.until(EC.text_to_be_present_in_element_value(
        (By.NAME, "e-mail"), "test@skypro.com"))

    phone = driver.find_element(By.NAME, "phone")
    phone.send_keys("+7985899998787")

    wait.until(EC.text_to_be_present_in_element_value(
        (By.NAME, "phone"), "+7985899998787"))

    city = driver.find_element(By.NAME, "city")
    city.send_keys("Москва")

    wait.until(EC.text_to_be_present_in_element_value(
        (By.NAME, "city"), "Москва"))

    country = driver.find_element(By.NAME, "country")
    country.send_keys("Россия")

    wait.until(EC.text_to_be_present_in_element_value(
        (By.NAME, "country"), "Россия"))

    job_position = driver.find_element(By.NAME, "job-position")
    job_position.send_keys("QA")

    wait.until(EC.text_to_be_present_in_element_value(
        (By.NAME, "job-position"), "QA"))

    company = driver.find_element(By.NAME, "company")
    company.send_keys("SkyPro")

    wait.until(EC.text_to_be_present_in_element_value(
        (By.NAME, "company"), "SkyPro"))

    driver.find_element(By.CLASS_NAME, "btn").click()

    zip_code = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
    background_color = zip_code.value_of_css_property("background-color")
    assert background_color == "rgba(248, 215, 218, 1)"

    fields = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company"
    ]

    for field in fields:
        element = wait.until(EC.presence_of_element_located((By.ID, field)))
        color = element.value_of_css_property("background-color")
        assert color == "rgba(209, 231, 221, 1)"

    driver.quit()
