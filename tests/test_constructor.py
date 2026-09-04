import pytest
from config import MAIN_URL
from locators import ConstructorLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import close_modal_if_present, safe_click

class TestConstructorTabs:

    def test_buns_tab_navigation(self, driver):
        driver.get(MAIN_URL)
        wait = WebDriverWait(driver, 10)
        close_modal_if_present(driver)

        # Переходим в Начинки
        safe_click(driver, ConstructorLocators.TOPPINGS_TAB)
        wait.until(EC.visibility_of_element_located(ConstructorLocators.FIRST_TOPPING))

        # Переходим в Булки
        safe_click(driver, ConstructorLocators.BUNS_TAB)
        wait.until(EC.visibility_of_element_located(ConstructorLocators.FIRST_BUN))

        # ПРОВЕРКА: активная вкладка имеет класс tab_tab_type_current
        buns_element = driver.find_element(*ConstructorLocators.BUNS_TAB)
        wait.until(lambda d: "tab_tab_type_current" in buns_element.get_attribute("class"))
        
        # Класс появился — тест пройден
        assert "tab_tab_type_current" in buns_element.get_attribute("class")

    def test_sauces_tab_navigation(self, driver):
        driver.get(MAIN_URL)
        wait = WebDriverWait(driver, 10)
        close_modal_if_present(driver)

        safe_click(driver, ConstructorLocators.SAUCES_TAB)
        wait.until(EC.visibility_of_element_located(ConstructorLocators.FIRST_SAUCE))

        # ПРОВЕРКА: активная вкладка имеет класс tab_tab_type_current
        sauces_element = driver.find_element(*ConstructorLocators.SAUCES_TAB)
        wait.until(lambda d: "tab_tab_type_current" in sauces_element.get_attribute("class"))
        
        assert "tab_tab_type_current" in sauces_element.get_attribute("class")

    def test_toppings_tab_navigation(self, driver):
        driver.get(MAIN_URL)
        wait = WebDriverWait(driver, 10)
        close_modal_if_present(driver)

        safe_click(driver, ConstructorLocators.TOPPINGS_TAB)
        wait.until(EC.visibility_of_element_located(ConstructorLocators.FIRST_TOPPING))

        # ПРОВЕРКА: активная вкладка имеет класс tab_tab_type_current
        toppings_element = driver.find_element(*ConstructorLocators.TOPPINGS_TAB)
        wait.until(lambda d: "tab_tab_type_current" in toppings_element.get_attribute("class"))
        
        assert "tab_tab_type_current" in toppings_element.get_attribute("class")