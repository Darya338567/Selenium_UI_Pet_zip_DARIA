from selenium.webdriver.common.by import By

from pages.main_page import MainPage


def test_drop_down(browser):
    link = "http://34.141.58.52:8080/#/"
    page = MainPage(browser, link)
    page.open()
    page.drop_down()
    browser.save_screenshot("result5.png")
    assert "Cat" in browser.find_element(By.CSS_SELECTOR, 'span#typesSelector').text.text
