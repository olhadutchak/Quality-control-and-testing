# test_green_city.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login_page import authenticated_driver

class TestGreenCity:
    def test_add_new_habit(self, authenticated_driver):
        driver = authenticated_driver
        search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "create-button")))
        search_button.click()
        add_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".primary-global-button.m-btn")))
        add_button.click()
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "app-one-habit")))
        habit_elements = driver.find_elements(By.CSS_SELECTOR, "app-one-habit")
        assert len(habit_elements) > 0

    def test_remove_added_habit(self, authenticated_driver):
        driver = authenticated_driver
        habit_edit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.edit.undone"))
        )
        habit_edit_button.click()
        surrender_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.tertiary-global-button.habit-btn"))
        )
        surrender_button.click()
        confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.m-btn.primary-global-button"))
        )
        confirm_button.click()
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, "app-one-habit"))
        )
        habit_elements = driver.find_elements(By.CSS_SELECTOR, "app-one-habit")
        assert len(habit_elements) == 0
