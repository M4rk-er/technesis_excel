EMPTY_CELL = 'В отправленном вами файле присутствуют пустые ячейки, проверьте его содержимое и отправьте файл еще раз'
WRONG_XPATH = 'Проверьте корректность указанвого вами xpath'
NOT_NUMBER_IN_XPATH = 'Проеврьте что по указанному вами xpath хранится число'
NOT_FILE_SENT = 'Отправте файл'
WRONG_FILE_FORMAT = 'Неверный формат файла, отправте файл в <b>.xlsx</b> формате'
MESSAGE_TEMPLATE = '\nНазвание: <b>{}</b>\nСсылка: {}\nЦена: <b>{}</b>\n'
START_MESSAGE = ('Привет, этот бот умеет обрабатывать файлы в формате <b>.xlsx</b>,'
                 ' возращать и возращать их содержимое. Файлы должны содержать столбцы'
                 ' с именами title, url, xpath в которых храниться имя товара, сссылка'
                 ' на него и xpath до его цены. Для начала работы испольюзуйте команду \n/excel')
SEND_FILE = 'Пожалуйста отправте файл в формате <b>.xlsx</b>'


def make_message_with_file_content(rows):
    res = ''
    for row in rows:
        title, url, price = row
        res += MESSAGE_TEMPLATE.format(title, url, price)
    return res
