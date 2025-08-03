from environs import env


env.read_env()


class Settings:
    devman_token = env.str('DEVMAN_TOKEN')
    tg_token = env.str('TG_TOKEN')
    chat_id = env.str('CHAT_ID')


settings = Settings()
