import vk_api
from telegram import Bot
from vk_api.longpoll import VkLongPoll, VkEventType
import datetime

# Токены
vk_token = 'YOUR_GROUP_VK_TOKEN'  # Токен группы ВКонтакте
tg_token = 'YOUR_TG_BOT_TOKEN'  # Токен бота Telegram
channel_username = 'YOUR_CHANNEL_USERNAME'  # Username канала в Telegram

# ID администратора (ваш ID ВКонтакте)
admin_id = 123456789  # Замените на ваш VK ID

# Инициализация VK API для группы
vk_session = vk_api.VkApi(token=vk_token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

# Инициализация Telegram API
bot = Bot(token=tg_token)

# Словарь для отслеживания количества отправленных песен
user_tracks_sent = {}

# Функция отправки музыки в Telegram канал
def send_music_to_telegram(music_url, music_title, artist_name):
    try:
        bot.send_audio(
            chat_id=f"@{channel_username}",
            audio=music_url,
            title=music_title,
            performer=artist_name
        )
    except Exception as e:
        print(f"Ошибка при отправке музыки в Telegram: {e}")

# Функция для проверки и ограничения отправки песен
def can_send_music(user_id):
    # Если пользователь - администратор, то не ограничиваем
    if user_id == admin_id:
        return True
    
    # Получаем текущее время
    current_date = datetime.date.today()
    
    # Если пользователь еще не отправлял песни сегодня, сбрасываем счетчик
    if user_id not in user_tracks_sent or user_tracks_sent[user_id]['date'] != current_date:
        user_tracks_sent[user_id] = {'count': 0, 'date': current_date}
    
    # Проверяем, не превышено ли ограничение
    if user_tracks_sent[user_id]['count'] < 20:
        return True
    return False

# Функция для обновления количества отправленных песен
def update_sent_tracks(user_id):
    if user_id not in user_tracks_sent:
        user_tracks_sent[user_id] = {'count': 0, 'date': datetime.date.today()}
    user_tracks_sent[user_id]['count'] += 1

# Прослушиваем события из группы ВКонтакте
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        # Проверка, есть ли вложения с музыкой
        if event.message['attachments']:
            music_count = 0
            for attachment in event.message['attachments']:
                if attachment['type'] == 'audio' and music_count < 10:
                    user_id = event.message['from_id']

                    # Проверка на возможность отправки музыки
                    if can_send_music(user_id):
                        music_url = attachment['audio']['url']
                        music_title = attachment['audio']['title']
                        artist_name = attachment['audio']['artist']
                        
                        # Отправка музыки в канал Telegram
                        send_music_to_telegram(music_url, music_title, artist_name)

                        # Обновляем количество отправленных треков
                        update_sent_tracks(user_id)

                        music_count += 1
                    else:
                        # Отправляем сообщение, что лимит на отправку треков превышен
                        vk.messages.send(
                            user_id=user_id,
                            message="Вы достигли лимита на отправку треков. Пожалуйста, попробуйте завтра."
                        )
