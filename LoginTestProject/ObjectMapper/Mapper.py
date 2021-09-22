class Mapper:

    # This class contains the objects across all the different pages whose tests are implemented
    # Login page objects
    username_textbox_id = "email"
    password_textbox_id = "password"
    login_button_id = "logIn"
    invalid_login_text_xpath = "//body[1]/div[2]/form[1]/div[3]/div[1]/p[1]"
    signup_link_xpath = "//a[contains(text(),'Sign up')]"
    needhelp_link_id = "forgot-password-link"
    reset_password_text = "//h2[contains(text(),'Let’s reset your password')]"
    hudl_image_xpath = "//body/div[2]/form[1]/div[1]"
    login_back_arrow_xpath = "//body/div[2]/div[1]/div[1]"
    login_with_organization_button_id = "logInWithOrganization"
    login_with_organization_text_xpath = "//h2[contains(text(),'Log into Hudl with your Organization')]"
    remember_me_checkbox_xpath = "//label[contains(text(),'Remember me')]"

    # Home page objects
    homepage_xpath = "//span[contains(text(),'Home')]"
    home_coach_button_xpath = "//body/div[@id='ssr-webnav']/div[1]/div[1]/nav[1]/div[4]/div[2]/div[1]/div[2]"
    logout_button = "//body/div[@id='ssr-webnav']/div[1]/div[1]/nav[1]/div[4]/div[2]/div[2]/div[3]/a[1]"

    # Welcome page objects
    welcome_login_button_xpath = "//header/div[2]/ul[1]/li[3]/a[1]"
    welcome_hudl_logo_xpath = "//header/div[1]/a[1]/img[1]"

    #SignUp Page pbjects
    request_free_demo_xpath = "//h1[contains(text(),'Request a Free Demo')]"
