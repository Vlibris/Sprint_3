import pytest
@pytest.fixture
def example_correct_user():
    example_correct_user = User(name='Имя', login='почта@ya.ru', password='111111')
    return example_correct_user
@pytest.fixture
def example_not_correct_user():
    example_not_correct_user = User(name=None, login='п@ya.ru', password='1111')
    return example_not_correct_user



