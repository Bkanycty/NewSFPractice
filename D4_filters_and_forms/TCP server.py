# Необходимо сделать tcp сервер, который распознаёт заданный формат данных и отображает его в требуемом формате.
# Обязательна запись данных во внешний файл. Интерфейс и способ отображения на выбор разработчика.
# Формат данных BBBBxNNxHH:MM:SS.zhqxGGCR


import socket
import logging

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', 53210))
serv_sock.listen(10)

Log_Format = "%(asctime)s - %(message)s"

logging.basicConfig(filename="logfile.log",
                    filemode="a",
                    format=Log_Format,
                    level=logging.INFO)

logger = logging.getLogger()
handler = logging.FileHandler('logfile.log')
logger.addHandler(handler)


def write_data(ready_list):  # Выводим логгирование данных в отдельную функцию, чтобы не повторять ее в коде
    ready_list = ''.join(ready_list)
    member_number = ready_list[0:4]
    channel_id = ready_list[5:7]
    cross_time = ready_list[8:18]
    data_formatted = f"Спортсмен, нагрудный номер {member_number} прошел отсечку {channel_id} в {cross_time}"
    logger.info(data_formatted)
    return data_formatted


while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)
    some_list = []  # Создаем пустой список, в который будут добавляться символы, переданные telnet
    while True:
        # Пока клиент не отключился, читаем передаваемые им данные
        data = client_sock.recv(1024)
        text_data = data.decode('utf-8')  # Декодируем данные из битовых, чтобы в список не падали лишние символы
        if not data:
            # Клиент отключился
            print('Клиент отключился')
            break

        some_list.append(text_data)  # Добавляем символ в список
        print(''.join(some_list))  # ДЛЯ ТЕСТА печатаем в консоль текущий список, чтобы видеть изменения
        if '[CR]' in ''.join(some_list):  # Если в списке стоп-символ, то проверяем номер группы
            if ''.join(some_list)[
               -6:-4] == '00':  # Если номер группы 00, то выводим форматированный текст в консоль и логгируем данные
                write_data(some_list)

                print(
                    f"Спортсмен, нагрудный номер {''.join(some_list[0:4])} прошел отсечку {''.join(some_list[5:7])} в {''.join(some_list[8:18])}")
            else:  # Если номер группы не 00, то просто логгируем данные
                write_data(some_list)
            some_list = []  # обнуляем список, чтобы принимать новые данные

    client_sock.close()

# BBBB - номер участника
# x - пробельный символ
# NN - id канала
# HH - Часы
# MM - минуты
# SS - секунды
# zhq - десятые сотые тысячные
# GG - номер группы
# CR - "возврат каретки" (закрывающий символ)

# Пример данных: 0002 C1 01:13:02.877 00[CR] Выводим "спортсмен, нагрудный номер BBBB прошел отсечку NN в "время" до десятых, сотые и тысячные отсекаются.
# Только для группы 00. Для остальных групп данные не отображаются, но пишутся в лог полностью.

