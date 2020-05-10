# -*- coding: utf8 -*-

"""Программа собирает данные пользователей,
которые вводят логин и пароль.
Если логин и пароль валидны, то они записываются в файл.
Если нет, то данные предлагается ввести заново согласно требованиям.
Также есть проверка на уникальность логина и mail.

"""

from re import fullmatch
from save import saveme

regular_login = r"^[a-zA-Z0-9\._-]{4,20}$"
"""Регулярное выражение для проверки логина пользователя.
Логин должен начинаться с буквы и состоять не менее чем из 4 символов и не более чем из 20 символов;
при создании логина можно использовать латинские буквы, цифры, символы тире (-), подчеркивания (_) и точки (.)

"""

regular_email = r"^[\w\.-]+@([A-z\d][-A-z\d]+\.)+[A-z]{2,4}$"
"""Регулярное выржание для проверки email пользователя.
Можно использовать (.), (-), (_), домен начинается с латинской буквы, регион от 2 до 4 букв.

"""

print("Если у вас еще нет аккаунта, пожалуйста, зарегистрируйтесь.\n")
print("Логин должен начинаться с буквы и состоять не менее чем из 6 символов и не более чем из 20 символов;\n"
      "при создании логина можно использовать латинские буквы, цифры, символы тире (-), подчеркивания (_) и точки (.)\n")

user_data = {}  # Словарь для хранения связок {логин : email}

users = int(input("Сколько пользователей вы хотите занести в базу данных?: "))

for i in range(users):

    user_login = input("Введите логин: ").lower()  # Переводим в нижний регистр
    while user_login in user_data.values():  # Проверка на дубль в одном словаре
        print("Пользователь с таким логином уже существует :(")
        user_login = input("Попробуйте другой логин: ").lower()

    user_email = input("Введите email: ").lower()
    while user_email in user_data.keys():   # Проверка на дубль в одном словаре
        print("Почта", user_email, "уже зарегистрирована в системе.")
        user_email = input("Введите другую почту: ").lower()

    valid_login = fullmatch(regular_login, user_login)
    valid_email = fullmatch(regular_email, user_email)

    while valid_login is None or valid_email is None:
        if valid_login is None and valid_email is None:
            print("Вы ввели все неправильно")
        elif valid_login is None:
            print("Ошибка при вводе логина.")
        elif valid_email is None:
            print("Ошибка при вводе email")

        user_login = input("Введите логин: ").lower()
        while user_login in user_data.values():
            print("Пользователь с таким логином уже существует :(")
            user_login = input("Попробуйте другой логин: ").lower()

        user_email = input("Введите email: ").lower()
        while user_email in user_data.keys():
            print("Почта", user_email, "уже зарегистрирована в системе.")
            user_email = input("Введите другую почту: ").lower()

        valid_login = fullmatch(regular_login, user_login)
        valid_email = fullmatch(regular_email, user_email)

    print("Данные сохранены")
    user_data[user_email] = user_login
    print(user_data)

saveme(user_data)
