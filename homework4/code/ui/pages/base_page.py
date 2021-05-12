import os

from appium.webdriver.common.touch_action import TouchAction

from utils.decorator import wait
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException


class BasePage(object):
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

    def find(self, locator, err=NoSuchElementException):
        return wait(self.driver.find_element, error=err, by=locator[0], value=locator[1])

    def click(self, locator, err=ElementClickInterceptedException):
        elem = self.find(locator=locator)
        wait(elem.click, error=err)

    def swipe_up(self, swipetime=200):

        action = TouchAction(self.driver)
        dimension = self.driver.get_window_size()
        x = int(dimension['width'] / 2)
        start_y = int(dimension['height'] * 0.8)
        end_y = int(dimension['height'] * 0.2)
        action. \
            press(x=x, y=start_y). \
            wait(ms=swipetime). \
            move_to(x=x, y=end_y). \
            release(). \
            perform()

    @staticmethod
    def get_version(repo_root):
        path_to_file = os.path.abspath(os.path.join(repo_root, '..\\code\\stuff'))
        name_apk = os.listdir(path_to_file)
        version = (name_apk[0].split('_v'))[1].split('.apk')

        return version[0]

    def swipe_to_element(self, locator, max_swipes):

        already_swiped = 0
        while len(self.driver.find_elements(*locator)) == 0:
            if already_swiped > max_swipes:
                raise TimeoutException(f"Error with swipe to {locator}")
            self.swipe_up()
            already_swiped += 1

    def swipe_element_lo_left(self, locator, max_swipes):
        web_element = self.find(locator)
        left_x = web_element.location['x']
        right_x = left_x + web_element.rect['width']
        upper_y = web_element.location['y']
        lower_y = upper_y + web_element.rect['height']
        middle_y = (upper_y + lower_y) / 2
        action = TouchAction(self.driver)
        already_swiped = 0
        while max_swipes > already_swiped:
            action. \
                press(x=right_x, y=middle_y). \
                wait(ms=300). \
                move_to(x=left_x, y=middle_y). \
                release(). \
                perform()
            already_swiped += 1
