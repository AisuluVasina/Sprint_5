from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопки и ссылки
    LOGIN_BTN_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_CABINET_LINK = (By.XPATH, '//p[text() = "Личный Кабинет"]')
    CONSTRUCTOR_LINK = (By.XPATH, "//a[.//p[contains(text(), 'Конструктор')]]")
    # Логотип 
    LOGO_IMG = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]'
    #LOGO_LINK = (By.CSS_SELECTOR, 'div.AppHeader_header_logo_2D0X2 a[href="/"]') 
    # Элементы модального окна
    MODAL_OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    MODAL_CLOSE_BUTTON = (By.CLASS_NAME, "Modal_modal__close__TnseK")

    # Заголовок "Соберите бургер" (для проверки главной)
    BUN_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")
    
class LoginPageLocators:
    # Поле ввода email
    EMAIL_FIELD = (By.XPATH, './/label[text()="Email"]/following-sibling::input')
    # Поле ввода пароля
    PASSWORD_FIELD = (By.XPATH, './/input[@name="Пароль"]')
    # Кнопка "Войти"
    SUBMIT_BTN = (By.XPATH, './/button[text()="Войти"]')
    # Сообщение об ошибке
    ERROR_MSG = By.XPATH, '//p[text() = "Некорректный пароль"]'
    # Восстановить пароль
    FORGOT_PASSWORD_LINK = ("css selector", "a[href='/forgot-password']")
    BACK_TO_LOGIN_LINK = ("css selector", "a[href='/login']") 

# Элементы страницы регистрации
class RegistrationPageLocators:
    # Поле ввода имени
    NAME_FIELD = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
    # Поле ввода email
    EMAIL_FIELD = (By.XPATH, './/label[text()="Email"]/following-sibling::input')
    # Поле ввода пароля
    PASSWORD_FIELD = (By.XPATH, './/input[@name="Пароль"]')
    # Кнопка "Зарегистрироваться"
    SUBMIT_BTN = (By.XPATH, '//button[text() = "Зарегистрироваться"]')
    # Кнопка "Войти"
    LOGIN_LINK_IN_REG = By.XPATH, '//a[text() = "Войти"]'
    # ссылка "Забыли пароль"
    FORGOT_PASSWORD_LINK = ("css selector", "a[href='/forgot-password']")
    BACK_TO_LOGIN_LINK = ("css selector", "a[href='/login']")

class PersonalCabinetLocators:
    # Кнопка «Выйти»
    LOGOUT_BTN = By.XPATH, '//button[@type = "button"]'

class ConstructorLocators:
    # Вкладки (базовые локаторы)
    BUNS_TAB = (By.XPATH, '//span[text() = "Булки"]')
    SAUCES_TAB = (By.XPATH, '//span[text() = "Соусы"]')
    TOPPINGS_TAB = (By.XPATH, '//span[text() = "Начинки"]')

    # Локаторы с проверкой активного класса (для assert)
    BUNS_TAB = (By.XPATH, "//span[normalize-space()='Булки']/..")
    SAUCES_TAB = (By.XPATH, "//span[normalize-space()='Соусы']/..")
    TOPPINGS_TAB = (By.XPATH, "//span[normalize-space()='Начинки']/..")

    # Элементы списков
    FIRST_BUN = ("xpath", "//a[.//img[@alt='Флюоресцентная булка R2-D3']]")
    FIRST_SAUCE = ("xpath", "//a[.//img[@alt='Соус Spicy-X']]")
    FIRST_TOPPING = ("xpath", "//a[.//img[@alt='Мясо бессмертных моллюсков Protostomia']]")