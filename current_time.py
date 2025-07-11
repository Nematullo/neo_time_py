from flask import Flask, render_template_string
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
    times = []
    for name, zone in timezones.items():
        tz = pytz.timezone(zone)
        now = datetime.now(tz)
        formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')
        times.append({'name': name, 'time': formatted_time})

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Текущее время</title>
        <meta charset="utf-8">
        <style>
            body {
                background: #f6fff6;
                font-family: 'Segoe UI', Arial, sans-serif;
                color: #222;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 500px;
                margin: 40px auto;
                background: #fff;
                border-radius: 12px;
                box-shadow: 0 2px 12px rgba(0,128,0,0.08);
                padding: 32px;
            }
            h1 {
                color: #1a7f37;
                text-align: center;
                margin-bottom: 24px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                background: #eaffea;
                border-radius: 8px;
                overflow: hidden;
            }
            th, td {
                padding: 12px 8px;
                text-align: left;
            }
            th {
                background: #1a7f37;
                color: #fff;
                font-weight: 600;
            }
            tr:nth-child(even) {
                background: #d6f5d6;
            }
            tr:hover {
                background: #b2eab2;
            }
        </style>
        <script>
            setTimeout(function() {
                window.location.reload();
            }, 5000); // обновлять каждые 5 секунд
        </script>
    </head>
    <body>
        <div class="container">
            <h1>Текущее время в разных странах и регионах</h1>
            <table>
                <tr>
                    <th>Регион</th>
                    <th>Время</th>
                </tr>
                {% for t in times %}
                <tr>
                    <td>{{ t.name }}</td>
                    <td>{{ t.time }}</td>
                </tr>
                {% endfor %}
            </table>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, times=times)

if __name__ == "__main__":
    setup_logging() # Вызываем новую функцию настройки логирования
    # Flask также выводит свои собственные логи в stdout/stderr по умолчанию.
    # Если вы не хотите, чтобы Flask логировал каждый HTTP-запрос, можно отключить его логирование,
    # но обычно это полезно для отладки.
    app.run(host="0.0.0.0", port=1001)