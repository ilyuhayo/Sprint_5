import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators
from conftest import driver
from urls import STELLAR_BURGERS_URL


class TestLoginFromRegPage:
    def test_login_from_reg(self, driver):
        driver.get(STELLAR_BURGERS_URL)
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(
            (StellarBurgersLocators.PERSONAL_AREA_BUTTON)))
        driver.find_element(*StellarBurgersLocators.PERSONAL_AREA_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(
            (StellarBurgersLocators.REGISTRATION_BUTTON)))
        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(
            (StellarBurgersLocators.LOGIN_BUTTON_REG)))
        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_REG).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((StellarBurgersLocators.AUTHORIZATION_FORM_BACKGROUND)))

        driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_LOG).send_keys(
            "ebashutest@mail.ru")
        driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_LOG).send_keys(
            "123456")

        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_LOG).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.presence_of_element_located((StellarBurgersLocators.PAGE_BACKGROUND)))

        make_order_button = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((StellarBurgersLocators.CHECKOUT_BUTTON))).text
        assert "Оформить заказ" in make_order_button
