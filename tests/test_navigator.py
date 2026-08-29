import pytest
from generators import generate_unique_email, generate_password
from locators import MainPageLocators, RegistrationPageLocators, LoginPageLocators, PersonalCabinetLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_user(driver, email, password):
    
    driver.get("https://stellarburgers.education-services.ru/login")
    wait = WebDriverWait(driver, 10)
    
    wait.until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD))
    
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*LoginPageLocators.SUBMIT_BTN).click()
    
    wait.until(EC.url_contains("/profile"))

@pytest.mark.navigation
def test_full_navigation_flow(driver):

    email = generate_unique_email()
    password = generate_password(6)
    wait = WebDriverWait(driver, 10)

    # 1:Регистрация и переход в ЛК 
    
    driver.get("https://stellarburgers.education-services.ru/register")
    wait.until(EC.element_to_be_clickable(RegistrationPageLocators.NAME_FIELD))
    driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys("Aisylu Vasina")
    driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys(password)
    driver.find_element(*RegistrationPageLocators.SUBMIT_BTN).click()
    
    login_user(driver, email, password)

    driver.get("https://stellarburgers.education-services.ru/")
    
    # Кликаем на ссылку «Личный кабинет» на главной
    cab_link = wait.until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_CABINET_LINK))
    cab_link.click()
    
    # Проверяем, что мы попали в профиль
    wait.until(EC.url_contains("/profile"))
    assert "profile" in driver.current_url, "Не удалось перейти в личный кабинет с главной страницы"

    #2: Переход из ЛК в конструктор
    
    constructor_btn = wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.CONSTRUCTOR_LINK))
    constructor_btn.click()
    wait.until(EC.url_contains("/"))
    assert "profile" not in driver.current_url, "Не произошел переход из ЛК в конструктор по кнопке"
    
    # Возвращаемся в ЛК
    driver.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).click()
    wait.until(EC.url_contains("/profile"))

    logo = wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.LOGO_IMG))
    logo.click()
    wait.until(EC.url_contains("/"))
    assert "profile" not in driver.current_url, "Не произошел переход из ЛК в конструктор по логотипу"

    #3: Выход из аккаунта
    
    # Возвращаемся в ЛК для проверки выхода
    driver.find_element(*MainPageLocators.PERSONAL_CABINET_LINK).click()
    wait.until(EC.url_contains("/profile"))
    
    logout_btn = wait.until(EC.element_to_be_clickable(PersonalCabinetLocators.LOGOUT_BTN))
    logout_btn.click()
    
    # Проверяем, что мы на странице логина и кнопка выхода исчезла
    wait.until(EC.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))
    assert "login" in driver.current_url, "Не произошел редирект на страницу входа после выхода"
    
    driver.quit()