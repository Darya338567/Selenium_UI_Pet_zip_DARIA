import time

import pytest
from selenium.webdriver.common.by import By
from pages.edit_profile_page import EditProfilePage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage

@pytest.mark.win10
def test_profile_edit_age(browser):
    link = "http://34.141.58.52:8080/#/"
    page = MainPage(browser, link)
    page.open()
    browser.maximize_window()
    page.go_to_login_page()
    time.sleep(2)

    link_1 = "http://34.141.58.52:8080/#/login"
    page_1 = LoginPage(browser, link_1)
    page_1.go_to_login()
    time.sleep(2)

    link_2 = "http://34.141.58.52:8080/#/profile"
    page_2 = ProfilePage(browser, link_2)
    page_2.go_to_edit_pet()
    time.sleep(2)

    link_3 = "http://34.141.58.52:8080/#/pet-edit/32235"
    page_3 = EditProfilePage(browser, link_3)
    page_3.change_age()
    time.sleep(4)
    assert "Thank you!" in browser.find_element(By.XPATH, 'body/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]').text

