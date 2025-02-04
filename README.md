> [!WARNING]
> Проект находится ещё в разработке ! 

<img src="https://github.com/love-angelll/VKtoTG-Music/blob/main/Images/banner.png" alt="Банер" width="100%">

# VKtoTG Music 🎶 

Этот проект представляет собой бота ВКонтакте, который принимает музыку, отправленную в личные сообщения группы, и пересылает её в бота Telegram.

> [!WARNING]
> Бот имеет ограничение — до 20 треков в день.

---

## Содержание

1. [Описание проекта](#описание-проекта)
2. [Лицензия](#лицензия)
3. [Инструкция](#инструкция)
    - [Требования](./INSTALLATION.md#требования)
    - [Получение токенов](./INSTALLATION.md#получение-токенов)
    - [Настройка кода](./INSTALLATION.md#настройка-кода)
    - [Запуск](./INSTALLATION.md#запуск)
4. [Древо проекта](#древо-проекта)
5. [Автор](#автор)

---

## Описание проекта

Этот бот:
- Принимает аудиофайлы, отправленные в личные сообщения группы ВКонтакте.
- Пересылает их в наш Telegram бот.
- Ограничивает количество отправленных треков для обычных пользователей до 20 в день.
- У администратора (ID указывается в коде) нет ограничений.

---

## Лицензия

Проект распространяется под [MIT License](./LICENSE). Ознакомьтесь с условиями лицензии перед использованием.

---

## Инструкция

Полная инструкция по установке и настройке бота находится в файле [INSTALLATION.md](./INSTALLATION.md). В инструкции описано:
- Как установить необходимые библиотеки.
- Как получить токены для ВКонтакте и Telegram.
- Как настроить и запустить бота.

---

## Древо проекта

```plaintext
main
├────────────────
├── LICENSE            # Условия использования
├── README.md          # Краткое описание проекта
└── INSTALLATION.md    # Полная инструкция по установке и настройке

main/Code
├────────────────
├── main.py            # Основной код бота 
├──
└──

main/Images
├────────────────
├──
├──
└──
```

## Автор 

Иван Фрунза — [![GitHub](https://img.shields.io/badge/GitHub-love--angelll?style=plastic&logo=github)](https://github.com/love-angelll)

<!-- 
Разбор кода:

https://img.shields.io – сервис для создания значков (badges).
badge=GitHub-love--angelll-181717 – текст на кнопке.
style=for-the-badge – стиль кнопки (можно менять на flat, plastic, flat-square).
logo=github – логотип GitHub.
Ссылка – ведёт на профиль love-angelll.
-->
