from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestTransitions:
    # Проверка перехода по клику на кнопку "Личный кабинет", неавторизованный пользователь
    def test_transition_click_button_personal_account_not_authorized_user(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        driver.quit()

    # Проверка перехода по клику на кнопку "Личный кабинет", авторизованный пользователь
    def test_transition_click_button_personal_account_authorized_user(self, correct_user):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*TestLocators.EMAIL_FIELD_LOGIN_FORM).send_keys(correct_user.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD_LOGIN_FORM).send_keys(correct_user.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOGIN_FORM).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Сохранить']")))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
        driver.quit()

    # Проверка перехода из личного кабинета в конструктор, через кнопку конструктор, неавторизованный пользователь
    def test_transition_from_personal_account_button_constructor_not_authorized_user(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']")))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        driver.quit()

    # Проверка перехода из личного кабинета в конструктор, через кнопку конструктор, авторизованный пользователь
    def test_transition_from_personal_account_button_constructor_authorized_user(self, correct_user):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*TestLocators.EMAIL_FIELD_LOGIN_FORM).send_keys(correct_user.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD_LOGIN_FORM).send_keys(correct_user.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOGIN_FORM).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Сохранить']")))
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        driver.quit()

    # Проверка перехода из личного кабинета в конструктор, через логотип Stellar Burgers, неавторизованный пользователь
    def test_transition_from_personal_account_logo_not_authorized_user(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*TestLocators.LOGO_STELLAR_BURGERS).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Войти в аккаунт']")))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        driver.quit()

    # Проверка перехода из личного кабинета в конструктор, через логотип Stellar Burgers, авторизованный пользователь
    def test_transition_from_personal_account_logo_authorized_user(self, correct_user):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*TestLocators.EMAIL_FIELD_LOGIN_FORM).send_keys(correct_user.login)
        driver.find_element(*TestLocators.PASSWORD_FIELD_LOGIN_FORM).send_keys(correct_user.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOGIN_FORM).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Сохранить']")))
        driver.find_element(*TestLocators.LOGO_STELLAR_BURGERS).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        driver.quit()

    # Проверка перехода к разделу Булки
    def test_transition_section_buns(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SECTION_FILLING).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Начинки']")))
        driver.find_element(*TestLocators.SECTION_BUNS).click()
        element = driver.find_element(*TestLocators.ACTIVE_SECTION_BUNS)
        assert element.get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 ' \
                                                 'noselect'
        driver.quit()

    # Проверка перехода к разделу соусы
    def test_transition_section_sauces(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SECTION_SAUCES).click()
        element = driver.find_element(*TestLocators.ACTIVE_SECTION_SAUCES)
        assert element.get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 ' \
                                                 'noselect'
        driver.quit()

    # Проверка перехода к разделу начинки
    def test_transition_section_filling(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.SECTION_FILLING).click()
        element = driver.find_element(*TestLocators.ACTIVE_SECTION_FILLING)
        assert element.get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 ' \
                                                 'noselect'
        driver.quit()
