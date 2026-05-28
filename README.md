# TerminalKawase
Kawase (為替) — A minimalist Python CLI currency converter featuring live API updates and smart data caching. Developed strictly for testing purposes

### 📝 Description
This repository contains a simple console-based currency converter application written in Python. It fetches real-time exchange rates for major currencies relative to the Euro (EUR) using a public API and provides an interactive CLI for currency exchange calculations.

> ⚠️ **Note:** This project is created **strictly for testing and demonstration purposes**.

### 🚀 Features
* **Real-time Rates:** Fetches live data from an external currency API.
* **Smart Fallback:** Uses local hardcoded rates if the network or API is unavailable.
* **Cross-Currency Exchange:** Allows conversion between any supported pairs (EUR, USD, SEK, GBP, PLN) via a base currency.
* **Clean Architecture:** Separated into configuration, utility functions, and main application logic.

### 🛠️ Project Structure
* `main.py` — The entry point of the CLI application.
* `config.py` — Contains API endpoints, currency symbols, and fallback rates.
* `utils.py` — Core logic for data fetching and exchange calculations.
* `main.spec` — PyInstaller specification file for compiling into an executable.

---
