import requests
from pprint import pprint
from colorama import Fore, init
import json
import datetime
import time
from discord_webhook import DiscordWebhook, DiscordEmbed

link = 'https://api.binance.com/api/v3/ticker/price'

btc = {
    'symbol': 'BTCUSDT'
}
sol = {
    'symbol': 'SOLUSDT'
}
eth = {
    'symbol': 'ETHUSDT'
}


def call(link, param):
    try:

        a = requests.get(link, params=param)
        if a.status_code == 200:
            data = float(a.json()['price'])
            return data
    except:
        print(Fore.RED, 'Invalid link. Status code is not 200')
        return 0


def create_webhook():
    wh = DiscordWebhook(
        url='https://discord.com/api/webhooks/1031340802615558185/'
            'TNAyAobGCW7Ahc9SI7-UxyT1XqqI2oMKbafYtROUeey--5Xs4cZPw5S-jE__ugwufDJG',
        content=f'UPDATED AT {datetime.datetime.today().strftime("%H:%M:%S")} MSK',
        username='Vega'
    )
    embed = DiscordEmbed(color='03b2f8')
    embed.add_embed_field(name='BTC', value=f'{call(link, btc)}', inline=False)
    embed.add_embed_field(name='SOL', value=f'{call(link, sol)}', inline=False)
    embed.add_embed_field(name='ETH', value=f'{call(link, eth)}', inline=False)
    wh.add_embed(embed)
    response = wh.execute()
    while True:
        wh.remove_embeds()
        wh.content = f'UPDATED AT {datetime.datetime.today().strftime("%H:%M:%S")} MSK'
        embed = DiscordEmbed(color='03b2f8')
        embed.add_embed_field(name='BTC', value=f'{call(link, btc)}', inline=False)
        embed.add_embed_field(name='SOL', value=f'{call(link, sol)}', inline=False)
        embed.add_embed_field(name='ETH', value=f'{call(link, eth)}', inline=False)
        wh.add_embed(embed)
        sent_wh = wh.edit(response)
        time.sleep(5)


if __name__ == '__main__':
    create_webhook()
