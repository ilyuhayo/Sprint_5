import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import StellarBurgersLocators

class TestStellarBurgers:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def teardown_method(self):
        self.driver.quit()

    def test_go_to_sauces_tab(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((StellarBurgersLocators.MAKE_BURGER_CONSTRUCTOR_BACKGROUND))
        )
        self.driver.find_element(*StellarBurgersLocators.SAUCES_TAB).click()
        sauces_header = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((StellarBurgersLocators.SAUCES_CONSTRUCTOR_HEADER)))
        assert "Соусы" in sauces_header.text

    def test_go_to_fillings_tab(self):
        self.driver.find_element(*StellarBurgersLocators.FILLINGS_TAB).click()
        fillings_header = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((StellarBurgersLocators.FILLINGS_CONSTRUCTOR_HEADER)))
        assert "Начинки" in fillings_header.text

    def test_go_to_buns_tabs(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((StellarBurgersLocators.MAKE_BURGER_CONSTRUCTOR_BACKGROUND))
        )
        self.driver.find_element(*StellarBurgersLocators.SAUCES_TAB).click()
        sauces_header = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((StellarBurgersLocators.SAUCES_CONSTRUCTOR_HEADER)))
        assert "Соусы" in sauces_header.text

        self.driver.find_element(*StellarBurgersLocators.BUNS_TAB).click()
        buns_header = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((StellarBurgersLocators.BUNS_CONSTRUCTOR_HEADER)))
        assert "Булки" in buns_header.text