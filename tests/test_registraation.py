from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestRegistration:
    # Проверка успешной регистрации
    def test_registration_positive_result(self, name_generator, login_generator, password_generator):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3)
        driver.find_element(*TestLocators.NAME_REGISTRATION_FORM).send_keys(name_generator)
        driver.find_element(*TestLocators.EMAIL_REGISTRATION_FORM).send_keys(login_generator)
        driver.find_element(*TestLocators.PASSWORD_REGISTRATION_FORM).send_keys(password_generator)
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        driver.quit()

# Проверка "некорректный пароль" при регистрации
    def test_incorrect_password_registration(self, name_generator, login_generator, not_correct_user):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        WebDriverWait(driver, 3)
        driver.find_element(*TestLocators.NAME_REGISTRATION_FORM).send_keys(name_generator)
        driver.find_element(*TestLocators.EMAIL_REGISTRATION_FORM).send_keys(login_generator)
        driver.find_element(*TestLocators.PASSWORD_REGISTRATION_FORM).send_keys(not_correct_user.password)
        driver.find_element(*TestLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 6)
        element = driver.find_element(*TestLocators.TEXT_INCORRECT_PASSWORD)
        assert element.get_attribute('class') == 'input__error text_type_main-default'
        driver.quit()






