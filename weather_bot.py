import requests
import schedule
import time
from datetime import datetime
from linebot import LineBotApi
from linebot.models import TextSendMessage

# --- あなたの情報 ---
LINE_ACCESS_TOKEN = "lNN3PhUSK2F4W9Nz24xpw6roqdeDvw3SPLhyM5r7tbK936XrX3bW/J1qUCRnneY2CBO2JxsBerhzvaG1InKHLK/FVOCnovBXsFgrtqEq2mjv9d9C+InT8mwr9hPWUXSJ9eHrKL8RHCd8QCq+xYLzAgdB04t89/1O/w1cDnyilFU="
API_KEY = "あbce0dd5f4f0105d0aad1504b3ff98d8dなたのOpenWeatherMap"
LAT = 43.1143   # 緯度（札幌市北区麻生町）
LON = 141.3392  # 経度（札幌市北区麻生町）
USER_ID = "U6d2eb8e5dc1ce12677f9bd247a30f70d"

# --- 天気を取得してLINEに送信 ---
def send_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric&lang=ja"
    response = requests.get(url)
    data = response.json()

    # エラーチェック
    if response.status_code != 200 or "weather" not in data:
        print("⚠️ 天気情報の取得に失敗しました:", data)
        return

    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]

    message = (
        f"【札幌市北区麻生町の天気】\n"
        f"天気：{weather}\n"
        f"現在の気温：{temp}℃\n"
        f"最低気温：{temp_min}℃\n"
        f"最高気温：{temp_max}℃\n"
        f"（{datetime.now().strftime('%H:%M')} 時点）"
    )

    # LINEに送信
    line_bot_api = LineBotApi(LINE_ACCESS_TOKEN)
    line_bot_api.push_message(USER_ID, TextSendMessage(text=message))
    print("✅ 天気をLINEに送信しました！")

# --- 毎朝7:30に実行 ---
schedule.every().day.at("07:30").do(send_weather)

print("🌤 天気通知ボットが起動しました（7:30に送信）")

# --- 常に動かし続ける ---
while True:
    schedule.run_pending()
    time.sleep(30)
