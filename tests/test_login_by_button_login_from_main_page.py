from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")))
driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg").click()
WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".Auth_login__3hAey")))
driver.find_element(By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='name']").send_keys("ilya_zolotov_10_555@yandex.ru")
driver.find_element(By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys("123456")
driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

driver.quit()

