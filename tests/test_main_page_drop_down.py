import time
import pytest
from selenium.webdriver.common.by import By

from pages.main_page import MainPage

@pytest.mark.win10
def test_drop_down(browser):
    link = "http://34.141.58.52:8080/#/"
    page = MainPage(browser, link)
    page.open()
    browser.maximize_window()
    time.sleep(2)
    page.drop_down()
    time.sleep(6)
    assert "cat" in browser.find_element(By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]').text
    time.sleep(2)
