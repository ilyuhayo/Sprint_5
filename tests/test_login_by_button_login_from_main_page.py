from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import StellarBurgersLocators


class TestLoginFromMainPage:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def teardown_method(self):
        self.driver.quit()

    def test_login_from_main_page(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((StellarBurgersLocators.LOGIN_BUTTON_MAIN)))
        self.driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()

        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((StellarBurgersLocators.AUTHORIZATION_FORM_BACKGROUND)))
        self.driver.find_element(*StellarBurgersLocators.EMAIL_FIELD_LOG).send_keys(
            "ebashutest@mail.ru")
        self.driver.find_element(*StellarBurgersLocators.PASSWORD_FIELD_LOG).send_keys(
            "123456")
        self.driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_LOG).click()

        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((StellarBurgersLocators.PAGE_BACKGROUND)))
        make_order_button = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((StellarBurgersLocators.CHECKOUT_BUTTON))).text
        assert "Оформить заказ" in make_order_button