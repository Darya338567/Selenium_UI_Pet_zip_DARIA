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
    page.go_to_login()
    page.go_to_profile_page()
    page.edit_profile
    assert "7" in browser.find_element(By.XPATH, '//*[@id="age"]/input[1]').txt

