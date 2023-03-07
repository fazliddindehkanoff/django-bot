from visametric_bot.models import Customer
from ..constants import *
def main_menu_keyboards():
    MAIN_MENU_BTNS = {
        "inline_keyboard":[
            [
                {"text": EXPRESS_VISA, "callback_data": EXPRESS_VISA_CALLBACK},
                {"text": MONTHLY_VISA, "callback_data": MONTHLY_VISA_CALLBACK},
            ]
        ]
    }
    
    return MAIN_MENU_BTNS

def navigation_keyboards():
    NAVIGATION_BTNS = {
        "inline_keyboard":[
            [
                {"text": TURN_ON, "callback_data": TURN_ON_CALLBACK_DATA},
                {"text": ADD_CLIENT, "callback_data": ADD_CLIENT_CALLBACK_DATA},
            ],
            [
                {"text": CLIENTS, "callback_data": CLIENTS_CALLBACK_DATA}
            ]
        ]
    }
    
    return NAVIGATION_BTNS

def get_clients(plan="monthly", back_btn=False, back_to=None):
    clients = Customer()
    clients = clients.get_all_customers(plan)
    markup = []
    for client in clients:
        markup.append(
            [
                {"text": client.get_full_name(), "callback_data": f"{client.pk}"},
                {"text": "✏️", "callback_data": f"action:edit-{client.pk}"},
                {"text": "❌", "callback_data": f"action:remove-{client.pk}"},
            ]
            
        )


    return {
        "inline_keyboard":markup
    }