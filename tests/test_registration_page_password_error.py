import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistrationError:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def teardown_method(self):
        self.driver.quit()

    def test_invalid_password(self):
        self.driver.find_element(By.XPATH,
                                 "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']").click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        self.driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Зарегистрироваться']").click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        self.driver.find_element(By.XPATH,
                                 "//label[contains(text(), 'Имя')]/following-sibling::input[contains(@class, 'text_type_main-default')]").send_keys(
            "Илья")
        self.driver.find_element(By.XPATH,
                                 "//label[text()='Email']/following-sibling::input[contains(@class, 'text input__textfield text_type_main-default')]").send_keys(
            "ebashutest@mail.ru")
        self.driver.find_element(By.XPATH,
                                 "//div//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys(
            "1")
        self.driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//p[@class='input__error text_type_main-default']")))
        error_message = self.driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']").text
        assert "Некорректный пароль" in error_message