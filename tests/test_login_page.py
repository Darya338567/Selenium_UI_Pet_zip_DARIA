from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


def test_go_to_login(browser):
    link = "http://34.141.58.52:8080/#/login"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    browser.save_screenshot("result6.png")
    text = browser.find_element(By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]')
    assert "Rona" in text.text

