from selenium.webdriver.common.by import By


class MainPageLocators:

    KEYBOARD_BUTTON = (By.ID, "ru.mail.search.electroscope:id/keyboard")
    INPUT_TEXT_FIELD = (By.ID, "ru.mail.search.electroscope:id/input_text")
    INPUT_TEXT_BUTTON = (By.ID, "ru.mail.search.electroscope:id/text_input_action")
    FACT_CARD_FIELD = (By.ID, "ru.mail.search.electroscope:id/item_dialog_fact_card_content_text")
    POPULATION_BUTTON = (By.XPATH, "//android.widget.TextView[@text='численность населения россии']")
    POPULATION_FIELD = (By.ID, "ru.mail.search.electroscope:id/item_dialog_fact_card_title")
    SCROLL_TO_BUTTON = (By.XPATH, "//android.widget.TextView[@text='Да']")

    RESULT_OF_MATH_FIELD = (By.XPATH, "//android.widget.TextView[@text={}]")

    SETTINGS_BUTTON = (By.ID, "ru.mail.search.electroscope:id/assistant_menu_bottom")

    NAME_NEWS_FIELD = (By.XPATH, "//android.widget.TextView[@text='{}']")

