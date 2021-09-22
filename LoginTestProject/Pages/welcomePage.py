from LoginTestProject.ObjectMapper.Mapper import Mapper
from selenium.common.exceptions import NoSuchElementException


# this class has the implementation for all the methods related to the welcome page
class WelcomePage:

    def __init__(self, driver):
        self.driver = driver
        self.welcome_login_button_xpath = Mapper.welcome_login_button_xpath
        self.welcome_hudl_logo_xpath = Mapper.welcome_hudl_logo_xpath

    def click_welcome_login_button(self):
        try:
            self.driver.find_element_by_xpath(self.welcome_login_button_xpath).click()
        except NoSuchElementException:
            assert False

    def verify_welcome_page(self):
        try:
            self.driver.find_element_by_xpath(self.welcome_hudl_logo_xpath)
        except NoSuchElementException:
            assert False
