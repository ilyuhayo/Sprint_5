import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import StellarBurgersLocators
from conftest import driver
from urls import STELLAR_BURGERS_URL


class TestStellarBurgers:
    def test_go_to_sauces_tab(self, driver):
        driver.get(STELLAR_BURGERS_URL)
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((StellarBurgersLocators.MAKE_BURGER_CONSTRUCTOR_BACKGROUND))
        )
        driver.find_element(*StellarBurgersLocators.SAUCES_TAB).click()
        sauces_header = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((StellarBurgersLocators.SAUCES_CONSTRUCTOR_HEADER)))
        assert "Соусы" in sauces_header.text

    def test_go_to_fillings_tab(self, driver):
        driver.get(STELLAR_BURGERS_URL)
        driver.find_element(*StellarBurgersLocators.FILLINGS_TAB).click()
        fillings_header = WebDriverWait(driver, 5).until(EC.presence_of_element_located((StellarBurgersLocators.FILLINGS_CONSTRUCTOR_HEADER)))
        assert "Начинки" in fillings_header.text

    def test_go_to_buns_tabs(self, driver):
        driver.get(STELLAR_BURGERS_URL)
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((StellarBurgersLocators.MAKE_BURGER_CONSTRUCTOR_BACKGROUND))
        )
        driver.find_element(*StellarBurgersLocators.SAUCES_TAB).click()
        sauces_header = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((StellarBurgersLocators.SAUCES_CONSTRUCTOR_HEADER)))
        assert "Соусы" in sauces_header.text

        driver.find_element(*StellarBurgersLocators.BUNS_TAB).click()
        buns_header = WebDriverWait(driver, 5).until(EC.presence_of_element_located((StellarBurgersLocators.BUNS_CONSTRUCTOR_HEADER)))
        assert "Булки" in buns_header.text