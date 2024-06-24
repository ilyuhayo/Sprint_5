from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")


driver.find_element(By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']").click()
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Зарегистрироваться']").click()
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
driver.find_element(By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input[contains(@class, 'text_type_main-default')]").send_keys("Илья")
driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input[contains(@class, 'text input__textfield text_type_main-default')]").send_keys("ebashutest@mail.ru")
driver.find_element(By.XPATH, "//div//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys("1")
driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[@class='input__error text_type_main-default']")))
error_message = driver.find_element(By.XPATH, "//p[@class='input__error text_type_main-default']").text

assert "Некорректный пароль" in error_message

driver.quit()
