from selenium.webdriver.common.by import By
class TestLocators:
    LOGO_STELLAR_BURGERS = By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']"  # Логотип Stellar Burgers
    LOGIN_BUTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"  # Кнопка «Войти в аккаунт»
    EMAIL_FIELD_LOGIN_FORM = By.XPATH, ".//input[@name='name']"  # Поле «Email» в окне входа
    PASSWORD_FIELD_LOGIN_FORM = By.XPATH, ".//input[@name='Пароль']"  # Поле «Пароль» в окне входа
    LOGIN_BUTTON_LOGIN_FORM = By.XPATH, ".//button[text()='Войти']"  # Кнопка «Войти» в форме входа
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, ".//a[@href='/account']"  # Кнопка «Личный Кабинет»
    FIELD_NAME_REGISTRATION_FORM = By.XPATH, ".//label[text()= 'Имя']"  # Поле "Имя" в регистрации
    FIELD_EMAIL_REGISTRATION_FORM = By.XPATH, ".//label[text()= 'Email']"  # Поле "Email" в регистрации
    FIELD_PASSWORD_REGISTRATION_FORM = By.XPATH, ".//label[text()= 'Пароль']"  # Поле "Пароль" в регистрации
    REGISTER_BUTTON = By.XPATH, ".//button[text()= 'Зарегистрироваться']"  # Кнопка «Зарегистрироваться»
    LOGIN_BUTTON_REGISTRATION_FORM = By.XPATH, ".//a[text()= 'Войти']"  # Кнопка "Войти" в форме регистрации
    LOGIN_BUTTON_PERSONAL_ACCOUNT = By.XPATH, ".//button[text()='Войти']"  # Кнопка «Войти» в личном кабинете
    LOGIN_BUTTON_PASSWORD_RECOVERY = By.XPATH, ".//a[text()='Войти']"  # Кнопка «Войти» в форме восстановления пароля
    TEXT_INCORRECT_PASSWORD = By.XPATH, ".//p[text()='Некорректный пароль']"  # Текст "Некорректный пароль"
    BUTTON_PLACE_ORDER = By.XPATH, ".//button[text()='Оформить заказ']"  # Кнопка «Оформить заказ»
    BUTTON_EXIT_PERSONAL_ACCOUNT = By.XPATH, ".//button[text()='Выход']"  # Кнопка «Выйти» в личном кабинете
    TEXT_LOGIN_LOGIN_FORM = By.XPATH, ".//h2[text()='Вход']"  # Текст «Вход» в форме входа
    BUTTON_CONSTRUCTOR = By.XPATH, ".//p[text()='Конструктор']"  # Кнопка «Конструктор»
    SECTION_BANS = By.XPATH, ".//span[text()='Булки']"  # Раздел «Булки»
    SECTION_SAUCES = By.XPATH, ".//span[text()='Соусы']"  # Раздел «Соусы»
    SECTION_FILLING = By.XPATH, ".//span[text()='Начинки']"  # Раздел «Начинки»

