# Файлик с логикой работы приложения

import requests
from bs4 import BeautifulSoup

url_bel_b = 'https://belarusbank.by/' # Ссылка на сайт Беларусьбанка

# Заголовки необходимые для корректного доступа на сайт
headers_bel_b = {
    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }

# Функция доступа к странице
def get_html(url, headers):
    out = requests.get(url, headers=headers)
    return out

# Функция получения нужного контента со страницы
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


#print(get_html(url_bel_b, headers_bel_b))
#html_bel_b = get_html(url_bel_b, headers_bel_b)
#print(get_content_bel_b(html_bel_b.text))