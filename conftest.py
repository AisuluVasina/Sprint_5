import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import RegistrationPageLocators, LoginPageLocators
from generators import generate_unique_email, generate_password
from config import REGISTER_URL, LOGIN_URL, MAIN_URL, PROFILE_URL

def close_modal_if_present(driver, timeout=10):
    wait = WebDriverWait(driver, timeout)

    # Проверяем наличие оверлея
    try:
        overlay = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".Modal_modal_overlay__x2ZCr")
        ))
    except Exception:
        # Оверлея нет — ничего не делаем, это нормально
        return

    # Пробуем закрыть кнопкой закрытия
    try:
        close_btn = driver.find_element(
            By.CSS_SELECTOR, ".Modal_modal__close__TnseK"  # исправлен класс
        )
        if close_btn.is_displayed():
            close_btn.click()
            wait.until(EC.invisibility_of_element(overlay))
            return
    except Exception:
        pass

    # Пробуем кликнуть по оверлею
    try:
        overlay.click()
        wait.until(EC.invisibility_of_element(overlay))
        return
    except Exception:
        pass

    # Если ничего не помогло — выбрасываем ошибку, а не удаляем оверлей через JS
    # Удаление через JS — это «костыль», который скрывает реальные проблемы верстки
    raise RuntimeError("Не удалось закрыть модальное окно стандартными способами")

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    
    if browser == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        # options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Неизвестный браузер: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def registered_user(driver):
    # Регистрирует пользователя
    email = "Aisulu_52_125@mail.ru"
    password = "123456"
    return email, password

@pytest.fixture
def logged_in_user(driver, registered_user):
    email, password = registered_user
    
    driver.get(LOGIN_URL)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_FIELD))
    
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
    close_modal_if_present(driver)
    driver.find_element(*LoginPageLocators.SUBMIT_BTN).click()
    
    wait.until(EC.url_to_be(MAIN_URL))
    return email, password

def safe_click(driver, locator):

    wait = WebDriverWait(driver, 15)
    element = wait.until(EC.element_to_be_clickable(locator))
    
    try:
        element.click()
    except Exception as e:
        driver.execute_script("arguments[0].click();", element)