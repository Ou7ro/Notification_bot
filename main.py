from services.devman_api import get_review_status
from config.logger import logger
from config.settings import settings
from services.tg_bot import send_notification
from utils.formater import format_review_notification


def main():
    logger.info('Запуск скрипта')
    timestamp = None

    while True:
        api_answer = get_review_status(timestamp)
        if api_answer.get('status') == 'timeout':
            timestamp = api_answer.get('timestamp_to_request')

            logger.debug(f'Запрос с новым timestamp {timestamp}')

        if api_answer.get('status') == 'found':
            logger.info("Найдены новые проверки!")

            timestamp = api_answer.get('last_attempt_timestamp')
            message = format_review_notification(api_answer)
            send_notification(settings.tg_token, settings.chat_id, message)

            logger.info(message)


if __name__ == '__main__':
    main()
