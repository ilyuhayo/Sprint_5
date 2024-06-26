import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker


class TestRegistration:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.fake = Faker()
        self.unique_email = self.fake.email()

    def teardown_method(self):
        self.driver.quit()

    def test_registration_with_unique_email(self):
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
            self.unique_email)
        self.driver.find_element(By.XPATH,
                                 "//div//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys(
            "123456")
        self.driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

        login_header = WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//h2[text()='Вход']")))  # Добавлена закрывающая скобка
        assert "Вход" in login_header.text