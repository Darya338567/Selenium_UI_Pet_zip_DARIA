import time
from .base_page import BasePage
from .locators import CreatePetLockators


class CreatePet(BasePage):
    def create_pet(self):
        input_name = self.browser.find_element(*CreatePetLockators.INPUT_NAME)
        input_name.send_keys("Lusya")
        type_pet = self.browser.find_element(*CreatePetLockators.TYPE)
        type_pet.click()
        type_dog = self.browser.find_element(*CreatePetLockators.TYPE_DOG)
        type_dog.click()
        time.sleep(2)
        save_create = self.browser.find_element(*CreatePetLockators.SAVE_CREATE)
        save_create.submit()
        choose_photo = self.browser.find_element(*CreatePetLockators.CHOOSE)
        choose_photo.click()
        choose_photo.send_keys('4248c241ad1d3bd162eb58edb100ed97.jpg')
        time.sleep(3)
        submit_photo = self.browser.find_element(*CreatePetLockators.CHOOSE_SUBMIT)
        submit_photo.submit()

