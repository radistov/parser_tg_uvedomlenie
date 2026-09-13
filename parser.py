import requests
from bs4 import BeautifulSoup
import logging
from telegram import Bot

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Конфигурация
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"
URL = "https://hh.ru/search/vacancy?text=python&area=1"  # Пример URL для поиска вакансий на hh.ru
KEYWORDS = ["python", "разработчик", "junior"]  # Ключевые слова для фильтрации

# Инициализация бота Telegram
bot = Bot(token=TELEGRAM_BOT_TOKEN)

def parse_vacancies(url):
    """
    Парсит вакансии с сайта и возвращает список подходящих.
    """
    logger.info(f"Парсинг вакансий с {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    vacancies = []
    for vacancy in soup.find_all("div", class_="vacancy-serp-item-body"):  # Пример класса для hh.ru
        title = vacancy.find("a", class_="serp-item__title").text
        link = vacancy.find("a", class_="serp-item__title")["href"]
        description = vacancy.find("div", class_="g-user-content").text if vacancy.find("div", class_="g-user-content") else ""

        # Проверка на ключевые слова
        if any(keyword.lower() in title.lower() or keyword.lower() in description.lower() for keyword in KEYWORDS):
            vacancies.append({"title": title, "link": link, "description": description})

    logger.info(f"Найдено {len(vacancies)} вакансий")
    return vacancies

def send_to_telegram(vacancies):
    """
    Отправляет список вакансий в Telegram.
    """
    if not vacancies:
        logger.info("Нет подходящих вакансий")
        return

    for vacancy in vacancies:
        message = f"🏢 {vacancy['title']}\n🔗 {vacancy['link']}\n📝 {vacancy['description'][:100]}..."  # Обрезаем описание
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        logger.info(f"Отправлено сообщение в Telegram: {vacancy['title']}")

def main():
    """
    Основная функция для запуска парсера.
    """
    try:
        vacancies = parse_vacancies(URL)
        send_to_telegram(vacancies)
    except Exception as e:
        logger.error(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
