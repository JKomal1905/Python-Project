import json
import requests
from dataclasses import dataclass
from typing import Final


BASE_URL: Final[str] = 'http://api.coingecko.com/api/v3/coins/markets'


@dataclass
class Coin:
    name: str
    symbol: str
    current_price: float
    high_24h: float
    low_24h: float
    price_change_24h: float
    price_change_percentage_24h: float

    def __str__(self):
        return f'{self.name}({self.symbol}): €{self.current_price:,.2f}'


def get_coins() -> list[Coin]:
    payload: dict = {'vs_currency': 'eur', 'order': 'market_cap_desc'}
    response = requests.get(BASE_URL, params=payload)

    # Check if response is successful
    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}")
        return []

    try:
        json_data: list = response.json()
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {e}")
        print("Response content:", response.text)
        return []

    coin_list: list[Coin] = []
    for item in json_data:
        current_coin = Coin(
            name=item.get('name'),
            symbol=item.get('symbol'),
            current_price=item.get('current_price'),
            high_24h=item.get('high_24h'),
            low_24h=item.get('low_24h'),
            price_change_24h=item.get('price_change_24h'),
            price_change_percentage_24h=item.get('price_change_percentage_24h')
        )
        coin_list.append(current_coin)
    return coin_list


if __name__ == '__main__':
    coins = get_coins()
    for coin in coins:
        print(coin)
