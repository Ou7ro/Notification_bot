from services.devman_api import get_review_status
from config.logger import logger
from services.tg_bot import send_notification
from utils.formater import format_review_notification
from requests.exceptions import ReadTimeout, ConnectionError
from environs import env


env.read_env()


def main():
    logger.info('Запуск скрипта')

    devman_token = env.str('DEVMAN_TOKEN')
    tg_token = env.str('TG_TOKEN')
    chat_id = env.str('CHAT_ID')

    timestamp = None

    while True:
        try:
            api_answer = get_review_status(devman_token, timestamp)
            if api_answer.get('status') == 'timeout':
                timestamp = api_answer.get('timestamp_to_request')

                logger.debug(f'Запрос с новым timestamp {timestamp}')

            if api_answer.get('status') == 'found':
                logger.info("Найдены новые проверки!")

                timestamp = api_answer.get('last_attempt_timestamp')
                message = format_review_notification(api_answer)
                send_notification(tg_token, chat_id, message)

                logger.info(message)
        except ReadTimeout:
            continue
        except ConnectionError:
            logger.warning('Нет соединения с интернетом')


if __name__ == '__main__':
    main()
