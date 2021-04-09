from selenium.webdriver.common.by import By
from ui.locators.dashboard_locators import DashBoardLocators


class SegmentsLocators(DashBoardLocators):

    CREATE_BUTTON = (By.XPATH, "//a[@href='/segments/segments_list/new/']")
    SEGMENT_NAME = (By.XPATH, "//a[contains(text(), '{}')]")
    ID_CHECKBOX = (By.XPATH, "//div[contains(@class, 'segmentsTable-module-idCellWrap')]//input")
    ACTION_BUTTON = (By.XPATH, "//span[contains(text(), 'Действия')]")
    DELETE_BUTTON = (By.XPATH, "//li[contains(text(), 'Удалить')]")
