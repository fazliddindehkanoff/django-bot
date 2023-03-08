from celery import shared_task
from celery.utils.log import get_task_logger

from visametric_bot.scraper import WebScraper
from visametric_bot.models import Customer
from visametric_bot.bot import send_message


logger = get_task_logger(__name__)


@shared_task
def send_notification():
    obj = WebScraper(Customer.objects.last())
    if obj.check_availability():
        send_message(
            "Schengen visaga bo'sh joy ochildi",
            1535815443,
        )
    else:
        print("There are no any awailable ")