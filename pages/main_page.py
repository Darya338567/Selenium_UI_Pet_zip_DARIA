import time

from .base_page import BasePage
from .locators import MainPageLockators

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLockators.LOGIN_LINK)
        login_link.click()

    def drop_down(self):
        drop = self.browser.find_element(*MainPageLockators.DROP_DOWN)
        drop.click()
        down = self.browser.find_element(*MainPageLockators.ITEM_OF_DROP_DOWN)
        down.click()

    def filter_neg(self):
        input_filter = self.browser.find_element(*MainPageLockators.INPUT)
        input_filter.clear()
        input_filter.send_keys("Dobick")
        empty_click = self.browser.find_element(*MainPageLockators.EMPTY_PLACE)
        empty_click.click()

    def filter_poz(self):
        input_filter = self.browser.find_element(*MainPageLockators.INPUT)
        input_filter.send_keys("Kuza")
        empty_click = self.browser.find_element(*MainPageLockators.EMPTY_PLACE)
        empty_click.click()

    def get_details(self):
        self.browser.find_element(*MainPageLockators.DETAILS).click()

