# базовый парсер вакансий с уведомлениями в Telegram

Этот скрипт парсит сайт hh.ru на наличие вакансий по ключевым словам и отправляет уведомления в Telegram.

## Зависимости
Установите зависимости с помощью:
bash
pip install requests beautifulsoup4 python-telegram-bot

## Настройка
1. Получите токен бота Telegram и chat_id.
2. Вставьте их в переменные `TELEGRAM_BOT_TOKEN` и `TELEGRAM_CHAT_ID`.

## Запуск

python parser.py

## Пример использования
Просто запустите скрипт, и он отправит подходящие вакансии в Telegram.
