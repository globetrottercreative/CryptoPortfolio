from celery.task.schedules import crontab
from celery.decorators import periodic_task
from dash.models import SpotPrice, Exchange, Crypto, FiatCurrency
from dash.apis import IR_GetMarketSummary, Cry_GetMarketSummary, Coin_GetMarketSummary

@periodic_task(run_every=(crontab(minute='*/1')), name="some_task", ignore_result=True)
def get_crypto_avg_update_coinmarketcap():
    _Cryptos = Crypto.objects.all()
    _CoinMarketCap = Exchange.objects.filter(name='CoinMarketCap')
    _FiatCurrencies = FiatCurrency.objects.all()

    for crypto in _Cryptos:
        coin_code = ''
        if crypto.code == 'ETH':
            coin_code = 'ethereum'
        elif crypto.code == 'BTC':
            coin_code = 'bitcoin'
        elif crypto.code == 'BCH':
            coin_code = 'bitcoin-cash'

        for fiat in _FiatCurrencies:
            response = Coin_GetMarketSummary(_CoinMarketCap.api_url, fiat, coin_code).run()

            crypto.cmc_marketcap = "{0:,.0f}".format(float(response['market_cap_nzd']))
            crypto.rank = response['rank']
            crypto.cmc_pct_change24 = response['percent_change_24h']
            crypto.cmc_pct_change7d = response['percent_change_7d']
            crypto.cmc_total_sply = "{0:,.0f}".format(float(response['total_supply']))
            crypto.cmc_avg_price = "{0:,.2f}".format(float(response['price_nzd']))
            crypto.save();