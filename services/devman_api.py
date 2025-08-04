import requests
from config.settings import settings


def get_review_status(timestamp):
    devman_url = 'https://dvmn.org/api/long_polling/'

    params = {'timestamp': timestamp} if timestamp else {}

    headers = {
        'Authorization': f'Token {settings.devman_token}'
    }
    response = requests.get(url=devman_url,
                            timeout=100,
                            params=params,
                            headers=headers)
    response.raise_for_status()
    api_answer = response.json()
    return api_answer
