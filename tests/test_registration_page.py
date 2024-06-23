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
driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input[contains(@class, 'text input__textfield text_type_main-default')]").send_keys("ilya_zolotov_10_555@yandex.ru")
driver.find_element(By.XPATH, "//div//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys("123456")
driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa")))
driver.quit()
