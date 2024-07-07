import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators


class TestRegistrationError:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def teardown_method(self):
        self.driver.quit()

    def test_invalid_password(self):
        self.driver.find_element(*StellarBurgersLocators.PERSONAL_AREA_BUTTON).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((StellarBurgersLocators.PAGE_BACKGROUND)))
        self.driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((StellarBurgersLocators.PAGE_BACKGROUND)))
        self.driver.find_element(*StellarBurgersLocators.NAME_FIELD_REG).send_keys(
            "Илья")
        self.driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_REG).send_keys(
            "ebashutest@mail.ru")
        self.driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_REG).send_keys(
            "1")
        self.driver.find_element(*StellarBurgersLocators.BIG_REGISTRATION_BUTTON).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(
            (StellarBurgersLocators.INCORRECT_PASSWORD_MESSAGE)))
        error_message = self.driver.find_element(*StellarBurgersLocators.INCORRECT_PASSWORD_MESSAGE).text
        assert "Некорректный пароль" in error_message