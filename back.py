# Файлик с логикой работы приложения

import requests
from bs4 import BeautifulSoup
import re

"""
url_bel_b = 'https://belarusbank.by/' # Ссылка на сайт Беларусьбанка

# Заголовки необходимые для корректного доступа на сайт
headers_bel_b = {
    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }
"""
# Функция доступа к странице
def get_html(url, headers):
    out = requests.get(url, headers=headers)
    return out

# Функция получения нужного контента со страницы беларусбанк
def get_content_bel_b(html):
    page_data = BeautifulSoup(html, 'html.parser')
    items = page_data.find_all('div', class_='home-page-block home-page-block--sm home-page-block--white home-page-block--bg-7 col-lg-3 col-md-4 col-sm-6 col-2xs-12')
    rez = {}
    temp = []
    # поиск значений названий валют и курсов
    for element in items:
        currency = element.find_all_next('td', class_='currency-table__cell-curr')
        value = element.find_all_next('td', class_='currency-table__cell-value')
    # Добавление названий в выходной словарь
    for line in currency:
        curr_name = line.text.strip().replace('\n', '')
        rez[curr_name] = ''
    # Добавление значений соответствующим валютам в выходной словарь
    for line in value:
        temp.append(line.text.strip().replace('\n', ''))
    rez['1 доллар США'] = (temp[0], temp[1])
    rez['1 евро'] = (temp[2], temp[3])
    rez['100 российских рублей'] = (temp[4], temp[5])
    return rez

# Функция получения нужного контента со страницы технобанк
def get_content_tb(html):
    page_data = BeautifulSoup(html, 'html.parser')
    items = page_data.find_all('div', class_='row row-md-bordered tab-content')
    temp = []
    rez = {}
    # Получение данных
    for element in items:
        currency = element.find_all_next('span', class_='currency-media-body media-body')
        value = element.find_all_next('span', class_='currency-media-new-curr')
    # Сортировка данных
    for line_val in value:
        temp.append(line_val.text)

    for line in currency:
        rez[line.text] = ''
    # Добавление значений соответствующим валютам в выходной словарь
    rez['USD'] = (temp[2], temp[3])
    rez['EUR'] = (temp[4], temp[5])
    rez['RUB'] = (temp[0], temp[1])
    return rez
# Функция получения данных с сайта НБ
def get_content_nb(html):
    page_data = BeautifulSoup(html, 'html.parser')
    items = page_data.find_all('dl', class_='js-stats-item', id='p4')
    out = []
    rez = {}
    for element in items:
        temp = element.text.strip().split('\n')
    for elem in temp:
        if elem != '':
            out.append(elem.strip())
    # Правочка для более стабильной работы
    # Поиск индексов по названиям валют
    index_usd = out.index('USD 1 Доллар США')
    index_euro = out.index('EUR 1 Евро')
    index_rub = out.index('RUB 100 Российских рублей')
    # Заполнение словаря данными
    rez[out[index_usd]] = (out[index_usd + 1], out[index_usd + 2])
    rez[out[index_euro]] = (out[index_euro + 1], out[index_euro + 2])
    rez[out[index_rub]] = (out[index_rub + 1], out[index_rub + 2])
    temp_date = []
    for data_element in out:
        if re.match('\d\d.\d\d.\d\d',data_element):
            temp_date.append(data_element)
    rez['today'] = temp_date[0]
    rez['tomorrow'] = temp_date[1]
    return rez