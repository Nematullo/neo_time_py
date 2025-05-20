# app.py
from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

# Список нужных временных зон с названиями
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
    app.run(host="0.0.0.0", port=1001)
