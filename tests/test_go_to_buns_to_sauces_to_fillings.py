from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")))
driver.find_element(By.XPATH, "//span[@class='text text_type_main-default' and contains(text(),'Соусы')]").click()
sauces_header = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(@class, 'text text_type_main-medium mb-6 mt-10') and contains(text(), 'Соусы')]")))
assert "Соусы" in sauces_header.text

driver.find_element(By.XPATH, "//span[@class='text text_type_main-default' and contains(text(),'Начинки')]").click()
fillings_header = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//h2[contains(@class, 'text text_type_main-medium mb-6 mt-10') and contains(text(), 'Начинки')]")))
assert "Начинки" in fillings_header.text

driver.find_element(By.XPATH, "//span[@class='text text_type_main-default' and contains(text(),'Булки')]").click()
buns_header = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//h2[contains(@class, 'text text_type_main-medium mb-6 mt-10') and contains(text(), 'Булки')]")))
assert "Булки" in buns_header.text

driver.quit()