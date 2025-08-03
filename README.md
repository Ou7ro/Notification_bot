# Notification_bot

Этот бот отслеживает статус проверки работ на образовательной платформе Devman (dvmn.org) и присылает уведомления в Telegram:
- Когда работа проверена.

- Результат проверки (принята/есть замечания).

- Ссылку на проверенную работу.

## Зависимости
- Python3 должен быть установлен.
- При разработке был использован Python3.10. С версиями выше есть конфликт у python-telegram-bot.
- Затем используйте pip для установки зависимостей:
```
pip install -r requirements.txt
```
Для оповещений потребуется создать [telegram-бота](https://zabotov.ru/blog/tpost/f6y359fvf1-botfather-instruktsiya-po-sozdaniyu-i-na)

## Переменные окружения
Требуется создать файл `.env` и прописать следующие переменные окружения:
- DEVMAN_TOKEN
- TG_TOKEN
- CHAT_ID

`DEVMAN_TOKEN` можно получить по следующей [ссылке](https://dvmn.org/api/docs/). Нужен для взаимодействия с devman API

`TG_TOKEN` можно сгенерировать у [Отца Ботов](https://telegram.me/BotFather). Нужен для взаимодействия с ботом.

`CHAT_ID` инструкция по получению id чата [здесь](https://lumpics.ru/how-find-out-chat-id-in-telegram/). Нужен для отправки уведомлений в ваш личный чат.

## Запуск 
Для запуска требуется ввести в консоль

```
python main.py
```

## Пример работы
Если вы следовали инструкции, то при проверке вашей работы, придет уведомление такого формата.
<img width="687" height="288" alt="image" src="https://github.com/user-attachments/assets/b1f5d274-8b6c-472a-b7a6-4a94f91d2e75" />
