from LoginTestProject.ObjectMapper.Mapper import Mapper
from selenium.common.exceptions import NoSuchElementException
import time


# this class has the implementation for all the methods related to the home page after sign in

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.homepage_xpath = Mapper.homepage_xpath
        self.home_coach_button_xpath = Mapper.home_coach_button_xpath
        self.logout_button = Mapper.logout_button

    def verify_valid_login_text(self):
        time.sleep(2)
        try:
            assert self.driver.find_element_by_xpath(self.homepage_xpath).text == "Home"
        except NoSuchElementException:
            assert False

    def logout_user(self):
        try:
            self.driver.find_element_by_xpath(self.home_coach_button_xpath).click()
            self.driver.find_element_by_xpath(self.logout_button).click()
        except NoSuchElementException:
            assert False
