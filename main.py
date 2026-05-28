import os
#import utils


import config
from utils import get_real_rates, convert_currency


def display_rates(rates: dict) -> None:
    print("\n🎯 ТЕКУЩИЕ МЕЖДУНАРОДНЫЕ КУРСЫ:")
    print("========================================")
    for code, rate in rates.items():
        print(f"• 1 EUR = {rate:.4f} {code} ({config.SYMBOLS[code]})")
    print("========================================\n")


def start_forex_app():
    cached_rates = config.FALLBACK_RATES.copy()
    cached_rates = get_real_rates(cached_rates)

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        display_rates(cached_rates)

        action = input("Выбери: [1] Обновить курсы | [2] Обменять валюту | [3] Выход: ").strip()

        if action == "3":
            print("\nПрограмма закрыта!")
            break

        elif action == "1":
            print("\n🔄 Обновляю курсы...")
            cached_rates = get_real_rates(cached_rates)

        elif action == "2":
            try:
                from_c = input("Из какой валюты?: ").strip().upper()
                to_c = input("В какую валюту?: ").strip().upper()
                amount = float(input("Сколько меняем?: "))

                result = convert_currency(amount, from_c, to_c, cached_rates)

                sym_from = config.SYMBOLS.get(from_c, "")
                sym_to = config.SYMBOLS.get(to_c, "")

                print(f"\n🔥 РЕЗУЛЬТАТ ОБМЕНА:")
                print(f"{amount:.2f} {from_c} ({sym_from}) ===> {result:.2f} {to_c} ({sym_to})\n")

            except ValueError as error:
                print(f"\n❌ Ошибка ввода: {error}\n")

            input("Нажми Enter, чтобы вернуться в меню...")

        else:
            print("\n⚠️  Неизвестная команда. Введи 1, 2 или 3.\n")
            input("Нажми Enter, чтобы продолжить...")


if __name__ == "__main__":
    start_forex_app()