from selenium.webdriver.common.by import By
from ui.locators.dashboard_locators import DashBoardLocators


class CampaignNewLocators(DashBoardLocators):

    TRAFFIC_BUTTON = (By.XPATH, "//div[@class='column-list-item _traffic']")
    LINK_FIELD = (By.XPATH, "//input[@placeholder='Введите ссылку']")
    CLEAR_COMPANY_FIELD = (By.XPATH, "//div[@class='input__clear js-input-clear']")
    NAME_COMPANY_FIELD = (By.XPATH, "//div[@class='input input_campaign-name input_with-close']//input")

    TEASER_BUTTON = (By.XPATH, "//div[@id='patterns_57_58']")
    HEADER_FIELD = (By.XPATH, "//input[@placeholder='Введите заголовок объявления']")
    DESCRIPTION_FIELD = (By.XPATH, "//textarea[@placeholder='Введите текст объявления']")
    CREATE_COMPANY_BUTTON = (By.XPATH, "//div[contains(text(), 'Создать кампанию')]")
    ADD_IMG_BUTTON = (By.XPATH, "//input[@data-test='image_90x75']")
    SAVE_IMG = (By.XPATH, "//input[@value='Сохранить изображение']")

    DELETE_IMG = (By.XPATH, "//div[contains(text(), 'Удалить все')]")
    APPLY_DELETE = (By.XPATH, "//div[contains(text(), 'Да, удалить')]")