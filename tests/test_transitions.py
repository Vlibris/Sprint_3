from locators import PersonalAreaLocators, LoginFormLocators, HomePageLocators
from pages.base_page import BasePage


class TestTransitions:
    # Проверка перехода по клику на кнопку "Личный кабинет", неавторизованный пользователь
    def test_transition_click_button_personal_account_not_authorized_user(self, driver, url_login_form_page):
        base_page = BasePage(driver, url_login_form_page)
        base_page.open()
        driver.find_element(*PersonalAreaLocators.PERSONAL_ACCOUNT_BUTTON).click()
        base_page.element_is_visible(LoginFormLocators.TEXT_LOGIN_LOGIN_FORM)
        assert driver.current_url == url_login_form_page

    # Проверка перехода по клику на кнопку "Личный кабинет", авторизованный пользователь
    def test_transition_click_button_personal_account_authorized_user(self, driver, url_login_form_page, correct_user):
        base_page = BasePage(driver, url_login_form_page)
        base_page.open()
        driver.find_element(* LoginFormLocators.EMAIL_FIELD_LOGIN_FORM).send_keys(correct_user.login)
        driver.find_element(* LoginFormLocators.PASSWORD_FIELD_LOGIN_FORM).send_keys(correct_user.password)
        driver.find_element(* LoginFormLocators.LOGIN_BUTTON_LOGIN_FORM).click()
        base_page.element_is_visible(HomePageLocators.BUTTON_PLACE_ORDER)
        driver.find_element(*PersonalAreaLocators.PERSONAL_ACCOUNT_BUTTON).click()
        base_page.element_is_visible(PersonalAreaLocators.BUTTON_SAVE_PERSONAL_ACCOUNT)
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    # Проверка перехода из личного кабинета в конструктор, через кнопку конструктор, неавторизованный пользователь
    def test_transition_from_personal_account_button_constructor_not_authorized_user(self, url_login_form_page,
                                                                                     url_home_page, driver):
        base_page = BasePage(driver, url_login_form_page)
        base_page.open()
        driver.find_element(*HomePageLocators.BUTTON_CONSTRUCTOR).click()
        base_page.element_is_visible(HomePageLocators.LOGIN_BUTTON)

        assert driver.current_url == url_home_page

    # Проверка перехода из личного кабинета в конструктор, через кнопку конструктор, авторизованный пользователь
    def test_transition_from_personal_account_button_constructor_authorized_user(self, driver, url_login_form_page,
                                                                                 url_home_page, correct_user):
        base_page = BasePage(driver, url_login_form_page)
        base_page.open()
        driver.find_element(*LoginFormLocators.EMAIL_FIELD_LOGIN_FORM).send_keys(correct_user.login)
        driver.find_element(*LoginFormLocators.PASSWORD_FIELD_LOGIN_FORM).send_keys(correct_user.password)
        driver.find_element(*LoginFormLocators.LOGIN_BUTTON_LOGIN_FORM).click()
        base_page.element_is_visible(HomePageLocators.BUTTON_PLACE_ORDER)
        driver.find_element(*PersonalAreaLocators.PERSONAL_ACCOUNT_BUTTON).click()
        base_page.element_is_visible(PersonalAreaLocators.BUTTON_SAVE_PERSONAL_ACCOUNT)
        driver.find_element(*HomePageLocators.BUTTON_CONSTRUCTOR).click()
        base_page.element_is_visible(HomePageLocators.BUTTON_PLACE_ORDER)
        assert driver.current_url == url_home_page

    # Проверка перехода из личного кабинета в конструктор, через логотип Stellar Burgers, неавторизованный пользователь
    def test_transition_from_personal_account_logo_not_authorized_user(self, driver, url_login_form_page,
                                                                       url_home_page):
        base_page = BasePage(driver,  url_login_form_page)
        base_page.open()
        driver.find_element(*HomePageLocators.LOGO_STELLAR_BURGERS).click()
        base_page.element_is_visible(HomePageLocators.LOGIN_BUTTON)
        assert driver.current_url == url_home_page

    # Проверка перехода из личного кабинета в конструктор, через логотип Stellar Burgers, авторизованный пользователь
    def test_transition_from_personal_account_logo_authorized_user(self, driver, url_login_form_page, url_home_page,
                                                                   correct_user):
        base_page = BasePage(driver, url_login_form_page)
        base_page.open()
        driver.find_element(*LoginFormLocators.EMAIL_FIELD_LOGIN_FORM).send_keys(correct_user.login)
        driver.find_element(*LoginFormLocators.PASSWORD_FIELD_LOGIN_FORM).send_keys(correct_user.password)
        driver.find_element(*LoginFormLocators.LOGIN_BUTTON_LOGIN_FORM).click()
        base_page.element_is_visible(HomePageLocators.BUTTON_PLACE_ORDER)
        driver.find_element(*PersonalAreaLocators.PERSONAL_ACCOUNT_BUTTON).click()
        base_page.element_is_visible(PersonalAreaLocators.BUTTON_SAVE_PERSONAL_ACCOUNT)
        driver.find_element(*HomePageLocators.LOGO_STELLAR_BURGERS).click()
        base_page.element_is_visible(HomePageLocators.BUTTON_PLACE_ORDER)
        assert driver.current_url == url_home_page

    # Проверка перехода к разделу Булки
    def test_transition_section_buns(self, driver, url_home_page):
        base_page = BasePage(driver, url_home_page)
        base_page.open()
        driver.find_element(*HomePageLocators.SECTION_FILLING).click()
        base_page.element_is_visible(HomePageLocators.TEXT_FILLING)
        driver.find_element(*HomePageLocators.SECTION_BUNS).click()
        element = driver.find_element(*HomePageLocators.ACTIVE_SECTION_BUNS)
        assert element.get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 ' \
                                                 'noselect'

    # Проверка перехода к разделу соусы
    def test_transition_section_sauces(self, driver, url_home_page):
        base_page = BasePage(driver, url_home_page)
        base_page.open()
        driver.find_element(*HomePageLocators.SECTION_SAUCES).click()
        element = driver.find_element(*HomePageLocators.ACTIVE_SECTION_SAUCES)
        assert element.get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 ' \
                                                 'noselect'

    # Проверка перехода к разделу начинки
    def test_transition_section_filling(self, driver, url_home_page):
        base_page = BasePage(driver, url_home_page)
        base_page.open()
        driver.find_element(*HomePageLocators.SECTION_FILLING).click()
        element = driver.find_element(*HomePageLocators.ACTIVE_SECTION_FILLING)
        assert element.get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 ' \
                                                 'noselect'
