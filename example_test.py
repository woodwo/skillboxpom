import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="module", autouse=True)
def driver():
    # Instantiate the WebDriver (in this case, using Chrome)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    # Close the WebDriver
    driver.quit()


@pytest.fixture(scope="module", autouse=True)
def login(driver):
    # Navigate to the webpage
    driver.get("http://pizzeria.skillbox.cc/")

    # Add the cookies to the local storage
    cookies = [
        {
            "name": "wordpress_608a4400240853029106aa1f2d8f9149",
            "value": "ujg51121%7C1685187738%7CPGd6PYK1Pwp3F4Bt6JNeNY8vHRpfaDBCm1p9IH2KQbe%7C0df96684db76d1615d06d00ed398521e64b8f35081cbf5847634334e7efb543d",
            "domain": "pizzeria.skillbox.cc",
        },
        {
            "name": "wordpress_logged_in_608a4400240853029106aa1f2d8f9149",
            "value": "ujg51121%7C1685187738%7CPGd6PYK1Pwp3F4Bt6JNeNY8vHRpfaDBCm1p9IH2KQbe%7C0df96684db76d1615d06d00ed398521e64b8f35081cbf5847634334e7efb543d",
            "domain": "pizzeria.skillbox.cc",
        },
    ]
    for cookie in cookies:
        driver.add_cookie(cookie)
    time.sleep(5)


def test_checkout_button(driver):
    # arrange
    driver.get("http://pizzeria.skillbox.cc/cart/")
    button = driver.find_element(By.CLASS_NAME, "checkout-button.button.alt.wc-forward")

    # act
    button.click()

    # assert
    assert driver.current_url == "http://pizzeria.skillbox.cc/checkout/"
