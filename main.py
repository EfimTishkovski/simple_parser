from back import *

url_bel_b = 'https://belarusbank.by/' # Ссылка на сайт Беларусбанка
url_tb = 'https://tb.by/individuals/' # Ссылка на сайт Технобанка

# Заголовки необходимые для корректного доступа на сайт
headers_bel_b = {
    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }

# Заголовки необходимые для корректного доступа на сайт
headers_tb = {
    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }

# Запросы на сайт банков
answer_bel_b = get_html(url_bel_b, headers_bel_b)
answer_tb = get_html(url_tb, headers_tb)

if answer_bel_b.status_code == 200:
    print(get_content_bel_b(answer_bel_b.text))
else:
    print('Беларусбанк: ошибка получения данных')

if answer_tb.status_code == 200:
    print(get_content_tb(answer_tb.text))
else:
    print('Технобанк: ошибка получения данных')

