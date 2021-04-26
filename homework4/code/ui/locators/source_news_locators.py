from selenium.webdriver.common.by import By


class SourceNewsLocators:

    NAME_NEWS_BUTT0N = (By.XPATH, "//android.widget.FrameLayout[@index='1']")
    SELECT_NEWS_BUTTON = (By.ID, "ru.mail.search.electroscope:id/news_sources_item_selected")