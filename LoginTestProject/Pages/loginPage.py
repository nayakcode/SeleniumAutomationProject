import time
from LoginTestProject.ObjectMapper.Mapper import Mapper
from selenium.common.exceptions import NoSuchElementException


# this class contains all the methods and objects that are used by the login page
class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = Mapper.username_textbox_id
        self.password_textbox_id = Mapper.password_textbox_id
        self.login_button_id = Mapper.login_button_id
        self.invalid_login_text_xpath = Mapper.invalid_login_text_xpath
        self.homepage_xpath = Mapper.homepage_xpath
        self.signup_link_xpath = Mapper.signup_link_xpath
        self.needhelp_link_id = Mapper.needhelp_link_id
        self.reset_password_text = Mapper.reset_password_text
        self.hudl_image_xpath = Mapper.hudl_image_xpath
        self.login_back_arrow_xpath = Mapper.login_back_arrow_xpath
        self.login_with_organization_button_id = Mapper.login_with_organization_button_id
        self.login_with_organization_text_xpath = Mapper.login_with_organization_text_xpath
        self.remember_me_checkbox_xpath = Mapper.remember_me_checkbox_xpath

    def enter_username(self, username):
        try:
            self.driver.find_element_by_id(self.username_textbox_id).clear()
            self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)
        except NoSuchElementException:
            assert False

    def enter_password(self, password):
        try:
            self.driver.find_element_by_id(self.password_textbox_id).clear()
            self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
        except NoSuchElementException:
            assert False

    def click_login_button(self):
        try:
            self.driver.find_element_by_id(self.login_button_id).click()
        except NoSuchElementException:
            assert False

    def verify_invalid_login_text(self):
        time.sleep(2)
        assert self.driver.find_element_by_xpath(
                self.invalid_login_text_xpath).text == "We didn't recognize that email and/or password. Need help?"

    def click_signup_link(self):
        # time.sleep(2)
        try:
            self.driver.find_element_by_xpath(self.signup_link_xpath).click()
        except NoSuchElementException:
            assert False

    def click_needhelp_link(self):
        try:
            self.driver.find_element_by_id(self.needhelp_link_id).click()
        except NoSuchElementException:
            assert False

    def verify_needhelp_page(self):
        try:
            assert self.driver.find_element_by_xpath(self.reset_password_text)
        except NoSuchElementException:
            assert False

    def click_hudl_image(self):
        try:
            self.driver.find_element_by_xpath(self.hudl_image_xpath).click()
        except NoSuchElementException:
            assert False

    def click_back_arrow(self):
        try:
            self.driver.find_element_by_xpath(self.login_back_arrow_xpath).click()
        except NoSuchElementException:
            assert False

    def click_login_with_organization(self):
        try:
            self.driver.find_element_by_id(self.login_with_organization_button_id).click()
        except NoSuchElementException:
            assert False

    def verify_login_with_organization(self):
        try:
            self.driver.find_element_by_xpath(self.login_with_organization_text_xpath)
        except NoSuchElementException:
            assert False

    def click_remember_me_option(self):
        try:
            self.driver.find_element_by_xpath(self.remember_me_checkbox_xpath).click()
        except NoSuchElementException:
            assert False

    def verify_if_email_is_remembered(self, validusername):
        time.sleep(2)
        assert self.driver.find_element_by_id(self.username_textbox_id).get_attribute('value') == validusername
