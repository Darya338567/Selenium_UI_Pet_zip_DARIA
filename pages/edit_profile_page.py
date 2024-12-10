import time
from .base_page import BasePage
from .locators import EditPageLockators


class EditProfilePage(BasePage):
    def change_age(self):
        input_age = self.browser.find_element(*EditPageLockators.AGE)
        input_age.clear()
        time.sleep(2)
        input_age.send_keys("7")
        time.sleep(2)
        save_button = self.browser.find_element(*EditPageLockators.SAVE_BUTTON)
        save_button.click()

    def change_photo(self):
        change_photo = self.browser.find_element(*EditPageLockators.CHANGE_PHOTO).click()
        change_photo.send_keys('tests/4248c241ad1d3bd162eb58edb100ed97.jpg')
        time.sleep(3)
        save_button = self.browser.find_element(*EditPageLockators.SAVE_BUTTON).click()
