from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

class TestEntranceExit():
    # Проверка входа через кнопку "Войти в аккаунт", положительный результат
    def test_entrance_button_login_correct_email_and_password_positive_result(self, correct_user):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3)
        driver.find_element(*TestLocators.EMAIL_FIELD_LOGIN_FORM).send_keys(correct_user.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD_LOGIN_FORM).send_keys(correct_user.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOGIN_FORM).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        driver.quit()

    # Проверка входа через кнопку "Войти в аккаунт", негативный результат
    def test_entrance_button_login_incorrect_password_negative_result(self, correct_user, not_correct_user):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3)
        driver.find_element(*TestLocators.EMAIL_FIELD_LOGIN_FORM).send_keys(correct_user.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD_LOGIN_FORM).send_keys(not_correct_user.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOGIN_FORM).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//p[text()='Некорректный пароль']")))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        driver.quit()

    # Проверка входа через кнопку "Личный кабинет", позитивный результат
    def test_entrance_personal_cabinet_correct_email_and_password_positive_result(self, correct_user):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3)
        driver.find_element(*TestLocators.EMAIL_FIELD_LOGIN_FORM).send_keys(correct_user.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD_LOGIN_FORM).send_keys(correct_user.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOGIN_FORM).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        driver.quit()

    # Проверка входа через кнопку "Войти" в форме регистрации, позитивный результат
    def test_entrance_registration_form_positive_result(self, correct_user):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.LOGIN_BUTTON_REGISTRATION_FORM).click()
        WebDriverWait(driver, 3)
        driver.find_element(*TestLocators.EMAIL_FIELD_LOGIN_FORM).send_keys(correct_user.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD_LOGIN_FORM).send_keys(correct_user.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOGIN_FORM).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        driver.quit()

    # Проверка входа через кнопку "Войти" в форме восстановления пароля, позитивный результат
    def test_entrance_restore_password_positive_result(self, correct_user):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(*TestLocators.LOGIN_BUTTON_PASSWORD_RECOVERY).click()
        WebDriverWait(driver, 3)
        driver.find_element(*TestLocators.EMAIL_FIELD_LOGIN_FORM).send_keys(correct_user.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD_LOGIN_FORM).send_keys(correct_user.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOGIN_FORM).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        driver.quit()

    # Проверка выхода через кнопку "Выйти" в личном кабинете
    def test_exit_personal_cabinet_positive_result(self, correct_user):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*TestLocators.EMAIL_FIELD_LOGIN_FORM).send_keys(correct_user.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD_LOGIN_FORM).send_keys(correct_user.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOGIN_FORM).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Выход']")))
        driver.find_element(*TestLocators.BUTTON_EXIT_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        driver.quit()
