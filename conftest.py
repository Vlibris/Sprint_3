import pytest
import random as r
from selenium import webdriver

from data.data import correct_name, correct_login, correct_password, not_correct_name, not_correct_login, \
    not_correct_password, User

from urls import home_page, login_form_page, registration_page, password_recovery_page


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def url_home_page():
    return home_page()


@pytest.fixture()
def url_login_form_page():
    return login_form_page()


@pytest.fixture()
def url_registration_pag():
    return registration_page()


@pytest.fixture()
def url_password_recovery_page():
    return password_recovery_page()


@pytest.fixture()
def correct_user():
    return User(name=correct_name(), login=correct_login(), password=correct_password())


@pytest.fixture()
def not_correct_user():
    return User(name=not_correct_name(), login=not_correct_login(), password=not_correct_password())


@pytest.fixture()
def name_generator():
    name = ''

    for _ in range(4):
        name += r.choice(list('asdfghjkl'))
    return name


@pytest.fixture()
def password_generator():
    password = ''

    for _ in range(6):
        password += r.choice(list('1234567890'))
    return password


@pytest.fixture()
def login_generator():
    login = ''

    for _ in range(4):
        login += r.choice(list('1234567890qwertyuiop'))
    return login + str('@yandex.ru')
