from selenium.webdriver.common.by import By


class SegmentsNewLocators:

    PARAM_CHECKBOX = (By.XPATH, "//div[@class='adding-segments-source']//input")
    ADD_BUTTON = (By.XPATH, "//div[contains(text(), 'Добавить сегмент')]")
    NEW_NAME_FIELD = (By.XPATH, "//div[@class='input input_create-segment-form']/div/input")
    CREATE_BUTTON = (By.XPATH, "//div[contains(text(), 'Создать сегмент')]")
