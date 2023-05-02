from locators import HomePageLocators, LoginFormLocators, PersonalAreaLocators, RegistrationFormLocators
from pages.base_page import BasePage


class TestEntranceExit:
    # Проверка входа через кнопку "Войти в аккаунт", положительный результат
    def test_entrance_button_login_correct_email_and_password_positive_result(self, driver, url_home_page,
                                                                              correct_user):
        page = BasePage(driver, url_home_page)
        page.open()
        driver.find_element(*HomePageLocators.LOGIN_BUTTON).click()
        page.element_is_visible(LoginFormLocators.TEXT_LOGIN_LOGIN_FORM)
        driver.find_element(*LoginFormLocators.EMAIL_FIELD_LOGIN_FORM).send_keys(correct_user.login)
        driver.find_element(*LoginFormLocators.PASSWORD_FIELD_LOGIN_FORM).send_keys(correct_user.password)
        driver.find_element(*LoginFormLocators.LOGIN_BUTTON_LOGIN_FORM).click()
        page.element_is_visible(HomePageLocators.BUTTON_PLACE_ORDER)
        assert driver.current_url == url_home_page
        driver.quit()

    # Проверка входа через кнопку "Войти в аккаунт", негативный результат
    def test_entrance_button_login_incorrect_password_negative_result(self, driver, url_home_page, url_login_form_page,
                                                                      correct_user, not_correct_user):
        page = BasePage(driver, url_home_page)
        page.open()
        driver.find_element(*HomePageLocators.LOGIN_BUTTON).click()
        page.element_is_visible(LoginFormLocators.TEXT_LOGIN_LOGIN_FORM)
        driver.find_element(*LoginFormLocators.EMAIL_FIELD_LOGIN_FORM).send_keys(correct_user.login)
        driver.find_element(*LoginFormLocators.PASSWORD_FIELD_LOGIN_FORM).send_keys(not_correct_user.password)
        driver.find_element(*LoginFormLocators.LOGIN_BUTTON_LOGIN_FORM).click()
        page.element_is_visible(LoginFormLocators.TEXT_INCORRECT_PASSWORD)
        assert driver.current_url == url_login_form_page
        driver.quit()

    # Проверка входа через кнопку "Личный кабинет", позитивный результат
    def test_entrance_personal_cabinet_correct_email_and_password_positive_result(self, driver, url_home_page,
                                                                                  correct_user):
        page = BasePage(driver, url_home_page)
        page.open()
        driver.find_element(*PersonalAreaLocators.PERSONAL_ACCOUNT_BUTTON).click()
        page.element_is_visible(LoginFormLocators.TEXT_LOGIN_LOGIN_FORM)
        driver.find_element(*LoginFormLocators.EMAIL_FIELD_LOGIN_FORM).send_keys(correct_user.login)
        driver.find_element(*LoginFormLocators.PASSWORD_FIELD_LOGIN_FORM).send_keys(correct_user.password)
        driver.find_element(*LoginFormLocators.LOGIN_BUTTON_LOGIN_FORM).click()
        page.element_is_visible(HomePageLocators.BUTTON_PLACE_ORDER)
        assert driver.current_url == url_home_page
        driver.quit()

    # Проверка входа через кнопку "Войти" в форме регистрации, позитивный результат
    def test_entrance_registration_form_positive_result(self, driver, url_registration_pag, url_home_page,
                                                        correct_user):
        page = BasePage(driver, url_registration_pag)
        page.open()
        driver.find_element(*RegistrationFormLocators.LOGIN_BUTTON_REGISTRATION_FORM).click()
        page.element_is_visible(LoginFormLocators.TEXT_LOGIN_LOGIN_FORM)
        driver.find_element(*LoginFormLocators.EMAIL_FIELD_LOGIN_FORM).send_keys(correct_user.login)
        driver.find_element(*LoginFormLocators.PASSWORD_FIELD_LOGIN_FORM).send_keys(correct_user.password)
        driver.find_element(*LoginFormLocators.LOGIN_BUTTON_LOGIN_FORM).click()
        page.element_is_visible(HomePageLocators.BUTTON_PLACE_ORDER)
        assert driver.current_url == url_home_page
        driver.quit()

    # Проверка входа через кнопку "Войти" в форме восстановления пароля, позитивный результат
    def test_entrance_restore_password_positive_result(self, driver, url_home_page, url_password_recovery_page,
                                                       correct_user):
        page = BasePage(driver, url_password_recovery_page)
        page.open()
        driver.find_element(*LoginFormLocators.LOGIN_BUTTON_PASSWORD_RECOVERY).click()
        page.element_is_visible(LoginFormLocators.TEXT_LOGIN_LOGIN_FORM)
        driver.find_element(*LoginFormLocators.EMAIL_FIELD_LOGIN_FORM).send_keys(correct_user.login)
        driver.find_element(*LoginFormLocators.PASSWORD_FIELD_LOGIN_FORM).send_keys(correct_user.password)
        driver.find_element(*LoginFormLocators.LOGIN_BUTTON_LOGIN_FORM).click()
        page.element_is_visible(HomePageLocators.BUTTON_PLACE_ORDER)
        assert driver.current_url == url_home_page
        driver.quit()

    # Проверка выхода через кнопку "Выйти" в личном кабинете
    def test_exit_personal_cabinet_positive_result(self, driver, url_login_form_page, correct_user):
        page = BasePage(driver, url_login_form_page)
        page.open()
        driver.find_element(*LoginFormLocators.EMAIL_FIELD_LOGIN_FORM).send_keys(correct_user.login)
        driver.find_element(*LoginFormLocators.PASSWORD_FIELD_LOGIN_FORM).send_keys(correct_user.password)
        driver.find_element(*LoginFormLocators.LOGIN_BUTTON_LOGIN_FORM).click()
        page.element_is_visible(HomePageLocators.BUTTON_PLACE_ORDER)
        driver.find_element(*PersonalAreaLocators.PERSONAL_ACCOUNT_BUTTON).click()
        page.element_is_visible(PersonalAreaLocators.BUTTON_EXIT_PERSONAL_ACCOUNT)
        driver.find_element(*PersonalAreaLocators.BUTTON_EXIT_PERSONAL_ACCOUNT).click()
        page.element_is_visible(LoginFormLocators.TEXT_LOGIN_LOGIN_FORM)
        assert driver.current_url == url_login_form_page
        driver.quit()
