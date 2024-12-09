from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePageLockators

def test_delete_pet(browser):
    link = "http://34.141.58.52:8080/#/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.go_to_login()
    page.delete_pet()
    page.delete_pet_no()
    page.delete_pet()
    page.delete_pet_yes()
    assert "Thank you" in browser.find_element(By.XPATH, 'body/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]').txt