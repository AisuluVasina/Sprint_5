import pytest
from generators import generate_unique_email, generate_password
from locators import RegistrationPageLocators, LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.registration
def test_successful_registration(driver):
    driver.get("https://stellarburgers.education-services.ru/register")
    
    email = generate_unique_email()
    password = generate_password(6)
    
    driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys("Aisylu Vasina")
    driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*RegistrationPageLocators.SUBMIT_BTN).click()
    
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
    assert "login" in driver.current_url, "Не произошел переход на страницу входа"

@pytest.mark.registration
def test_invalid_password_registration(driver):
    driver.get("https://stellarburgers.education-services.ru/register")
    
    email = generate_unique_email()
    # Пароль меньше 6 символов
    password = "12345" 
    
    driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys("Aisylu Vasina")
    driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*RegistrationPageLocators.SUBMIT_BTN).click()
    
    wait = WebDriverWait(driver, 5)
    assert "register" in driver.current_url, "Форма ушла, хотя пароль был неверным"
  