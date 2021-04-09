from selenium.webdriver.common.by import By
from ui.locators.dashboard_locators import DashBoardLocators


class CampaignNewLocators(DashBoardLocators):

    TRAFFIC_BUTTON = (By.XPATH, "//div[@class='column-list-item _traffic']")
    LINK_FIELD = (By.XPATH, "//input[@placeholder='Введите ссылку']")
    NAME_COMPANY_FIELD =(By.XPATH, "//input[@class='input__inp js-form-element']")
    CLEAR_COMPANY_FIELD = (By.XPATH, "//div[@class='input__clear js-input-clear']")

    TEASER_BUTTON = (By.XPATH, "//div[@id='patterns_57_58']")
    HEADER_FIELD = (By.XPATH, "//input[@placeholder='Введите заголовок объявления']")
    DESCRIPTION_FIELD = (By.XPATH, "//textarea[@placeholder='Введите текст объявления']")
    CREATE_COMPANY_BUTTON = (By.XPATH, "//div[contains(text(), 'Создать кампанию')]")
    ADD_IMG_BUTTON = (By.XPATH, "//input[@type='file']")
    SAVE_IMG = (By.XPATH, "//input[@value='Сохранить изображение']")

    DELETE_IMG = (By.XPATH, "//div[contains(text(), 'Удалить все')]")
    APPLY_DELETE = (By.XPATH, "//div[contains(text(), 'Да, удалить')]")