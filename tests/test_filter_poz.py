from selenium.webdriver.common.by import By
from pages.main_page import MainPage


def test_filter_negative(browser):
    link = "http://34.141.58.52:8080/#/"
    page = MainPage(browser, link)
    page.open()
    page.filter_poz()
    browser.save_screenshot("result8.png")
    assert "Kuza" in browser.find_element(By.CSS_SELECTOR, 'div#app > main > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div > div:nth-of-type(2) > div').text.text
