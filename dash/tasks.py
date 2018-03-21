from celery.task.schedules import crontab
from celery.decorators import periodic_task
from dash.models import SpotPrice, Exchange, Crypto, FiatCurrency, CryptoAverage, HourlyPrice
from dash.apis import IR_GetMarketSummary, Cry_GetMarketSummary, Coin_GetMarketSummary, CC_GetMarketHistory
from django.utils import timezone
from datetime import datetime

@periodic_task(run_every=(crontab(minute='*/1')), name="get_CMC", ignore_result=True)
def get_CMC():
    _Cryptos = Crypto.objects.all()
    _CoinMarketCap = Exchange.objects.get(name='CoinMarketCap')
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
            response = Coin_GetMarketSummary(_CoinMarketCap.api_url, fiat.code, coin_code).run()
            CryptoAverage.objects.filter(crypto=crypto, fiat=fiat.code).delete()
            cp = CryptoAverage()
            cp.fiat = fiat.code
            cp.crypto = crypto
            cp.cmc_marketcap = "{0:,.0f}".format(float(response['market_cap_'+fiat.code.lower()]))
            cp.rank = response['rank']
            cp.cmc_pct_change24 = response['percent_change_24h']
            cp.cmc_pct_change7d = response['percent_change_7d']
            cp.cmc_total_sply = "{0:,.0f}".format(float(response['total_supply']))
            cp.cmc_avg_price = "{0:,.2f}".format(float(response['price_'+fiat.code.lower()]))
            cp.save();

@periodic_task(run_every=(crontab(minute='*/1')), name="get_Exchs", ignore_result=True)
def get_Exchs():
    _Cryptos = Crypto.objects.all()
    _IndependentReserve = Exchange.objects.get(name='Independent Reserve')
    _Cryptopia = Exchange.objects.get(name='Cryptopia')
    _FiatCurrencies = FiatCurrency.objects.all()

    for crypto in _Cryptos:
        for fiat in _FiatCurrencies:
            IR_response = IR_GetMarketSummary(_IndependentReserve.api_url, fiat.code, crypto.code_alt).run()
            CRY_response = Cry_GetMarketSummary(_Cryptopia.api_url, fiat.code_alt, crypto.code).run()
            
            #After successful response, remove old DB values
            SpotPrice.objects.filter(crypto=crypto, currency=fiat.code).delete()

            # Put response data in DB
            sp = SpotPrice()
            sp.crypto = crypto
            sp.currency = fiat.code
            sp.timestamp = IR_response['CreatedTimestampUtc']
            sp.source_api = _IndependentReserve.api_url
            sp.source_data = _IndependentReserve.name
            sp.avg_day = "{0:,.2f}".format(IR_response['CurrentLowestOfferPrice'])
            sp.high_day = "{0:,.2f}".format(IR_response['DayHighestPrice'])
            sp.low_day = "{0:,.2f}".format(IR_response['DayLowestPrice'])
            sp.vol_crypto = 'N/A'
            sp.vol_currency = "{0:,.2f}".format(IR_response['DayVolumeXbt'])
            sp.last_price = "{0:,.2f}".format(IR_response['LastPrice'])
            sp.save()
    
            # Put response data in DB
            sp = SpotPrice()
            sp.crypto = crypto
            sp.currency = fiat.code
            sp.timestamp = timezone.now()
            sp.source_api = _Cryptopia.api_url
            sp.source_data = _Cryptopia.name
            sp.avg_day = "{0:,.2f}".format(CRY_response['AskPrice'])
            sp.high_day = "{0:,.2f}".format(CRY_response['High'])
            sp.low_day = "{0:,.2f}".format(CRY_response['Low'])
            sp.vol_crypto = "{0:,.2f}".format(CRY_response['Volume'])
            sp.vol_currency = "{0:,.2f}".format(CRY_response['BaseVolume'])
            sp.last_price = "{0:,.2f}".format(CRY_response['LastPrice'])
            sp.save()

@periodic_task(run_every=(crontab(minute=0, hour='*/12')), name="get_agg_Graph", ignore_result=True)
def get_agg_Graph():
    _Cryptos = Crypto.objects.all()
    _CryptoCompare = Exchange.objects.get(name='CryptoCompare')
    _FiatCurrencies = FiatCurrency.objects.all()

    for crypto in _Cryptos:
        for fiat in _FiatCurrencies:
            CC_response = CC_GetMarketHistory(_CryptoCompare.api_url, fiat.code, crypto.code).run()
            #After successful response, remove old DB values
            HourlyPrice.objects.filter(crypto=crypto, currency=fiat.code).delete()

            for point in CC_response['Data']:
                # Put response data in DB
                dp = HourlyPrice()
                dp.crypto = crypto
                dp.currency = fiat.code
                dp.avg_price = point['close']
                dp.day_start = timezone.make_aware(datetime.fromtimestamp(point['time']), timezone.get_current_timezone())
                dp.day_end = timezone.make_aware(datetime.fromtimestamp(point['time']), timezone.get_current_timezone())
                dp.source_api = _CryptoCompare.api_url
                dp.source_data = _CryptoCompare.name
                dp.open_value = point['open']
                dp.high_value = point['high']
                dp.low_value = point['low']
                dp.close_value = point['close']
                dp.volume = 0
                dp.save()
