from telegram.ext import Updater
from config.logger import logger


def send_notification(tg_token, chat_id, message):
    updater = Updater(token=tg_token)
    updater.bot.send_message(chat_id=chat_id, text=message)
    logger.info('Сообщение отправлено')
