class User:
    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password


def correct_name():
    name = "Влада"
    return name


def correct_login():
    login = "VladaPantyuhova9888@yandex.ru"
    return login


def correct_password():
    password = "808080"
    return password


def not_correct_name():
    name = ""
    return name


def not_correct_login():
    login = "VladaPantyuhova9888"
    return login


def not_correct_password():
    password = "80808"
    return password
