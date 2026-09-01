import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators
from config import MAIN_URL, LOGIN_URL, REGISTER_URL

WAIT_TIMEOUT = 10

def wait_for_element_clickable(driver, locator):
    # Ожидание кликабельности элемента
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    return wait.until(EC.element_to_be_clickable(locator))

def wait_for_url_to_be(driver, expected_url):
    # Ожидание полного совпадения URL
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    wait.until(EC.url_to_be(expected_url))

def wait_for_url_contains(driver, substring):
    # Ожидание подстроки в URL
    wait = WebDriverWait(driver, WAIT_TIMEOUT)
    wait.until(lambda d: substring in d.current_url)

def close_modal_if_present(driver):

    try:
        # Ждём, пока оверлей модалки появится (или таймаут пройдёт — тогда except)
        overlay = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(MainPageLocators.MODAL_OVERLAY)
        )
        # Сначала пробуем найти кнопку закрытия (крестик)
        try:
            close_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(MainPageLocators.MODAL_CLOSE_BUTTON)
            )
            close_btn.click()
        except:
            # Если крестика нет — кликаем по оверлею (фону)
            driver.execute_script("arguments[0].click();", overlay)
        # Ждём, пока модалка исчезнет
        WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(MainPageLocators.MODAL_OVERLAY))
    except:
        # Если модалки не было — просто продолжаем
        pass

class TestLoginScenarios:

    def test_login_via_main_page_button(self, driver, registered_user):
            # 1: Вход через кнопку «Войти в аккаунт»
            email, password = registered_user
            driver.get(MAIN_URL)
            close_modal_if_present(driver) 
    
            # Находим и кликаем кнопку входа
            login_btn = wait_for_element_clickable(driver, MainPageLocators.LOGIN_BTN_MAIN)
            login_btn.click()
    
            # Ждем перехода на страницу логина
            wait_for_url_contains(driver, "/login")
    
            # Вводим Email
            email_field = wait_for_element_clickable(driver, LoginPageLocators.EMAIL_FIELD)
            email_field.clear()
            email_field.send_keys(email)
    
            # Вводим Пароль
            password_field = wait_for_element_clickable(driver, LoginPageLocators.PASSWORD_FIELD)
            password_field.clear()
            password_field.send_keys(password)
    
            # Нажимаем кнопку "Войти"
            submit_btn = wait_for_element_clickable(driver, LoginPageLocators.SUBMIT_BTN)
            submit_btn.click()

            wait_for_url_to_be(driver, MAIN_URL)
    
    def test_login_via_personal_cabinet_link(self, driver, registered_user):
          #Вход через ссылку «Личный кабинет»."""
          email, password = registered_user
          
          # Переходим на главную страницу
          driver.get(MAIN_URL)
          close_modal_if_present(driver)
  
          # Находим и кликаем ссылку "Личный кабинет"
          cabinet_link = wait_for_element_clickable(driver, MainPageLocators.PERSONAL_CABINET_LINK)
          cabinet_link.click()
  
          # Ждем перехода на страницу логина
          wait_for_url_contains(driver, "/login")
          close_modal_if_present(driver) # Проверяем модалку и на странице логина
  
          # Вводим данные и логинимся
          email_field = wait_for_element_clickable(driver, LoginPageLocators.EMAIL_FIELD)
          email_field.clear()
          email_field.send_keys(email)
  
          password_field = wait_for_element_clickable(driver, LoginPageLocators.PASSWORD_FIELD)
          password_field.clear()
          password_field.send_keys(password)
  
          submit_btn = wait_for_element_clickable(driver, LoginPageLocators.SUBMIT_BTN)
          submit_btn.click()
  
          # Ждем возврата на главную страницу (это подтверждает успешный вход)
          wait_for_url_to_be(driver, MAIN_URL)

    def test_login_via_registration_form_link(self, driver, registered_user):
        #Вход через ссылку в форме регистрации.
        email, password = registered_user
        driver.get(REGISTER_URL)
        close_modal_if_present(driver)
    
        login_link_in_reg = wait_for_element_clickable(driver, RegistrationPageLocators.LOGIN_LINK_IN_REG)
        login_link_in_reg.click()
    
        # Ждем перехода на страницу логина
        wait_for_url_contains(driver, "/login")
        close_modal_if_present(driver) # Проверяем модалку и на странице логина
    
        email_field = wait_for_element_clickable(driver, LoginPageLocators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(email)
    
        password_field = wait_for_element_clickable(driver, LoginPageLocators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)
    
        submit_btn = wait_for_element_clickable(driver, LoginPageLocators.SUBMIT_BTN)
        submit_btn.click()
    
        # Ждем возврата на главную страницу (это подтверждает успешный вход)
        wait_for_url_to_be(driver, MAIN_URL)

    def test_login_via_forgot_password_link(self, driver, registered_user):
        #Вход через ссылку в форме восстановления пароля
        email, password = registered_user
        driver.get(LOGIN_URL)
        close_modal_if_present(driver)
    
        forgot_link = wait_for_element_clickable(driver, LoginPageLocators.FORGOT_PASSWORD_LINK)
        forgot_link.click()
    
        wait_for_url_contains(driver, "/forgot-password")
        close_modal_if_present(driver)
    
        back_to_login = wait_for_element_clickable(driver, LoginPageLocators.BACK_TO_LOGIN_LINK)
        back_to_login.click()
    
        wait_for_url_contains(driver, "/login")
    
        email_field = wait_for_element_clickable(driver, LoginPageLocators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(email)
            
        password_field = wait_for_element_clickable(driver, LoginPageLocators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)
    
        submit_btn = wait_for_element_clickable(driver, LoginPageLocators.SUBMIT_BTN)
        submit_btn.click()
            
        wait_for_url_to_be(driver, MAIN_URL)