import random
import string

def generate_unique_email(first_name="Aisylu", last_name="Vasina", cohort="52"):
   #Генерация email
    random_digits = ''.join(random.choices(string.digits, k=3))
    return f"{first_name}_{last_name}_{cohort}_{random_digits}@yandex.ru"

def generate_password(length=6):
    #Генерация пароля из букв и цифр.
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))