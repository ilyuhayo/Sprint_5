from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLoginFromRecPage:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def teardown_method(self):
        self.driver.quit()

    def test_login_from_recovery(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']")))
        self.driver.find_element(By.XPATH,
                                 "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']").click()

        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']")))
        self.driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']").click()

        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Войти']")))
        self.driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Войти']").click()

        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']")))

        self.driver.find_element(By.XPATH,
                                 "//input[@class='text input__textfield text_type_main-default' and @name='name']").send_keys(
            "ebashutest@mail.ru")
        self.driver.find_element(By.XPATH,
                                 "//input[@class='text input__textfield text_type_main-default' and @name='Пароль']").send_keys(
            "123456")
        self.driver.find_element(By.XPATH,
                                 "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "App_componentContainer__2JC2W")))
        make_order_button = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']"))).text
        assert "Оформить заказ" in make_order_button