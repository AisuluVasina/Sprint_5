import pytest
from generators import generate_unique_email, generate_password
from locators import RegistrationPageLocators, LoginPageLocators, MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def register_user(driver, email, password):
    driver.get("https://stellarburgers.education-services.ru/register")
    driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys("Aisylu Vasina")
    driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*RegistrationPageLocators.SUBMIT_BTN).click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))

@pytest.mark.login
def test_login_from_main_page(driver):
    #Вход по кнопке «Войти в аккаунт»
    email = generate_unique_email()
    password = generate_password(6)
    
    register_user(driver, email, password)
    
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*MainPageLocators.LOGIN_BTN_MAIN).click()
    
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
    
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*LoginPageLocators.SUBMIT_BTN).click()
    
    wait.until(EC.url_contains("/profile"))
    assert "profile" in driver.current_url, "Не удалось войти через главную страницу"

@pytest.mark.login
def test_login_from_personal_cabinet_link(driver):
    #Вход через кнопку «Личный кабинет»
    email = generate_unique_email()
    password = generate_password(6)
    
    register_user(driver, email, password)
    
    driver.get("https://stellarburgers.education-services.ru/")
    driver.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).click()
    
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
    
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*LoginPageLocators.SUBMIT_BTN).click()

@pytest.mark.login
def test_login_from_registration_form(driver):
    #Вход через кнопку в форме регистрации
    email = generate_unique_email()
    password = generate_password(6)
    register_user(driver, email, password)
    
    driver.get("https://stellarburgers.education-services.ru/register")
    
    wait = WebDriverWait(driver, 10)
    login_link_in_reg = wait.until(EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK_IN_REG))
    login_link_in_reg.click()
    
    wait.until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
    
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*LoginPageLocators.SUBMIT_BTN).click()

    wait.until(EC.url_contains("/profile"))
    assert "profile" in driver.current_url, "Не удалось войти через форму регистрации"

@pytest.mark.login
def test_login_from_forgot_password_form(driver):
    #Вход через кнопку в форме восстановления пароля
    email = generate_unique_email()
    password = generate_password(6)
    register_user(driver, email, password)
    
    driver.get("https://stellarburgers.education-services.ru/login")
    
    wait = WebDriverWait(driver, 10)
    forgot_pass_link = wait.until(EC.element_to_be_clickable(LoginPageLocators.FORGOT_PASSWORD_LINK))
    forgot_pass_link.click()
    
    back_to_login_link = wait.until(EC.element_to_be_clickable(LoginPageLocators.BACK_TO_LOGIN_LINK))
    back_to_login_link.click()
    
    wait.until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
    
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*LoginPageLocators.SUBMIT_BTN).click()
    
    wait.until(EC.url_contains("/profile"))
    assert "profile" in driver.current_url, "Не удалось войти через форму восстановления пароля"

    wait.until(EC.url_contains("/profile"))

    driver.quit()