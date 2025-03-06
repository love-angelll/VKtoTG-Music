import json
import random
import string
from vk_api import VkApi, VkUpload
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Загрузка данных из файлов
with open('adm.json', 'r') as f:
    admins = json.load(f)

with open('keys.json', 'r') as f:
    user_data = json.load(f)

# Функция для генерации случайного ключа
def generate_key():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

# ВКонтакте бот
class VKBot:
    def __init__(self, token, tg_bot_token):
        self.vk_session = VkApi(token=token)
        self.vk = self.vk_session.get_api()
        self.upload = VkUpload(self.vk_session)
        self.tg_bot = Bot(token=tg_bot_token)
        
    def handle_message(self, event):
        user_id = event.obj.message['from_id']
        text = event.obj.message['text']

        # Проверка на команду /reg
        if text.lower() == '/reg':
            self.reset_key(user_id)
            self.vk.messages.send(
                user_id=user_id,
                message="Вы запросили новый ключ для привязки. Используйте его в Telegram.",
                random_id=0
            )
            return

        # Проверка на наличие аудио
        if 'attachments' in event.obj.message:
            attachments = event.obj.message['attachments']
            for attachment in attachments:
                if attachment['type'] == 'audio':
                    audio_url = attachment['audio']['url']
                    if user_id not in user_data:
                        user_data[user_id] = {'count': 0, 'key': '', 'tg_id': None}

                    # Ограничение на количество треков для обычных пользователей
                    if user_data[user_id]['count'] >= 20:
                        self.vk.messages.send(
                            user_id=user_id,
                            message="Вы достигли лимита отправки треков на сегодня.",
                            random_id=0
                        )
                    else:
                        # Отправка аудио в Telegram
                        if user_data[user_id]['tg_id']:
                            self.tg_bot.send_audio(
                                chat_id=user_data[user_id]['tg_id'],
                                audio=audio_url
                            )
                            user_data[user_id]['count'] += 1
                            self.save_user_data()
                        else:
                            self.vk.messages.send(
                                user_id=user_id,
                                message="Для привязки с Telegram, используйте команду /reg.",
                                random_id=0
                            )
                    
    def reset_key(self, user_id):
        # Перегенерация ключа
        if user_id not in user_data:
            user_data[user_id] = {'count': 0, 'key': '', 'tg_id': None}
        
        if 'keys_reset' not in user_data[user_id]:
            user_data[user_id]['keys_reset'] = 0

        if user_data[user_id]['keys_reset'] < 5:
            user_data[user_id]['key'] = generate_key()
            user_data[user_id]['keys_reset'] += 1
            self.save_user_data()

            # Отправка ключа в ВКонтакте
            self.vk.messages.send(
                user_id=user_id,
                message=f"Ваш новый ключ для привязки: {user_data[user_id]['key']}",
                random_id=0
            )
        else:
            self.vk.messages.send(
                user_id=user_id,
                message="Вы превысили лимит запросов ключа на месяц. Пожалуйста, свяжитесь с администратором.",
                random_id=0
            )
            
    def save_user_data(self):
        with open('keys.json', 'w') as f:
            json.dump(user_data, f, indent=4)

# Telegram бот
def tg_start(update, context):
    update.message.reply_text("Привет! Отправьте свой ключ из ВКонтакте для привязки.")

def tg_handle_message(update, context):
    user_id = update.message.from_user.id
    text = update.message.text.strip()

    # Проверка на ключ
    if user_id not in user_data or not user_data[user_id]['key']:
        update.message.reply_text("Прежде чем отправлять музыку, привяжите свой аккаунт, отправив ключ из ВКонтакте.")
        return

    if user_data[user_id]['key'] == text:
        user_data[user_id]['tg_id'] = update.message.chat.id
        update.message.reply_text(f"Привязка успешна! Ваш ID ВКонтакте: {user_id}, Имя: {update.message.from_user.full_name}")
        vk_bot.vk.messages.send(
            user_id=user_id,
            message="Ваш аккаунт успешно привязан к Telegram. Теперь вы можете отправлять музыку.",
            random_id=0
        )
        vk_bot.save_user_data()

# Запуск ВКонтакте бота
vk_token = "VK_TOKEN"
tg_token = "TG_BOT_TOKEN"

vk_bot = VKBot(vk_token, tg_token)

# Подключаем слушатель ВКонтакте
vk_bot.vk_session.method('messages.setActivity', {'type': 'typing'})

# Запуск Telegram бота
updater = Updater(token=tg_token, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", tg_start))
dispatcher.add_handler(MessageHandler(Filters.text, tg_handle_message))

updater.start_polling() 
