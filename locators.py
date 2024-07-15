from selenium.webdriver.common.by import By


class StellarBurgersLocators:

    PERSONAL_AREA_BUTTON = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']") # Кнопка "Личный Кабинет"

    PAGE_BACKGROUND = (By.CLASS_NAME, "App_componentContainer__2JC2W") # Фон страницы

    REGISTRATION_BUTTON = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться"

    NAME_FIELD_REG = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input[contains(@class, 'text_type_main-default')]") # Поле "Имя" регистрация

    EMAIL_FIELD_REG = (By.XPATH, "//label[text()='Email']/following-sibling::input[contains(@class, 'text input__textfield text_type_main-default')]") # Поле "Email" регистрация

    PASSWORD_FIELD_REG = ((By.XPATH, "//div//input[@class='text input__textfield text_type_main-default' and @name='Пароль']")) # Поле "Пароль" регистрация

    BIG_REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Большая кнопка "Зарегистрироваться"

    INCORRECT_PASSWORD_MESSAGE = (By.XPATH, "//p[@class='input__error text_type_main-default']") # Текст ошибки "Некорректный пароль"

    LOGIN_FORM_NAME = ((By.XPATH, "//h2[text()='Вход']")) # Название формы авторизации - "Вход"

    AUTHORIZATION_FORM_BACKGROUND = (By.CSS_SELECTOR, ".Auth_login__3hAey")

    EMAIL_FIELD_LOG = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='name']") # Поле "Email" логин

    PASSWORD_FIELD_LOG = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='Пароль']") # Поле "Пароль" логин

    LOGIN_BUTTON_LOG = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']") # Кнопка "Войти" логин

    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка "Оформить заказ"

    LOGIN_BUTTON_REG = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Войти']") # Кнопка "Войти" логин

    PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']") # Кнопка "Восстановить пароль" логин

    LOGIN_BUTTON_REС = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Войти']") # Кнопка "Войти" восстановление пароля

    LOGIN_BUTTON_MAIN = (By.CSS_SELECTOR, ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg") # Кнопка "Войти в аккаунт"

    PAGE_BACKGROUND_MAIN = (By.XPATH, "//main[@class='App_componentContainer__2JC2W']") # Фон страницы главная

    PROFILE_TAB = (By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']") # Вкладка "Профиль" профиль

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and contains(text(), 'Конструктор')]") # Кнопка "Конструктор"

    MAKE_BURGER_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']") # Заголовок "Соберите бургер"

    MAKE_BURGER_CONSTRUCTOR_BACKGROUND = (By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2") # Фон конструктора бургеров

    SAUCES_TAB = (By.XPATH, "//span[@class='text text_type_main-default' and contains(text(),'Соусы')]") # Таб "Соусы"

    SAUCES_CONSTRUCTOR_HEADER = (By.XPATH, "//h2[contains(@class, 'text text_type_main-medium mb-6 mt-10') and contains(text(), 'Соусы')]") # Заголовок "Соусы" в конструкторе

    FILLINGS_TAB = (By.XPATH, "//span[@class='text text_type_main-default' and contains(text(),'Начинки')]") # Таб "Начинки"

    FILLINGS_CONSTRUCTOR_HEADER = (By.XPATH, "//h2[contains(@class, 'text text_type_main-medium mb-6 mt-10') and contains(text(), 'Начинки')]") # Заголовок "Начинки" в конструкторе

    BUNS_TAB = (By.XPATH, "//span[@class='text text_type_main-default' and contains(text(),'Булки')]") # Таб "Булки"

    BUNS_CONSTRUCTOR_HEADER = (By.XPATH, "//h2[contains(@class, 'text text_type_main-medium mb-6 mt-10') and contains(text(), 'Булки')]") # Заголовок "Булки" в конструкторе

    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']") # Кнопка "Выход"























