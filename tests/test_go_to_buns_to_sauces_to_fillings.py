import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestStellarBurgers:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def teardown_method(self):
        self.driver.quit()

    def test_login_and_navigation(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2"))
        )
        self.driver.find_element(By.XPATH,
                                 "//span[@class='text text_type_main-default' and contains(text(),'Соусы')]").click()
        sauces_header = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,
                                                                                              "//h2[contains(@class, 'text text_type_main-medium mb-6 mt-10') and contains(text(), 'Соусы')]")))
        assert "Соусы" in sauces_header.text

        self.driver.find_element(By.XPATH,
                                 "//span[@class='text text_type_main-default' and contains(text(),'Начинки')]").click()
        fillings_header = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                                              "//h2[contains(@class, 'text text_type_main-medium mb-6 mt-10') and contains(text(), 'Начинки')]")))
        assert "Начинки" in fillings_header.text

        self.driver.find_element(By.XPATH,
                                 "//span[@class='text text_type_main-default' and contains(text(),'Булки')]").click()
        buns_header = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                                          "//h2[contains(@class, 'text text_type_main-medium mb-6 mt-10') and contains(text(), 'Булки')]")))
        assert "Булки" in buns_header.text