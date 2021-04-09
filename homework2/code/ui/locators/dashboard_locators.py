from selenium.webdriver.common.by import By


class DashBoardLocators:

    SEGMENTS_BUTTON = (By.XPATH, "//a[@href='/segments']")
    NEW_CAMPAIGN_BUTTON = (By.XPATH, "//div[contains(text(), 'Создать кампанию')]")
    MENU_EXIT = (By.XPATH, "//div[contains(@class, 'right-module-rightWrap')]")
    EXIT_BUTTON = (By.XPATH, "//a[contains(text(), 'Выйти')]")
    CHECK_COMPANY = (By.XPATH, "//a[contains(text(), '{}')]")
    ID_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")
    ACTION_BUTTON = (By.XPATH, "//span[contains(text(), 'Действия')]")
    DELETE_COMPANY_BUTTON = (By.XPATH, "//li[@title='Удалить']")
