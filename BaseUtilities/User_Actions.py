import time

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserActions():

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("Element not visible in time.")

    def click(self, locator, wait_time=5):
        self.wait_for_element(locator, wait_time)
        self.driver.find_element(*locator).click()

    def get_text(self, locator, wait_time=5):
        self.wait_for_element(locator, wait_time)
        return self.driver.find_element(*locator).text

    def type(self, locator, value, wait_time=5):
        self.wait_for_element(locator, wait_time)
        self.driver.find_element(*locator).send_keys(value)

    def element_should_be_visible(self, locator, wait_time=5):
        self.wait_for_element(locator, wait_time)
        assert self.is_element_present(locator) == True, "Element " + locator + " is not visible."

    def element_should_not_be_visible(self, locator):
        assert self.is_element_present(locator) == False, "Element " + locator + " is visible."

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def is_element_enabled(self, locator):
        try:
            self.driver.find_element(locator).is_enabled()
            return True
        except NoSuchElementException:
            return False

    def wait_for_seconds(self, seconds):
        time.sleep(seconds)
