from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os

app = Flask(__name__) 

@app.route('/')
def home():
    return "LINE天気Bot稼働中！"




LINE_CHANNEL_ACCESS_TOKEN = "lNN3PhUSK2F4W9Nz24xpw6roqdeDvw3SPLhyM5r7tbK936XrX3bW/J1qUCRnneY2CBO2JxsBerhzvaG1InKHLK/FVOCnovBXsFgrtqEq2mjv9d9C+InT8mwr9hPWUXSJ9eHrKL8RHCd8QCq+xYLzAgdB04t89/1O/w1cDnyilFU="
LINE_CHANNEL_SECRET = "2faec8027320d6b0f80fc817bc351f34"

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)



@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_text = event.message.text  # ユーザーが送ったメッセージ

    # 特定の言葉に応じた返信
    if "おはよう" in user_text:
        reply_text = "おはよう！今日もがんばろう☀️"
    elif "疲れた" in user_text:
        reply_text = "おつかれさま！無理しすぎないでね🍵"
    elif "ありがとう" in user_text:
        reply_text = "どういたしまして😊"
    else:
        reply_text = "うんうん、聞いてるよ👂"

    # LINEに返信を送信
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
