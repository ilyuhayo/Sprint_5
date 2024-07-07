import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators

class TestGoToConstructorAndLogo:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def teardown_method(self):
        self.driver.quit()

    def test_go_to_constructor(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((StellarBurgersLocators.LOGIN_BUTTON_MAIN)))
        self.driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((StellarBurgersLocators.AUTHORIZATION_FORM_BACKGROUND)))
        self.driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_LOG).send_keys("ebashutest@mail.ru")
        self.driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_LOG).send_keys("123456")
        self.driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_LOG).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((StellarBurgersLocators.PAGE_BACKGROUND_MAIN)))
        self.driver.find_element(*StellarBurgersLocators.PERSONAL_AREA_BUTTON).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((StellarBurgersLocators.CONSTRUCTOR_BUTTON)))
        self.driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_BUTTON).click()

        string_on_constructor_page = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((StellarBurgersLocators.MAKE_BURGER_HEADER))).text
        assert "Соберите бургер" in string_on_constructor_page

    def test_go_to_logo(self):
        self.driver.find_element(*StellarBurgersLocators.PERSONAL_AREA_BUTTON).click()
        self.driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_LOG).send_keys(
            "ebashutest@mail.ru")
        self.driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_LOG).send_keys(
            "123456")
        self.driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_LOG).click()

        string_on_main_page = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((StellarBurgersLocators.MAKE_BURGER_HEADER))).text
        assert "Соберите бургер" in string_on_main_page