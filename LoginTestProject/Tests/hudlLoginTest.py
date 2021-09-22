import unittest
import time
import configparser
import HtmlTestRunner
from selenium import webdriver
from LoginTestProject.Pages.loginPage import LoginPage
from LoginTestProject.Pages.welcomePage import WelcomePage
from LoginTestProject.Pages.homePage import HomePage
from LoginTestProject.Pages.signupPage import SignUpPage
from parameterized import parameterized

# Reading credentials from the Config file

config = configparser.ConfigParser()
config.read(r'Configurations/config.ini')
validUsername = config.get('credentials', 'valid_username')
validPassword = config.get('credentials', 'valid_password')


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # initializing chrome driver
        self.driver = webdriver.Chrome(executable_path='drivers/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    # Parameterization to reduce redundancy
    # Testing different combinations of invalid usernames and passwords
    @parameterized.expand([
        ("InvalidUsername", "invalidemail@xyz.com", validPassword),
        ("InvalidPassword", validUsername, "InvalidPassword"),
        ("InvalidPwdandUsername", "invalidemail@xyz.com", "InvalidPassword"),
    ])
    def test_invalid_login(self, name, username, password):
        driver = self.driver
        driver.get("https://www.hudl.com")
        # print(name)

        welcome = WelcomePage(driver)
        welcome.click_welcome_login_button()

        login = LoginPage(driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login_button()
        login.verify_invalid_login_text()

    # testing login functionality with valid credentials
    def test_valid_login(self):
        driver = self.driver
        driver.get("https://www.hudl.com")

        # HUDL welcome page actions (to click on the login button)
        welcome = WelcomePage(driver)
        welcome.click_welcome_login_button()

        # Login page actions
        login = LoginPage(driver)
        login.enter_username(validUsername)
        login.enter_password(validPassword)
        login.click_login_button()

        # Home Page actions
        home = HomePage(driver)
        home.verify_valid_login_text()
        home.logout_user()

    # Testing if the sign up link works
    def test_validate_signup_page(self):
        driver = self.driver
        driver.get("https://www.hudl.com")

        # HUDL welcome page actions

        welcome = WelcomePage(driver)
        welcome.click_welcome_login_button()

        # Login Page Actions
        login = LoginPage(driver)
        login.click_signup_link()

        # Signup page actions
        signup = SignUpPage(driver)
        signup.verify_signuppage()

    # Testing the forgot password (Need help) link
    def test_validate_forgot_password_page(self):
        driver = self.driver
        driver.get("https://www.hudl.com")

        # HUDL welcome page actions

        welcome = WelcomePage(driver)
        welcome.click_welcome_login_button()

        # Login Page Actions
        login = LoginPage(driver)
        login.click_needhelp_link()
        login.verify_needhelp_page()

    # testing if clicking the HUDL logo navigates control to the welcome page
    def test_validate_hudl_image_navigation(self):
        driver = self.driver
        driver.get("https://www.hudl.com")

        # HUDL welcome page options

        welcome = WelcomePage(driver)
        welcome.click_welcome_login_button()

        # login page actions

        login = LoginPage(driver)
        login.click_hudl_image()

        welcome.verify_welcome_page()

    # testing if back arrow takes the user to the welcome page
    def test_login_back_arrow_navigation(self):
        driver = self.driver
        driver.get("https://www.hudl.com")

        # HUDL welcome page options

        welcome = WelcomePage(driver)
        welcome.click_welcome_login_button()

        # login page actions

        login = LoginPage(driver)
        login.click_back_arrow()

        welcome.verify_welcome_page()

    # testing if the login with organization button works
    def test_login_with_organization(self):
        driver = self.driver
        driver.get("https://www.hudl.com")

        # HUDL welcome page options

        welcome = WelcomePage(driver)
        welcome.click_welcome_login_button()

        # login page actions

        login = LoginPage(driver)
        login.click_login_with_organization()
        login.verify_login_with_organization()

    # testing if the remember me option actually remembers the user's email
    def test_remember_me_option(self):
        driver = self.driver
        driver.get("https://www.hudl.com")

        # HUDL welcome page options

        welcome = WelcomePage(driver)
        welcome.click_welcome_login_button()

        # login page actions

        login = LoginPage(driver)
        login.click_remember_me_option()
        login.enter_username(validUsername)
        login.enter_password(validPassword)
        login.click_login_button()

        # Home Page actions
        home = HomePage(driver)
        time.sleep(2)
        home.logout_user()

        welcome.click_welcome_login_button()

        # Validate if email is remembered
        login.verify_if_email_is_remembered(validUsername)

    # closing the driver
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Tests Completed")


# this is to enable html reporting for all the tests
# the test reports are available under the /TestReports directory
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='TestReports', verbosity=2))
