import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarBurgersLocators
from conftest import driver
from urls import STELLAR_BURGERS_URL

class TestAccountFunctionality:
    def test_login_logout(self, driver):
        driver.get(STELLAR_BURGERS_URL)
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((StellarBurgersLocators.LOGIN_BUTTON_MAIN)))
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((StellarBurgersLocators.AUTHORIZATION_FORM_BACKGROUND)))
        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_LOG).send_keys("ebashutest@mail.ru")
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_LOG).send_keys("123456")
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_LOG).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((StellarBurgersLocators.MAKE_BURGER_CONSTRUCTOR_BACKGROUND)))
        driver.find_element(*StellarBurgersLocators.PERSONAL_AREA_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((StellarBurgersLocators.EXIT_BUTTON)))
        driver.find_element(*StellarBurgersLocators.EXIT_BUTTON).click()

        login_text = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((StellarBurgersLocators.LOGIN_FORM_NAME))).text
        assert "Вход" in login_text