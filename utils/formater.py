import textwrap


def format_review_notification(api_answer: bool) -> str:
    attempt = api_answer.get('new_attempts')[0]
    lesson_title = attempt.get('lesson_title')
    lesson_url = attempt.get('lesson_url')

    if api_answer.get('is_negative'):
        answer_format = '''
            У вас проверили работу «{0}»
            {1}
            К сожалению, в работе нашлись ошибки.
        '''.format(lesson_title, lesson_url)
    else:
        answer_format = '''
            У вас проверили работу «{0}»
            {1}
            Преподавателю всё понравилось, можно приступать к следующему уроку!
        '''.format(lesson_title, lesson_url)
    return textwrap.dedent(answer_format)
