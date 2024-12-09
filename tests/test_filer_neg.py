from selenium.webdriver.common.by import By
from pages.main_page import MainPage


def test_filter_negative(browser):
    link = "http://34.141.58.52:8080/#/"
    page = MainPage(browser, link)
    page.open()
    page.filter_neg()
    browser.save_screenshot("result7.png")
    assert "No records found." in browser.find_element(By.CSS_SELECTOR, 'div#app > main > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div').text
