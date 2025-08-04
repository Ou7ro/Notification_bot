import requests


def get_review_status(devman_token, timestamp):
    devman_url = 'https://dvmn.org/api/long_polling/'

    params = {'timestamp': timestamp} if timestamp else {}

    headers = {
        'Authorization': f'Token {devman_token}'
    }
    response = requests.get(url=devman_url,
                            timeout=100,
                            params=params,
                            headers=headers)
    response.raise_for_status()
    api_answer = response.json()
    return api_answer
