from selenium.webdriver.common.by import By


class MainPageLockators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#app > header > div > ul > li > a")
    DROP_DOWN = (By.XPATH, '//*[@id="typesSelector"]')
    ITEM_OF_DROP_DOWN = (By.XPATH, '//*[@id="pv_id_2_1"]')
    TEXT_DD = (By.CSS_SELECTOR, "span#typesSelector")
    INPUT = (By.XPATH, '//*[@id="petName"]')
    NO_ITEM = (By.CSS_SELECTOR, "div#app > main > div > div:nth-of-type(2) > div:nth-of-type(2) > div > div > div")
    KUZA = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]')
    EMPTY_PLACE = (By.XPATH, '//*[@id="app"]')
    DETAILS = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]')

class LoginPageLockators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")

class ProfilePageLockators:
    EDIT = (By.XPATH,'//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[1]')
    DELETE_PET = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/button[2]')
    DELETE_PET_YES = (By.XPATH, 'body/div[3]/div[2]/button[2]')
    DELETE_PET_NO = (By.CSS_SELECTOR, 'html > body > div:nth-of-type(3) > div:nth-of-type(2) > button')
    ADD_PET = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]')

class EditPageLockators:
    INPUT_PAGE = (By.XPATH, '//*[@id="age"]/input[1]')
    BUTTON_CHANGE_PHOTO = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]')
    BUTTON_SAVE_CHANGES = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/form[1]/div[1]/div[2]/div[3]/button[1]')
    AGE = (By.CSS_SELECTOR, 'span#age > input')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'div#app > main > div > form > div > div:nth-of-type(2) > div:nth-of-type(3) > button')
    CHANGE_PHOTO = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/form[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]')

class CreatePetLockators:
    INPUT_NAME = (By.XPATH, '//*[@id="name"]')
    TYPE = (By.XPATH, '//*[@id="typeSelector"]')
    TYPE_DOG = (By.XPATH, '//*[@id="pv_id_28_2"]')
    SAVE_CREATE = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[3]/button[1]')
    CHOOSE = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span[1]')
    CHOOSE_SUBMIT = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span[1]')

class CreatePhoto:
    CHOOSE = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span[1]')
    CHOOSE_SUBMIT = (By.XPATH, '//*[@id="app"]/main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span[1]')