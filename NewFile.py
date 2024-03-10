import serial  # Импорт модуля serial для работы с последовательным портом
import time  # Импорт модуля time для работы со временем
import serial.tools.list_ports  # Импорт модуля list_ports из пакета serial.tools для получения списка доступных портов

speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200']  # Список доступных скоростей для последовательного порта
ports = [p.device for p in serial.tools.list_ports.comports()]  # Получение списка доступных портов и извлечение их имен
port_name = ports[0]  # Выбор первого порта из списка
port_speed = int(speeds[-1])  # Выбор самой высокой скорости из списка и преобразование ее в целое число
port_timeout = 10  # Установка времени ожидания ввода/вывода в порт (в секундах)

ard = serial.Serial(port_name, port_speed, timeout=port_timeout)  # Инициализация объекта Serial для работы с последовательным портом
time.sleep(1)  # Пауза в 1 секунду для инициализации порта
ard.flushInput()  # Очистка входного буфера порта

try:
    # Чтение данных из порта и объединение полученных байтов
    msg_bin = ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())
    msg_bin += ard.read(ard.inWaiting())
    
    msg_str_ = msg_bin.decode()  # Декодирование полученных байтов в строку
    print(len(msg_bin))  # Вывод длины полученных байтов

except Exception as e:
    print('Error!')  # Вывод сообщения об ошибке при возникновении исключения

ard.close()  # Закрытие порта
time.sleep(1)  # Пауза в 1 секунду
print(msg_str_)  # Вывод содержимого строки msg_str_
