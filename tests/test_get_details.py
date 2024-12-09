from selenium.webdriver.common.by import By
from pages.main_page import MainPage


def test_get_details(browser):
    link = "http://34.141.58.52:8080/#/"
    page = MainPage(browser, link)
    page.open()
    page.get_details()
    browser.save_screenshot("result8.png")
    assert "Pet picture:" in browser.find_element(By.CSS_SELECTOR, 'div#app > main > div > div > div > div > div').text