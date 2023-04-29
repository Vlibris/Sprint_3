import pytest
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

