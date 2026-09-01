import pytest
from config import MAIN_URL 
from locators import ConstructorLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import close_modal_if_present, safe_click 

class TestConstructorTabs:
    
    def test_buns_tab_navigation(self, driver):
        # Переход из раздела Начинки в раздел Булки
        driver.get(MAIN_URL)
        wait = WebDriverWait(driver, 10)
        close_modal_if_present(driver)

        # Переходим в Начинки
        safe_click(driver, ConstructorLocators.TOPPINGS_TAB)
        wait.until(EC.visibility_of_element_located(ConstructorLocators.FIRST_TOPPING))

        # Переходим в Булки
        safe_click(driver, ConstructorLocators.BUNS_TAB)
        wait.until(EC.visibility_of_element_located(ConstructorLocators.FIRST_BUN))
        
        # Проверка
        assert "Булки" in driver.page_source, "Не удалось подтвердить переход в раздел Булки"
 
    def test_sauces_tab_navigation(self, driver):
        # Переход на вкладку 'Соусы' 
        driver.get(MAIN_URL)
        wait = WebDriverWait(driver, 10)

        close_modal_if_present(driver)

        # Кликаем по вкладке "Соусы"
        safe_click(driver, ConstructorLocators.SAUCES_TAB)

        # Проверка: Ждем появления карточки первого соуса 
        wait.until(EC.visibility_of_element_located(ConstructorLocators.FIRST_SAUCE))

        tab_element = driver.find_element(*ConstructorLocators.SAUCES_TAB)
        assert tab_element.text.strip() == "Соусы", f"Ожидался текст 'Начинки', найдено: '{tab_element.text}'"

    def test_toppings_tab_navigation(self, driver):
        # Переход в раздел "Начинки"
        driver.get(MAIN_URL)
        wait = WebDriverWait(driver, 10)

        close_modal_if_present(driver)

        safe_click(driver, ConstructorLocators.TOPPINGS_TAB)

        toppings_tab = wait.until(EC.element_to_be_clickable(ConstructorLocators.TOPPINGS_TAB))
        toppings_tab.click()

        # Проверка появление первого элемента
        wait.until(EC.visibility_of_element_located(ConstructorLocators.FIRST_TOPPING))

        tab_element = driver.find_element(*ConstructorLocators.TOPPINGS_TAB)
        assert tab_element.text.strip() == "Начинки", f"Ожидался текст 'Начинки', найдено: '{tab_element.text}'"