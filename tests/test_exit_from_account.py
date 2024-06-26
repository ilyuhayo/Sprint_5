from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']")))
driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']")))
driver.find_element(By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='name']").send_keys("ebashutest@mail.ru")
driver.find_element(By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys("123456")
driver.find_element(By.XPATH, "//button[text()='Войти']").click()
WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']")))
driver.find_element(By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and contains(@href, '/account')]").click()
WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Выход']")))
driver.find_element(By.XPATH, "//button[text()='Выход']").click()

login_text = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, "//h2[text()='Вход']"))).text
assert "Вход" in login_text

driver.quit()


























