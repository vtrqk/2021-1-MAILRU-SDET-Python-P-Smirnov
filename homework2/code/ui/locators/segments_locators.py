from selenium.webdriver.common.by import By
from ui.locators.dashboard_locators import DashBoardLocators


class SegmentsLocators(DashBoardLocators):

    CREATE_BUTTON_FIRST = (By.XPATH, "//a[@href='/segments/segments_list/new/']")
    SEGMENT_NAME = (By.XPATH, "//a[contains(text(), '{}')]")
    CREATE_BUTTON_SECOND = (By.XPATH, "//div[contains(text(), 'Создать сегмент')]")
    ID_CHECKBOX = (By.XPATH, "//a[contains(text(), '{}')]/ancestor::div[@class='ReactVirtualized__Grid']//input")
    ACTION_BUTTON = (By.XPATH, "//span[contains(text(), 'Действия')]")
    DELETE_BUTTON = (By.XPATH, "//li[contains(text(), 'Удалить')]")
