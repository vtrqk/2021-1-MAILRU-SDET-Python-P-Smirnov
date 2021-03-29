from selenium.webdriver.common.by import By


class LoginLocs:
    ENTER_BUTTON = (By.XPATH, "//div[contains(@class, '1BMAy4')]")

    LOGIN_FIELD = (By.XPATH, "//input[contains(@name, 'email')]")

    PASS_FIELD = (By.XPATH, "//input[contains(@name, 'pass')]")

    LOGIN_BUTTON = (By.XPATH, "//div[contains(@class, '2G6lZu')]")


class MenuLocs:
    MENU_EXIT = (By.XPATH, "//div[contains(@class, '25NVA9')]")

    EXIT_BUTTON = (By.XPATH, "//a[contains(text(), 'Выйти')]")


class ProfileLocs(MenuLocs):
    ENTER_BUTTON = (By.XPATH, "//div[contains(@class, '1BMAy4')]")

    LOGIN_FIELD = (By.XPATH, "//input[contains(@name, 'email')]")

    PASS_FIELD = (By.XPATH, "//input[contains(@name, 'pass')]")

    LOGIN_BUTTON = (By.XPATH, "//div[contains(@class, '2G6lZu')]")
