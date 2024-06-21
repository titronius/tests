# -*- coding: utf-8 -*-
import pytest
import requests
from main import check_age, check_auth, get_cost
from settings import yandex_token

@pytest.mark.parametrize(
    'age, expected',
    (
        [10, 'Доступ запрещён'],
        [20, 'Доступ разрешён'],
        [18, 'Доступ разрешён'],
    )
)
def test_check_age(age, expected):
    result = check_age(age)
    assert result == expected

@pytest.mark.parametrize(
    'login, password, expected',
    (
        ['admin', 'password', 'Добро пожаловать'],
        ['user', 'password', 'Доступ ограничен'],
        ['admin', 'рыбамеч', 'Доступ ограничен'],
    )
)
def test_check_auth(login, password, expected):
    result = check_auth(login,password)
    assert result == expected

@pytest.mark.parametrize(
    'weight, expected',
    (
        [5, 'Стоимость доставки: 200 руб.'],
        [10, 'Стоимость доставки: 200 руб.'],
        [20, 'Стоимость доставки: 500 руб.'],
    )
)
def test_get_cost(weight, expected):
    result = get_cost(weight)
    assert result == expected

class TestYandexDisk:
    def setup_method(self):
        self.headers = {
            'Authorization': f'OAuth {yandex_token}'
        }

    @pytest.mark.parametrize(
        'key,value,statuscode',
        (
                ['pat', 'Файлы', 400],
                ['path', 'Файлы', 201],
                ['path', 'Файлы', 409],
        )
    )
    def test_create_folder(self, key, value, statuscode):
        params = {key: value}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)
        assert response.status_code == statuscode

