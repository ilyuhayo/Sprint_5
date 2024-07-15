import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from locators import StellarBurgersLocators
from conftest import driver
from urls import STELLAR_BURGERS_URL


class TestRegistration:
    def setup_method(self):
        self.fake = Faker()
        self.unique_email = self.fake.email()
    def test_registration_with_unique_email(self, driver):
        driver.get(STELLAR_BURGERS_URL)
        driver.find_element(*StellarBurgersLocators.PERSONAL_AREA_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((StellarBurgersLocators.PAGE_BACKGROUND)))
        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((StellarBurgersLocators.PAGE_BACKGROUND)))
        driver.find_element(*StellarBurgersLocators.NAME_FIELD_REG).send_keys(
            "Илья")
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_REG).send_keys(self.unique_email)
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_REG).send_keys(
            "123456")
        driver.find_element(*StellarBurgersLocators.BIG_REGISTRATION_BUTTON).click()

        login_header = WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((StellarBurgersLocators.LOGIN_FORM_NAME)))  # Добавлена закрывающая скобка
        assert "Вход" in login_header.text