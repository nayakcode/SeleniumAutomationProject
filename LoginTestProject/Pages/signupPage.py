from LoginTestProject.ObjectMapper.Mapper import Mapper


# this class contains all the methods and objects used by the sign up page
class SignUpPage:

    def __init__(self, driver):
        self.driver = driver
        self.request_free_demo_xpath = Mapper.request_free_demo_xpath

    def verify_signuppage(self):
        assert self.driver.find_element_by_xpath(self.request_free_demo_xpath).text == "Request a Free Demo"
