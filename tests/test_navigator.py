import time
import pytest
from config import REGISTER_URL, MAIN_URL, LOGIN_URL, PROFILE_URL 
from generators import generate_unique_email, generate_password
from locators import RegistrationPageLocators, LoginPageLocators, MainPageLocators, PersonalCabinetLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Убран импорт 'driver' из conftest! Он передается в тест автоматически.
from conftest import close_modal_if_present, registered_user 

class TestRegistration:
    
    def test_navigate_to_personal_cabinet_as_guest(self, driver, registered_user):
        #Вход существующего пользователя и переход в личный кабинет.
        driver.get(MAIN_URL)
        close_modal_if_present(driver)

        wait = WebDriverWait(driver, 15)

        # Клик по кнопке ЛК
        profile_btn = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_LINK))
        profile_btn.click()

        # Ожидание и заполнение формы входа
        email_field_locator = LoginPageLocators.EMAIL_FIELD
        wait.until(EC.visibility_of_element_located(email_field_locator))

        email, password = registered_user

        email_field = wait.until(EC.element_to_be_clickable(email_field_locator))
        email_field.clear()
        email_field.send_keys(email)

        password_field = wait.until(EC.element_to_be_clickable(LoginPageLocators.PASSWORD_FIELD))
        password_field.clear()
        password_field.send_keys(password)

        submit_btn = wait.until(EC.element_to_be_clickable(LoginPageLocators.SUBMIT_BTN))
        submit_btn.click()

        wait.until(EC.url_to_be(MAIN_URL))
        print(">>> УСПЕХ: Вход выполнен, находимся на главной странице.")

        # Ещё раз кликаем по Личному кабинету
        profile_btn_after_login = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_LINK))
        profile_btn_after_login.click()

        # ПРОВЕРКА
        try:
            wait.until(EC.url_to_be(PROFILE_URL))
            print(">>> УСПЕХ: Переход в личный кабинет подтверждён!")
        except Exception as e:
            driver.save_screenshot("profile_navigation_failed.png")
            raise AssertionError(f"Не удалось перейти в личный кабинет. Текущий URL: {driver.current_url}") from e

    def test_navigate_to_constructor_from_cabinet_by_button(self, driver, logged_in_user):
        #Переход из ЛК в конструктор.

        driver.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).click()

        # Ждём загрузки страницы профиля
        WebDriverWait(driver, 15).until(EC.url_to_be(PROFILE_URL))

        #Закрываем модальное окно
        close_modal_if_present(driver)
        
        # кликаем по "Конструктор"
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_LINK))
        driver.find_element(*MainPageLocators.CONSTRUCTOR_LINK).click()

        # Ждём возврата на главную
        WebDriverWait(driver, 15).until(EC.url_to_be(MAIN_URL))

        # Проверяем заголовок
        assert driver.find_element(*MainPageLocators.BUN_HEADER).is_displayed(), \
            "Не вернулись в конструктор: заголовок 'Соберите бургер' не отображается"

    def test_navigate_to_constructor_from_cabinet_by_logo(self, driver, logged_in_user):
        # Клик по логотипу
        driver.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).click()

        # Ждём загрузки страницы профиля
        WebDriverWait(driver, 15).until(EC.url_to_be(PROFILE_URL))

        close_modal_if_present(driver)

        # Кликаем по логотипу
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(MainPageLocators.LOGO_IMG))
        driver.find_element(*MainPageLocators.LOGO_IMG).click()

        # Ждём возврата на главную
        WebDriverWait(driver, 15).until(EC.url_to_be(MAIN_URL))

        # Проверяем заголовок
        assert driver.find_element(*MainPageLocators.BUN_HEADER).is_displayed(), \
            "Не вернулись в конструктор: заголовок 'Соберите бургер' не отображается"

    def test_logout_user(self, driver, logged_in_user):
        # Выход по кнопке «Выйти» в личном кабинете.
        driver.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).click()

        WebDriverWait(driver, 15).until(EC.url_to_be(PROFILE_URL))

        close_modal_if_present(driver)

        # Находим кнопку выхода и ждём, пока она станет кликабельна
        logout_btn = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(PersonalCabinetLocators.LOGOUT_BTN)
        )

        # Клик по кнопке выхода
        driver.execute_script("arguments[0].click();", logout_btn)
        print("Клик по кнопке 'Выйти' выполнен через JS.")

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD)
        )

        # Проверка
        assert "login" in driver.current_url, "Не произошел редирект на страницу входа после выхода"
        print("Тест пройден: успешный выход из аккаунта.")