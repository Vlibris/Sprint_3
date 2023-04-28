from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Registration():
    def test_registration_mail_password_positive_result(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        driver.find_element(By.XPATH, ".//input[@name='name']").send_keys("почта@ya.ru")
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys("111111")
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        driver.quit()

