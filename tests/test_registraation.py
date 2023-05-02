from locators import RegistrationFormLocators, LoginFormLocators
from pages.base_page import BasePage


class TestRegistration:
    # Проверка успешной регистрации
    def test_registration_positive_result(self, driver, url_registration_pag, name_generator, password_generator,
                                          login_generator):
        registration_form_page = BasePage(driver, url_registration_pag)
        registration_form_page.open()
        driver.find_element(*RegistrationFormLocators.NAME_REGISTRATION_FORM).send_keys(name_generator)
        driver.find_element(*RegistrationFormLocators.EMAIL_REGISTRATION_FORM).send_keys(login_generator)
        driver.find_element(*RegistrationFormLocators.PASSWORD_REGISTRATION_FORM).send_keys(password_generator)
        driver.find_element(*RegistrationFormLocators.REGISTER_BUTTON).click()
        registration_form_page.element_is_visible(LoginFormLocators.TEXT_LOGIN_LOGIN_FORM)
        element = driver.find_element(*LoginFormLocators.LOGIN_BUTTON_LOGIN_FORM)
        assert element.get_attribute("class") == 'button_button__33qZ0 button_button_type_primary__1O7Bx ' \
                                                 'button_button_size_medium__3zxIa'

    # Проверка "некорректный пароль" при регистрации
    def test_incorrect_password_registration(self, driver, url_registration_pag, name_generator, login_generator,
                                             not_correct_user):
        registration_form_page = BasePage(driver, url_registration_pag)
        registration_form_page.open()
        driver.find_element(*RegistrationFormLocators.NAME_REGISTRATION_FORM).send_keys(name_generator)
        driver.find_element(*RegistrationFormLocators.EMAIL_REGISTRATION_FORM).send_keys(login_generator)
        driver.find_element(*RegistrationFormLocators.PASSWORD_REGISTRATION_FORM).send_keys(
            not_correct_user.password)
        driver.find_element(*RegistrationFormLocators.REGISTER_BUTTON).click()
        registration_form_page.element_is_visible(RegistrationFormLocators.TEXT_INCORRECT_PASSWORD)
        element = driver.find_element(*RegistrationFormLocators.TEXT_INCORRECT_PASSWORD)
        assert element.get_attribute('class') == 'input__error text_type_main-default'

