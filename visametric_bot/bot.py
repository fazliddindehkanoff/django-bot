from django.conf import settings
from django.db.models.query_utils import PathInfo
import requests as r
import json


BASE_URL = "https://api.telegram.org/bot{}/".format(settings.BOT_TOKEN)


def bot(method, data):
    response = r.post(BASE_URL + method, json=data)
    return json.loads(response.text)

def send_message(text, chat_id, menu = None, parse_mode = "html"):
    data = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": parse_mode,
        "disable_web_page_preview": True
    }

    if menu:
        data["reply_markup"] = menu
    
    return bot("sendMessage", data)


def send_photo(photo_url, caption, chat_id, menu=None, parse_mode="html"):
    data = {
        "chat_id": chat_id,
        "photo": photo_url,
        "caption": caption,
        "parse_mode": parse_mode
    }

    if menu:
        data["reply_markup"] = menu

    return bot("sendPhoto", data)


def edit_message(text, chat_id, message_id, menu = None, parse_mode = "html"):
    data = {
        "chat_id": chat_id,
        "text": text,
        "message_id": message_id,
        "parse_mode": parse_mode
    }

    if menu:
        data["reply_markup"] = menu
    
    return bot("editMessageText", data)


def edit_reply_markup(chat_id, message_id, menu):
    data = {
        "chat_id": chat_id,
        "message_id": message_id,
        "reply_markup": menu
    }

    return bot("editMessageReplyMarkup", data)


def send_photo_group(photo_urls, chat_id):
    if len(photo_urls) == 1 or len(photo_urls) > 10:
        return send_photo(photo_urls[0], chat_id)
    
    media = []
    for photo_url in photo_urls:
        media.append({
            "type": "photo",
            "media": photo_url
        })
    
    data = {
        "chat_id": chat_id,
        "media": media,
    }

    return bot("sendMediaGroup", data)


def delete_message(chat_id, message_id):
    data = {"chat_id": chat_id, "message_id": message_id}
    return bot("deleteMessage", data)
