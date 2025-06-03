from flask import Flask
from datetime import datetime
import pytz
import logging
import os
import sys # Импортируем sys для sys.stdout

app = Flask(__name__)

timezones = {
    "Москва": "Europe/Moscow",
    "Санкт-Петербург": "Europe/Moscow",
    "Таджикистан (Душанбе)": "Asia/Dushanbe",
    "Китай (Пекин)": "Asia/Shanghai",
    "США (Нью-Йорк)": "America/New_York",
    "США (Лос-Анджелес)": "America/Los_Angeles",
    "Европа (Берлин)": "Europe/Berlin",
    "Европа (Лондон)": "Europe/London",
    "Япония (Токио)": "Asia/Tokyo",
    "Индия (Дели)": "Asia/Kolkata",
    "ОАЭ (Дубай)": "Asia/Dubai",
    "Бразилия (Сан-Паулу)": "America/Sao_Paulo"
}

# Инициализируем логгер до использования
logger = logging.getLogger(__name__) # Получаем логгер для текущего модуля

# Функция для настройки логирования
def setup_logging():
    log_dir = "/var/log/current-time"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 1. Настройка обработчика для файла (для startup.log)
    file_handler = logging.FileHandler(os.path.join(log_dir, "startup.log"), encoding='utf-8')
    file_handler.setLevel(logging.INFO) # Уровень логирования для файла
    file_formatter = logging.Formatter('%(asctime)s %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # 2. Настройка обработчика для стандартного вывода (stdout)
    console_handler = logging.StreamHandler(sys.stdout) # Направляем в stdout
    console_handler.setLevel(logging.INFO) # Уровень логирования для консоли
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s') # Формат для консоли
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # Устанавливаем общий уровень логирования для логгера
    logger.setLevel(logging.INFO)

    # Лог запуска приложения (попадет и в файл, и в stdout)
    logger.info("Лог Нео - время запуска приложения: %s", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

@app.route("/")
def current_time():
    # Логирование запроса к сайту в stdout
    logger.info("Сайт был запрошен/обновлен.") # Это сообщение пойдет в stdout

    result = "<h1>Текущее время в разных странах и регионах:</h1><ul>"
    for name, zone in timezones.items():
        tz = pytz.timezone(zone)
        now = datetime.now(tz)
        formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')
        result += f"<li><strong>{name}</strong>: {formatted_time}</li>"
    result += "</ul>"
    return result

if __name__ == "__main__":
    setup_logging() # Вызываем новую функцию настройки логирования
    # Flask также выводит свои собственные логи в stdout/stderr по умолчанию.
    # Если вы не хотите, чтобы Flask логировал каждый HTTP-запрос, можно отключить его логирование,
    # но обычно это полезно для отладки.
    app.run(host="0.0.0.0", port=1001)