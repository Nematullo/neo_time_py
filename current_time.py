# app.py
from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def current_time():
    now = datetime.now()
    return f"<h1>Сейчасное время:</h1><p>{now.strftime('%Y-%m-%d %H:%M:%S')}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1001)
