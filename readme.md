# CryptoSentinel

A Django-based backend application designed to monitor cryptocurrency prices and serve as a central management hub for trading bots.

## Features
- **Real-time Data Retrieval**: Fetch live cryptocurrency prices using the Binance Public API.
- **Data Persistence**: Store historical price data in a structured SQLite database.
- **Admin Dashboard**: Comprehensive management interface to view and filter price logs.
- **Modular Architecture**: Built with scalability in mind, allowing for easy integration of automated trading strategies.

## Tech Stack
- **Framework**: Django 6.0
- **Language**: Python 3.12+
- **Database**: SQLite (Development)
- **External APIs**: Binance API via `requests`

## Installation

### 1. Clone the repository
```bash
git clone [https://github.com/BobSnopek/CryptoSentinel.git](https://github.com/BobSnopek/CryptoSentinel.git)
cd CryptoSentinel