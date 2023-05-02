from selenium.webdriver.common.by import By


class RegistrationFormLocators:
    NAME_REGISTRATION_FORM = By.XPATH, "//label[text()='Имя']/following-sibling::input"  # "Имя" в регистрации
    EMAIL_REGISTRATION_FORM = By.XPATH, "//label[text()='Email']/following-sibling::input"  # "Email" в регистрации
    PASSWORD_REGISTRATION_FORM = By.XPATH, ".//input[@name= 'Пароль']"  # "Пароль" в регистрации
    REGISTER_BUTTON = By.XPATH, ".//button[text()= 'Зарегистрироваться']"  # Кнопка «Зарегистрироваться»
    LOGIN_BUTTON_REGISTRATION_FORM = By.XPATH, ".//a[text()= 'Войти']"  # Кнопка "Войти" в форме регистрации
    TEXT_INCORRECT_PASSWORD = By.XPATH, ".//p[text()='Некорректный пароль']"  # Текст "Некорректный пароль"


class PersonalAreaLocators:
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, ".//a[@href='/account']"  # Кнопка «Личный Кабинет»
    LOGIN_BUTTON_PERSONAL_ACCOUNT = By.XPATH, ".//button[text()='Войти']"  # Кнопка «Войти» в личном кабинете
    BUTTON_EXIT_PERSONAL_ACCOUNT = By.XPATH, ".//button[text()='Выход']"  # Кнопка «Выйти» в личном кабинете
    BUTTON_SAVE_PERSONAL_ACCOUNT = By.XPATH, ".//button[text()='Сохранить']"  # Кнопка «Сохранить» в личном кабинет


class LoginFormLocators:
    TEXT_LOGIN_LOGIN_FORM = (By.XPATH, ".//h2[text()='Вход']")  # Текст «Вход» в форме входа
    EMAIL_FIELD_LOGIN_FORM = By.XPATH, ".//input[@name='name']"  # Поле «Email» в окне входа
    PASSWORD_FIELD_LOGIN_FORM = By.XPATH, ".//input[@name='Пароль']"  # Поле «Пароль» в окне входа
    LOGIN_BUTTON_LOGIN_FORM = By.XPATH, ".//button[text()='Войти']"  # Кнопка «Войти» в форме входа
    TEXT_INCORRECT_PASSWORD = By.XPATH, ".//p[text()='Некорректный пароль']"  # Текст "Некорректный пароль"
    LOGIN_BUTTON_PASSWORD_RECOVERY = By.XPATH, ".//a[text()='Войти']"  # Кнопка «Войти» в форме восстановления пароля


class HomePageLocators:
    BUTTON_PLACE_ORDER = By.XPATH, ".//button[text()='Оформить заказ']"  # Кнопка «Оформить заказ»
    LOGO_STELLAR_BURGERS = By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']"  # Логотип Stellar Burgers
    BUTTON_CONSTRUCTOR = By.XPATH, ".//p[text()='Конструктор']"  # Кнопка «Конструктор»
    SECTION_BUNS = By.XPATH, ".//span[text()='Булки']"  # Раздел «Булки»
    SECTION_SAUCES = By.XPATH, ".//span[text()='Соусы']"  # Раздел «Соусы»
    SECTION_FILLING = By.XPATH, ".//span[text()='Начинки']"  # Раздел «Начинки»
    TEXT_FILLING = By.XPATH, ".//h2[text()='Начинки']"  # Текст "Начинки"

    ACTIVE_SECTION_BUNS = By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 " \
                                    "noselect']"  # активен раздел «Булки»
    ACTIVE_SECTION_SAUCES = By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 " \
                                      "pl-10 noselect']"  # активен раздел  «Соусы»
    ACTIVE_SECTION_FILLING = By.XPATH, ".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 " \
                                       "pl-10 noselect']"  # активен раздел «Начинки»
    LOGIN_BUTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"  # Кнопка «Войти в аккаунт»
