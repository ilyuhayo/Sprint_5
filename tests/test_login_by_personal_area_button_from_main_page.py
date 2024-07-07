import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators


class TestLoginByPersonalAreaButton:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def teardown_method(self):
        self.driver.quit()

    def test_login_by_personal_area(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(
            (StellarBurgersLocators.PERSONAL_AREA_BUTTON)))
        self.driver.find_element(*StellarBurgersLocators.PERSONAL_AREA_BUTTON).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((StellarBurgersLocators.AUTHORIZATION_FORM_BACKGROUND)))
        self.driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_LOG).send_keys(
            "ebashutest@mail.ru")
        self.driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_LOG).send_keys(
            "123456")
        self.driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_LOG).click()

        make_order_button = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((StellarBurgersLocators.CHECKOUT_BUTTON))).text
        assert "Оформить заказ" in make_order_button
