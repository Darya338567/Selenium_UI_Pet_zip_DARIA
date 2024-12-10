import time
from .base_page import BasePage
from .locators import ProfilePageLockators


class ProfilePage(BasePage):
    def go_to_edit_pet(self):
        edit_button = self.browser.find_element(*ProfilePageLockators.EDIT)
        edit_button.click()

    def delete_pet(self):
        delete_pet = self.browser.find_element(*ProfilePageLockators.DELETE_PET)
        delete_pet.click()
        time.sleep(3)

    def delete_pet_no(self):
        delete_pet_no = self.browser.find_element(*ProfilePageLockators.DELETE_PET_NO).click()
        delete_pet_no.submit()

    def delete_pet_yes(self):
        delete_pet_yes = self.browser.find_element(*ProfilePageLockators.DELETE_PET_YES)
        delete_pet_yes.submit()

    def add_pet(self):
        add_pet = self.browser.find_element(*ProfilePageLockators.ADD_PET)
        add_pet.click()