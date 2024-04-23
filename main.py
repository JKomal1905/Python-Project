import time
from crypto_data import get_coins, Coin  # Assuming get_coins and coin are defined in crypto_data

def alert(symbol: str, bottom: float, top: float, coins_list: list[Coin]):
    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price > top or coin.current_price < bottom:
                print(coin, '!!TRIGGERED!!!')
            else:
                print(coin)

if __name__ == '__main__':
    while True:
        coins = get_coins()
        alert('btc', bottom=20_000, top=28_000, coins_list=coins)
        alert('eth', bottom=1800, top=1900, coins_list=coins)
        alert('xrp', bottom=0.47, top=0.48, coins_list=coins)
        time.sleep(30)
