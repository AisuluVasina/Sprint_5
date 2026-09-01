import pytest
from config import REGISTER_URL
from selenium import webdriver
from generators import generate_unique_email, generate_password
from locators import RegistrationPageLocators, LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver

class TestRegistration:
    
    def test_successful_registration(self, driver):
        driver.get(REGISTER_URL)
        
        email = generate_unique_email()
        password = generate_password(6)
        
        driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys("Aisylu Vasina")
        driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*RegistrationPageLocators.SUBMIT_BTN).click()
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
        
        assert driver.find_element(*LoginPageLocators.EMAIL_FIELD).is_displayed(), \
            "Поле ввода email формы входа не отобразилось после регистрации"
        
    def test_invalid_password_registration(self, driver):
        driver.get(REGISTER_URL)
        
        email = generate_unique_email()
        # Пароль меньше 6 символов
        password = "12345" 
        
        driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys("Aisylu Vasina")
        driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*RegistrationPageLocators.SUBMIT_BTN).click()
        
        wait = WebDriverWait(driver, 5)

        assert driver.find_element(*RegistrationPageLocators.NAME_FIELD).is_displayed(), \
            "Форма регистрации исчезла, хотя пароль был неверным"
  