import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from locators import StellarBurgersLocators


class TestRegistration:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.fake = Faker()
        self.unique_email = self.fake.email()

    def teardown_method(self):
        self.driver.quit()

    def test_registration_with_unique_email(self):
        self.driver.find_element(*StellarBurgersLocators.PERSONAL_AREA_BUTTON).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((StellarBurgersLocators.PAGE_BACKGROUND)))
        self.driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((StellarBurgersLocators.PAGE_BACKGROUND)))
        self.driver.find_element(*StellarBurgersLocators.NAME_FIELD_REG).send_keys(
            "Илья")
        self.driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_REG).send_keys(
            self.unique_email)
        self.driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_REG).send_keys(
            "123456")
        self.driver.find_element(*StellarBurgersLocators.BIG_REGISTRATION_BUTTON).click()

        login_header = WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((StellarBurgersLocators.LOGIN_FORM_NAME)))  # Добавлена закрывающая скобка
        assert "Вход" in login_header.text