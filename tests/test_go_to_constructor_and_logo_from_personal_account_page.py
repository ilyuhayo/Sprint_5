import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators
from conftest import driver
from urls import STELLAR_BURGERS_URL


class TestGoToConstructorAndLogo:
    def test_go_to_constructor(self, driver):
        driver.get(STELLAR_BURGERS_URL)
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((StellarBurgersLocators.LOGIN_BUTTON_MAIN)))
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((StellarBurgersLocators.AUTHORIZATION_FORM_BACKGROUND)))
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_LOG).send_keys("ebashutest@mail.ru")
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_LOG).send_keys("123456")
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_LOG).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((StellarBurgersLocators.PAGE_BACKGROUND_MAIN)))
        driver.find_element(*StellarBurgersLocators.PERSONAL_AREA_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((StellarBurgersLocators.CONSTRUCTOR_BUTTON)))
        driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_BUTTON).click()

        string_on_constructor_page = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((StellarBurgersLocators.MAKE_BURGER_HEADER))).text
        assert "Соберите бургер" in string_on_constructor_page

    def test_go_to_logo(self, driver):
        driver.get(STELLAR_BURGERS_URL)
        driver.find_element(*StellarBurgersLocators.PERSONAL_AREA_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_LOG).send_keys(
            "ebashutest@mail.ru")
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_LOG).send_keys(
            "123456")
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_LOG).click()

        string_on_main_page = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((StellarBurgersLocators.MAKE_BURGER_HEADER))).text
        assert "Соберите бургер" in string_on_main_page