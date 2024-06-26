import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestGoToConstructorAndLogo:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def teardown_method(self):
        self.driver.quit()

    def test_go_to_constructor(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")))
        self.driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']")))
        self.driver.find_element(By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='name']").send_keys("ebashutest@mail.ru")
        self.driver.find_element(By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys("123456")
        self.driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//main[@class='App_componentContainer__2JC2W']")))
        self.driver.find_element(By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and contains(@href, '/account')]").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and contains(text(), 'Конструктор')]")))
        self.driver.find_element(By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and contains(text(), 'Конструктор')]").click()

        string_on_constructor_page = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']"))).text
        assert "Соберите бургер" in string_on_constructor_page

    def test_go_to_logo(self):
        self.driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        self.driver.find_element(By.XPATH,
                                 "//input[@class='text input__textfield text_type_main-default' and @name='name']").send_keys(
            "ebashutest@mail.ru")
        self.driver.find_element(By.XPATH,
                                 "//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys(
            "123456")
        self.driver.find_element(By.XPATH,
                                 "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        string_on_main_page = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']"))).text
        assert "Соберите бургер" in string_on_main_page