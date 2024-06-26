from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class TestGoToPersonalAccount:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def teardown_method(self):
        self.driver.quit()

    def test_go_to_personal_account(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH,
                                                                                    "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")))
        self.driver.find_element(By.XPATH,
                            "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
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
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(
            (By.XPATH, "//main[@class='App_componentContainer__2JC2W']")))
        self.driver.find_element(By.XPATH,
                            "//a[@class='AppHeader_header__link__3D_hX' and contains(@href, '/account')]").click()
        profile_string = WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH,
                                                                                                     "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']"))).text
        assert "Профиль" in profile_string
