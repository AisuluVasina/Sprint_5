class MainPageLocators:
    # Кнопка «Войти в аккаунт» на главной
    LOGIN_BTN_MAIN = ("css", "a[href='/login']")  
    # Ссылка «Личный кабинет»
    PERSONAL_CABINET_LINK = ("css", "a[href='/profile']")  # Ссылка «Личный кабинет»
# Ссылка «Личный кабинет»
    LOGIN_BTN_MAIN = ("css", "a[href='/login']")  
    PERSONAL_CABINET_LINK = ("css", "a[href='/profile']") 

class LoginPageLocators:
    # Поле ввода email
    EMAIL_FIELD = ("css", "input[type='email']")
    # Поле ввода пароля
    PASSWORD_FIELD = ("css", "input[type='password']")
    # Кнопка "Войти"
    SUBMIT_BTN = ("css", "button[type='submit']")
     # Сообщение об ошибке
    ERROR_MSG = ("css", ".error-message")  

# Элементы страницы регистрации
class RegistrationPageLocators:
    # Поле ввода имени
    NAME_FIELD = ("css", "input[name='name']")
    # Поле ввода email
    EMAIL_FIELD = ("css", "input[type='email']")
    # Поле ввода пароля
    PASSWORD_FIELD = ("css", "input[type='password']")
    # Кнопка "Зарегистрироваться"
    SUBMIT_BTN = ("css", "button[type='submit']")
    # Ссылка "Войти"
    LOGIN_LINK_IN_REG = ("css", "a[href='/login']") 
    # ссылка "Забыли пароль"
    FORGOT_PASSWORD_LINK = ("css", "a[href='/forgot-password']")
    BACK_TO_LOGIN_LINK = ("css", "a[href='/login']")

class PersonalCabinetLocators:
    # Кнопка «Выйти»
    LOGOUT_BTN = ("css", "button[data-testid='logout']")
    # Ссылка «Конструктор» 
    CONSTRUCTOR_LINK = ("css", "a[href='/']")
    # Логотип 
    LOGO_IMG = ("css", "img[alt='Stellar Burgers']") 

class ConstructorLocators:
    # Вкладка "Булки"
    BUNS_TAB = ("css", "[data-testid='buns-tab']")
    # Вкладка "Соусы"
    SAUCES_TAB = ("css", "[data-testid='sauces-tab']")
    # Вкладка "Начинки"
    TOPPINGS_TAB = ("css", "[data-testid='toppings-tab']")
    
    # Первый элемент списка "Булки"
    FIRST_BUN = ("css", "[data-testid='bun-item']") 
    # Первый элемент списка "Соусы"
    FIRST_SAUCE = ("css", "[data-testid='sauce-item']")
    # Первый элемент списка "Начинки"
    FIRST_TOPPING = ("css", "[data-testid='topping-item']") 

