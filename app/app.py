# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import datetime
import logging
import redis


from flask import Flask, request, abort


from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.exceptions import (InvalidSignatureError)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
    ButtonsTemplate, URITemplateAction, PostbackTemplateAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    ImagemapSendMessage, MessageImagemapAction, BaseSize, ImagemapArea
)

app = Flask(__name__)
app.config.from_object('config')
redis = redis.from_url(app.config['REDIS_URL'])
stream_handler = logging.StreamHandler()
app.logger.addHandler(stream_handler)
app.logger.setLevel(app.config['LOG_LEVEL'])
line_bot_api = LineBotApi(app.config['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(app.config['CHANNEL_SECRET'])


@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    sysdate = datetime.datetime.today()
    if text == 'START':
        line_bot_api.reply_message(
            event.reply_token,
            TextMessage(text=sysdate)
        )
    elif text == 'STOP':
        line_bot_api.reply_message(
            event.reply_token,
            TextMessage(text=sysdate)
        )
    elif text == 'RECORDS':
        line_bot_api.reply_message(
            event.reply_token,
            TextMessage(text=text)
        )
    elif text == 'PLANK':
        line_bot_api.reply_message(
            event.reply_token,
            TextMessage(text=text)
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextMessage(text=text)
        )
