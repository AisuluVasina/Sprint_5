import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators
from config import MAIN_URL, LOGIN_URL, REGISTER_URL
from conftest import close_modal_if_present  # Импортируем функцию из conftest

WAIT_TIMEOUT = 10

class TestLoginScenarios:

    def test_login_via_main_page_button(self, driver, registered_user):
        #Вход через кнопку «Войти в аккаунт» на главной странице
        email, password = registered_user
        driver.get(MAIN_URL)
        close_modal_if_present(driver)

        # Кликаем «Войти в аккаунт»
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BTN_MAIN)
        ).click()

        # Ждём перехода на /login
        WebDriverWait(driver, 10).until(
            lambda d: "/login" in d.current_url
        )

        # Вводим email
        email_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD)
        )
        email_field.clear()
        email_field.send_keys(email)

        # Вводим пароль
        password_field = driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)

        # Нажимаем «Войти»
        driver.find_element(*LoginPageLocators.SUBMIT_BTN).click()

        # Ждём перехода на главную
        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))
        assert driver.current_url == MAIN_URL, "Не произошёл редирект на главную страницу после входа"

    def test_login_via_personal_cabinet_link(self, driver, registered_user):
        #Вход через ссылку «Личный кабинет»
        email, password = registered_user
        driver.get(MAIN_URL)
        close_modal_if_present(driver)

        # Кликаем «Личный кабинет»
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_LINK)
        ).click()

        # Ждём /login
        WebDriverWait(driver, 10).until(
            lambda d: "/login" in d.current_url
        )
        close_modal_if_present(driver)

        # Вводим данные
        email_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD)
        )
        email_field.clear()
        email_field.send_keys(email)

        password_field = driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)

        driver.find_element(*LoginPageLocators.SUBMIT_BTN).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))
        assert driver.current_url == MAIN_URL, "Не произошёл редирект на главную страницу после входа"

    def test_login_via_registration_form_link(self, driver, registered_user):
        #Вход через ссылку «Войти» на странице регистрации
        email, password = registered_user
        driver.get(REGISTER_URL)
        close_modal_if_present(driver)

        # Кликаем «Войти»
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK_IN_REG)
        ).click()

        # Ждём /login
        WebDriverWait(driver, 10).until(
            lambda d: "/login" in d.current_url
        )
        close_modal_if_present(driver)

        # Вводим данные
        email_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD)
        )
        email_field.clear()
        email_field.send_keys(email)

        password_field = driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)

        driver.find_element(*LoginPageLocators.SUBMIT_BTN).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))
        assert driver.current_url == MAIN_URL, "Не произошёл редирект на главную страницу после входа"

    def test_login_via_forgot_password_link(self, driver, registered_user):
        #Вход через «Вернуться к логину» на странице восстановления пароля
        email, password = registered_user
        driver.get(LOGIN_URL)
        close_modal_if_present(driver)

        # Кликаем «Забыли пароль?»
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.FORGOT_PASSWORD_LINK)
        ).click()

        # Ждём /forgot-password
        WebDriverWait(driver, 10).until(
            lambda d: "/forgot-password" in d.current_url
        )
        close_modal_if_present(driver)

        # Кликаем «Вернуться к логину»
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.BACK_TO_LOGIN_LINK)
        ).click()

        # Ждём /login
        WebDriverWait(driver, 10).until(
            lambda d: "/login" in d.current_url
        )

        # Вводим данные
        email_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD)
        )
        email_field.clear()
        email_field.send_keys(email)

        password_field = driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)

        driver.find_element(*LoginPageLocators.SUBMIT_BTN).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(MAIN_URL))
        assert driver.current_url == MAIN_URL, "Не произошёл редирект на главную страницу после входа"