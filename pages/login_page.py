from pages.base_page import BasePage
from pages.locators import LoginPageLockators


class LoginPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLockators.LOGIN_EMAIL)
        login_email.send_keys("diva.86@inbox.ru")
        login_password = self.browser.find_element(*LoginPageLockators.LOGIN_PASS)
        login_password.send_keys("Sd338567")
        login_button = self.browser.find_element(*LoginPageLockators.LOGIN_BTN)
        login_button.click()
