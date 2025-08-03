import requests
from config.logger import logger
from config.settings import settings
from requests.exceptions import ReadTimeout, ConnectionError


def get_review_status(timestamp):
    devman_url = 'https://dvmn.org/api/long_polling/'

    params = {'timestamp': timestamp} if timestamp else {}

    headers = {
        'Authorization': f'Token {settings.devman_token}'
    }

    try:
        response = requests.get(url=devman_url,
                                timeout=100,
                                params=params,
                                headers=headers)
        response.raise_for_status()

        api_answer = response.json()
        return api_answer
    except ReadTimeout:
        logger.warning('Сервер не ответил в срок')
    except ConnectionError:
        logger.warning('Нет соединения с интернетом')
