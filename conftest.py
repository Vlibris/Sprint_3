import pytest
import random as r

class User:
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password

@pytest.fixture(scope='function')
def correct_user():
    return User(name='Влада', login='VladaPantyuhova9888@yandex.ru', password='808080')

@pytest.fixture(scope='function')
def not_correct_user():
    return User(name='', login='VladaPantyuhova9888', password='80808')

@pytest.fixture(scope='function')
def name_generator():
    name = ''
    for _ in range(4):
        name += r.choice(list('asdfghjkl'))
    return name

@pytest.fixture(scope='function')
def password_generator():
    password = ''
    for _ in range(6):
        password += r.choice(list('1234567890'))
    return password
@pytest.fixture(scope='function')
def login_generator():
    login = ''
    for _ in range(4):
        login += r.choice(list('1234567890qwertyuiop'))
    return login + str('@yandex.ru')

