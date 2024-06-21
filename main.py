# -*- coding: utf-8 -*-
def check_age(age):

    if age >= 18:
        result = 'Доступ разрешён'
    else:
        result = 'Доступ запрещён'

    return result

def check_auth(login, password):

    if login == 'admin' and password == 'password':
        # В этом блоке напишите код, который выполнится, если условие True. Используйте result, как в задании выше
        result = 'Добро пожаловать'
    else:
        # В этом блоке напишите код, который выполнится, если условие False. Используйте result, как в задании выше
        result = 'Доступ ограничен'
    return result

def get_cost(weight):
    if weight <= 10:
        result = 'Стоимость доставки: 200 руб.'
    else:
        result = 'Стоимость доставки: 500 руб.'
    return result