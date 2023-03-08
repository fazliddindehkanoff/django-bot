from datetime import datetime

def get_message(update):
    if not "message" in update:
        return None

    if "text" in update["message"]:
        return update["message"]["text"]
    else:
        return None

def get_message_id(update):
    if not "message" in update:
        return None

    if "text" in update["message"]:
        return update["message"]["message_id"]
    else:
        return None

def get_user_id(update):
    if "message" in update:
        return update["message"]["from"]["id"]
    elif "callback_query" in update:
        return update["callback_query"]["from"]["id"]


def get_callback_message_id(update):
    if "callback_query" in update:
        return update["callback_query"]["message"]["message_id"]
    else:
        return None

def get_callback_text(update):
    if "callback_query" in update:
        if "text" in update["callback_query"]["message"]:
            return update["callback_query"]["message"]["text"]
        else:
            return None
    else:
        return None


def get_callback_data(update):
    if "callback_query" in update:
        return update["callback_query"]["data"]
    else:
        return None
    
def is_date_available(date: str):
    try:
        return datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return False