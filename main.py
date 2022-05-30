from back import *
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi
import sys

url_bel_b = 'https://belarusbank.by/' # Ссылка на сайт Беларусбанка
url_tb = 'https://tb.by/individuals/' # Ссылка на сайт Технобанка
url_nb = 'https://www.nbrb.by/'       # Ссылка на сайт нацбанка
url_vtb = 'https://www.vtb.by/sites/default/files/rates.xml' # Ссылка на сайт ВТБ

# Заголовки необходимые для корректного доступа на сайт
headers_bel_b = {
    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }

headers_tb = {
    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }

headers_vtb = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
    }

class Main_window(QWidget):
    # Функция отображения данных в окошке программы
    def show_data(self):
        try:
            enable_bank = self.comboBox.currentText()
            # Получение и отображение данных от Беларусбанка
            if enable_bank == 'Беларусбанк':
                answer_bel_b = get_html(url_bel_b, headers_bel_b)
                if answer_bel_b.status_code == 200:
                    course_data = get_content_bel_b(answer_bel_b.text)
                    self.buy.setText('Покупка')
                    self.sale.setText('Продажа')
                    # Отображение курса доллара
                    self.usd_buy.setText(course_data['1 доллар США'][0])
                    self.usd_sale.setText(course_data['1 доллар США'][1])
                    # Отображение курса евро
                    self.euro_buy.setText(course_data['1 евро'][0])
                    self.euro_sale.setText(course_data['1 евро'][1])
                    # Отображение курса российского рубля
                    self.rub_buy.setText(course_data['100 российских рублей'][0])
                    self.rub_sale.setText(course_data['100 российских рублей'][1])
                    self.messege_label.setText('Готово(Беларусбанк)')
                else:
                    self.messege_label.setText('Ошибка')

            # Получение и отображение данных от Технобанка
            if enable_bank == 'Технобанк':
                answer_tb = get_html(url_tb, headers_tb)
                if answer_tb.status_code == 200:
                    course_data = get_content_tb(answer_tb.text)
                    self.buy.setText('Покупка')
                    self.sale.setText('Продажа')
                    # Отображение курса доллара
                    self.usd_buy.setText(course_data['USD'][0])
                    self.usd_sale.setText(course_data['USD'][1])
                    # Отображение курса евро
                    self.euro_buy.setText(course_data['EUR'][0])
                    self.euro_sale.setText(course_data['EUR'][1])
                    # Отображение курса российского рубля
                    self.rub_buy.setText(course_data['RUB'][0])
                    self.rub_sale.setText(course_data['RUB'][1])
                    self.messege_label.setText('Готово (Технобанк)')
                else:
                    self.messege_label.setText('Ошибка')

            # Получение и отображение данных от Нацбанка
            if enable_bank == 'Национальный банк РБ':
                answer_nb = get_html(url_nb, headers='')
                if answer_nb.status_code == 200:
                    course_data = get_content_nb(answer_nb.text)
                    self.buy.setText(course_data['today'])
                    self.sale.setText(course_data['tomorrow'])
                    # Отображение курса доллара
                    self.usd_buy.setText(course_data['USD 1 Доллар США'][0])
                    self.usd_sale.setText(course_data['USD 1 Доллар США'][1])
                    # Отображение курса евро
                    self.euro_buy.setText(course_data['EUR 1 Евро'][0])
                    self.euro_sale.setText(course_data['EUR 1 Евро'][1])
                    # Отображение курса российского рубля
                    self.rub_buy.setText(course_data['RUB 100 Российских рублей'][0])
                    self.rub_sale.setText(course_data['RUB 100 Российских рублей'][1])
                    self.messege_label.setText('Готово (Нацбанк)')
                else:
                    self.messege_label.setText('Ошибка')

            # Получение данных от ВТБ
            if enable_bank == 'ВТБ':
                answer_vtb = get_html(url_vtb, headers=headers_vtb)
                if answer_vtb.status_code == 200:
                    data = get_content_vtb()
                    print(data)
                else:
                    self.messege_label.setText('Ошибка')
        except:
            self.messege_label.setText('Ошибка')
    def __init__(self):
        super(Main_window, self).__init__()
        loadUi('Form.ui', self)

        self.messege_label.setText('')                         # Сброс сообщения при запуске
        self.show_data()                                       # Получение первойстроки комбобокса
        self.comboBox.activated[str].connect(self.show_data)   # Обработка сигнала смены строки комбобокса
        self.refresh_button.clicked.connect(self.show_data)    # Обработчик кнопки "обновить"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main_window()
    window.show()
    sys.exit(app.exec_())