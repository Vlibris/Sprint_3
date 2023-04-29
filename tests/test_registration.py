from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Registration():
    def test_registration_positive_result(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        RANDOM_MAIL=

        driver.find_element(By.XPATH, ".//label[text()= 'Имя']").send_keys([])

        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        driver.quit()

