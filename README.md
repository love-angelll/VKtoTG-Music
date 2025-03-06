<img src="https://github.com/love-angelll/VKtoTG-Music/blob/main/Images/banner.png" alt="Банер" width="100%">

# VKtoTG Music 🎶 

**VKtoTG Music** — это уникальный бот, который позволяет интегрировать вашу группу ВКонтакте с Telegram. Бот принимает аудиофайлы, отправленные в личные сообщения вашей группы ВКонтакте, и пересылает их в ваш Telegram-бот. Это позволяет легко переносить музыку из ВКонтакте в Telegram и поддерживает различные функциональные ограничения для обычных пользователей и администраторов.

### Основные функции бота:
- **Прием аудиофайлов**: Бот принимает аудиофайлы, отправленные в личные сообщения группы ВКонтакте.
- **Пересылка в Telegram**: Отправленные аудиофайлы пересылаются в Telegram-бот.
- **Ограничения для пользователей**: Обычные пользователи могут отправлять не более 20 треков в день. Для администраторов этих ограничений нет.
- **Привязка Telegram-аккаунта**: Для подключения к боту в Telegram необходимо отправить одноразовый ключ, который вы получите после отправки команды `/reg` в личные сообщения группы ВКонтакте.
- **Сброс ключа**: Пользователи могут запросить новый ключ до 5 раз в месяц. После достижения лимита, пользователь получает сообщение, что необходимо связаться с администратором.

### Почему вам стоит использовать этого бота?
- Легкая интеграция ВКонтакте и Telegram для музыкальных файлов.
- Гибкая настройка прав для администраторов и обычных пользователей.
- Простота использования с командой для привязки аккаунтов и сбросом ключей.
- Удобный интерфейс и возможность контроля за количеством отправленных треков.

## Функционал бота

1. **Прием аудиофайлов**:
   - Бот принимает только аудиофайлы (mp3 и другие поддерживаемые форматы), которые отправляются в личные сообщения группы ВКонтакте.
   - Каждый аудиофайл, полученный от пользователя, автоматически пересылается в Telegram.

2. **Ограничения для обычных пользователей**:
   - Пользователь может отправить не более 20 аудиофайлов в день.
   - Если количество отправленных треков достигает лимита, бот уведомит пользователя, что лимит на отправку музыки исчерпан.

3. **Отсутствие ограничений для администраторов**:
   - Администраторы, указанные в файле `adm.json`, могут отправлять неограниченное количество аудиофайлов.
   - Они могут обрабатывать любые запросы пользователей без ограничений.

4. **Привязка Telegram-аккаунта**:
   - Чтобы начать использовать бота в Telegram, пользователю нужно в личные сообщения группы ВКонтакте отправить команду `/reg`.
   - Бот сгенерирует одноразовый ключ, который нужно ввести в Telegram-бота для привязки.
   - После привязки аккаунта в Telegram, все последующие аудиофайлы будут пересылаться в Telegram для пользователя.

5. **Сброс ключа**:
   - Каждый пользователь может запросить новый ключ для привязки до 5 раз в месяц.
   - Для сброса ключа достаточно отправить команду `/reg` в личные сообщения группы ВКонтакте.
   - Если пользователь превышает лимит, бот уведомит его, что нужно связаться с администратором для получения нового ключа.


Этот проект предоставляет удобное решение для обмена музыкальными файлами между ВКонтакте и Telegram с возможностью управления правами пользователей и гибкой настройкой.
 

> [!WARNING]
> ПРОЕКТ НАХОДИТСЯ ЕЩЁ В РАЗРАБОТКЕ !  

> [!IMPORTANT]
> Бот имеет ограничение — до 20 треков в день.

## Лицензия

Проект распространяется под [MIT License](./LICENSE). Ознакомьтесь с условиями лицензии перед использованием.

## Инструкция

Полная инструкция по установке и настройке бота находится в файле [INSTALLATION.md](./INSTALLATION.md). В инструкции описано:
- Как установить необходимые библиотеки.
- Как получить токены для ВКонтакте и Telegram.
- Как настроить и запустить бота.


## Автор 

[![GitHub](https://img.shields.io/badge/GitHub-Ivan--Frunza-%2312101C?style=for-the-badge&logo=github&logoColor=white)](https://github.com/love-angelll)
[![Telegram](https://img.shields.io/badge/Telegram-iv__frunza-%2312101C?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/iv_frunza)
[![Instagram](https://img.shields.io/badge/Instagram-iv.frunza-%2312101C?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/iv.frunza/)



<!-- 
Разбор кода:

https://img.shields.io – сервис для создания значков (badges).
badge=GitHub-love--angelll-181717 – текст на кнопке.
style=for-the-badge – стиль кнопки (можно менять на flat, plastic, flat-square).
logo=github – логотип GitHub.
Ссылка – ведёт на профиль love-angelll.
-->
