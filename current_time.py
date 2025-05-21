from flask import Flask
from datetime import datetime
import pytz
import logging
import os

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

# Функция для записи лога запуска
def log_startup():
    log_dir = "/var/log/current-time"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    logging.basicConfig(
        filename=os.path.join(log_dir, "startup.log"),
        level=logging.INFO,
        format='%(asctime)s %(message)s',
        encoding='utf-8'
    )
    logging.info("Лог Нео - время запуска приложения: %s", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

@app.route("/")
def current_time():
    result = "<h1>Текущее время в разных странах и регионах:</h1><ul>"
    for name, zone in timezones.items():
        tz = pytz.timezone(zone)
        now = datetime.now(tz)
        formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')
        result += f"<li><strong>{name}</strong>: {formatted_time}</li>"
    result += "</ul>"
    return result

if __name__ == "__main__":
    log_startup()
    app.run(host="0.0.0.0", port=1001)
