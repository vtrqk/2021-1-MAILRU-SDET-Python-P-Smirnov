from selenium.webdriver.common.by import By


class LoginLocs:

    ENTER_BUTTON = (By.XPATH, "//div[contains(text(), 'Войти')]")
    LOGIN_FIELD = (By.XPATH, "//input[contains(@name, 'email')]")
    PASS_FIELD = (By.XPATH, "//input[contains(@name, 'pass')]")
    LOGIN_BUTTON = (By.XPATH, "//div[contains(@class, 'authForm-module-button')]")


class MenuLocs:

    MENU_EXIT = (By.XPATH, "//div[contains(@class, 'right-module-rightWrap')]")
    EXIT_BUTTON = (By.XPATH, "//a[contains(text(), 'Выйти')]")
    PARAMITRIZE_VAR = (By.XPATH, "//a[@href='{}']")


class ProfileLocs(MenuLocs):

    PROFILE_BUTTON = (By.XPATH, "//a[@href='/profile']")
    NAME_FIELD = (By.XPATH, "//div[@data-name='fio']//input")
    PHONE_FIELD = (By.XPATH, "//div[@data-name='phone']//input")
    MAIL_FILED = (By.XPATH, "//div[@class='js-additional-email profile__list__row__input']//input")
    SUBMIT_BUTTON = (By.XPATH, "//div[contains(text(), 'Сохранить')]")
