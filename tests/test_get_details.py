import time
import pytest
from selenium.webdriver.common.by import By
from pages.main_page import MainPage

@pytest.mark.regression
def test_get_details(browser):
    link = "http://34.141.58.52:8080/#/"
    page = MainPage(browser, link)
    page.open()
    browser.maximize_window()
    time.sleep(3)
    page.get_details()
    time.sleep(2)
    assert "Pet picture:" in browser.find_element(By.CSS_SELECTOR, 'div#app > main > div > div > div > div > div').text