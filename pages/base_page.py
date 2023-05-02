from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EX


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=6):
        return WebDriverWait(self.driver, timeout).until(EX.visibility_of_element_located(locator))
