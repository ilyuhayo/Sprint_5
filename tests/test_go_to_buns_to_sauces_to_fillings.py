from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']")))
driver.find_element(By.XPATH, "//div/main/section[1]/div[1]/div[2]").click()
sauces_selector = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"))).text
sauces_header = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][2]"))).text
assert sauces_selector == "Соусы"
assert sauces_header == "Соусы"

driver.find_element(By.XPATH, "//div/main/section[1]/div[1]/div[3]").click()
fillings_selector = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"))).text
fillings_header = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][3]"))).text

assert fillings_selector == "Начинки"
assert fillings_header == "Начинки"


driver.find_element(By.XPATH, "//div/main/section[1]/div[1]/div[1]").click()
buns_selector = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"))).text
buns_header = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10'][1]"))).text

assert buns_selector == "Булки"
assert buns_header == "Булки"

driver.quit()