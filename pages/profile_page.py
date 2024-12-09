import time
from .base_page import BasePage
from .locators import MainPageLockators
from .locators import ProfilePageLockators

class ProfilePage(BasePage):
    def go_to_profile_page(self):
        login_link = self.browser.find_element(*MainPageLockators.LOGIN_LINK)
        login_link.click()

    def edit_profile(self):
        edit_button = self.browser.find_element(*ProfilePageLockators.EDIT)
        edit_button.click()
        input_age = self.browser.find_element(*ProfilePageLockators.AGE)
        input_age.clear()
        input_age.send_keys("7")
        save_button = self.browser.find_element(*ProfilePageLockators.SAVE_BUTTON)
        save_button.click()

    def change_photo(self):
        change_photo = self.browser.find_element(*ProfilePageLockators.CHANGE_PHOTO).click()
        change_photo.send_keys("")
        time.sleep(3)
        save_button = self.browser.find_element(*ProfilePageLockators.SAVE_BUTTON).click()

    def delete_pet(self):
        delete_pet = self.browser.find_element(*ProfilePageLockators.DELETE_PET).click()
        time.sleep(3)
        delete_pet_yes = self.browser.find_element(*ProfilePageLockators.CONFIRM_DELETE_YES).click()
        delete_pet_no = self.browser.find_element(*ProfilePageLockators.CONFIRM_DELETE_NO).click()