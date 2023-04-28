from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture('example_correct_user', 'example_not_correct_user')
class TestEntrance():
    def test_entrance_correct_mail_and_password_positive_result(self, example_correct_user):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        WebDriverWait(driver, 3)
        driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(example_correct_user.get("login"))
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(example_correct_user.get("password"))
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        driver.quit()

    def test_entrance_incorrect_password_negative_result(self, example_correct_user, example_not_correct_user):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        driver.find_element(By.XPATH, ".//input[@name='name']").send_keys(example_correct_user("login"))
        driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys(example_not_correct_user("password"))
        driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//p[text()='Некорректный пароль']")))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
        driver.quit()
