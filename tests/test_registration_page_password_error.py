import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators
from conftest import driver
from urls import STELLAR_BURGERS_URL


class TestRegistrationError:
    def test_invalid_password(self, driver):
        driver.get(STELLAR_BURGERS_URL)
        driver.find_element(*StellarBurgersLocators.PERSONAL_AREA_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((StellarBurgersLocators.PAGE_BACKGROUND)))
        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((StellarBurgersLocators.PAGE_BACKGROUND)))
        driver.find_element(*StellarBurgersLocators.NAME_FIELD_REG).send_keys(
            "Илья")
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_REG).send_keys(
            "ebashutest@mail.ru")
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_REG).send_keys(
            "1")
        driver.find_element(*StellarBurgersLocators.BIG_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (StellarBurgersLocators.INCORRECT_PASSWORD_MESSAGE)))
        error_message = driver.find_element(*StellarBurgersLocators.INCORRECT_PASSWORD_MESSAGE).text
        assert "Некорректный пароль" in error_message