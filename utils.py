import json
import urllib.request
import config


class MarketFetchError(Exception):
    """Кастомная ошибка для сбоев сети или парсинга данных"""
    pass


def get_real_rates(last_known_rates: dict) -> dict:
    """Получает актуальные курсы. При сбое возвращает кэш (последние удачные курсы)."""
    try:
        with urllib.request.urlopen(config.URL, timeout=5) as response:
            raw_data = response.read().decode("utf-8")

        data = json.loads(raw_data)

        if "rates" not in data:
            raise MarketFetchError("Поле 'rates' отсутствует в ответе сервера.")

        new_rates = {}
        for code in config.SYMBOLS:
            if code not in data["rates"] and code != "EUR":
                raise MarketFetchError(f"Код {code} отсутствует в ответе сервера.")
            new_rates[code] = data["rates"].get(code, 1.0)

        return new_rates

    except Exception as e:
        print(f"⚠️  Не удалось получить курсы ({e}), используется кэш.")
        return last_known_rates if last_known_rates else config.FALLBACK_RATES.copy()


def convert_currency(amount: float, from_cur: str, to_cur: str, current_rates: dict) -> float:
    """Точный кросс-обмен через базовый EUR."""
    if from_cur not in current_rates or to_cur not in current_rates:
        raise ValueError("Неверный код валюты! Доступны: EUR, USD, SEK, GBP, PLN")
    if amount <= 0:
        raise ValueError("Сумма перевода должна быть больше нуля!")

    return round((amount / current_rates[from_cur]) * current_rates[to_cur], 2)