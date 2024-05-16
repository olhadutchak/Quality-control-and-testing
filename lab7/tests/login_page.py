# login_page.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CLASS_NAME, "greenStyle")
        self.sign_in_button = (By.CLASS_NAME, 'primary-global-button.btn')

    def login(self, email, password):
        self.driver.get("https://www.greencity.social/#/greenCity")
        start_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.sign_in_button))
        start_button.click()
        email_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.email_input))
        email_input.send_keys(email)
        password_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_input))
        password_input.send_keys(password)
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button))
        login_button.click()

@pytest.fixture(scope="module")
def authenticated_driver():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.login("dutchak.olha.o@chnu.edu.ua", "parolOlha2413!")
    yield driver
    driver.quit()
