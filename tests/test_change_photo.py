import time
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePageLockators


def test_profile_edit(browser):
    link = "http://34.141.58.52:8080/#/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

    link = "http://34.141.58.52:8080/#/login"
    page = LoginPage(browser,link)
    page.go_to_login()
    time.sleep(3)

    link = "http://34.141.58.52:8080/#/profile"
    page = ProfilePage(browser,link)
    page.edit_profile()
    page.change_photo()
    assert "Thank you" in browser.find_element(By.XPATH, 'body/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]').txt