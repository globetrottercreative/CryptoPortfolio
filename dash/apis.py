import requests, json
from rest_framework.views import APIView
from rest_framework.response import Response
from dash.models import HourlyPrice, Crypto, FiatCurrency
from datetime import datetime, timedelta
import calendar, time

'''
Expose Chart Data
'''
class ChartData(APIView):
    authentication_classes = ()
    permission_classes = ()
    ETH = Crypto.objects.get(code='ETH')
    BTC = Crypto.objects.get(code='BTC')
    BCH = Crypto.objects.get(code='BCH')

    def get(self, request, format=None):
        _crypts = Crypto.objects.all()
        _fiat = FiatCurrency.objects.all()
        nz_eth_dates = []
        nz_eth_data = []
        nz_btc_dates = []
        nz_btc_data = []
        nz_bch_dates = []
        nz_bch_data = []
        us_eth_dates = []
        us_eth_data = []
        us_btc_dates = []
        us_btc_data = []
        us_bch_dates = []
        us_bch_data = []
        for cryp in _crypts:
            for fiat in _fiat:
                _data = HourlyPrice.objects.filter(
                        crypto=cryp,
                        currency=fiat.code,
                        source_data='CryptoCompare',
                    )
                if cryp.code == 'ETH' and fiat.code == 'NZD':
                    for pnt in _data:
                        nz_eth_dates.append(pnt.day_end.date())
                        nz_eth_data.append(pnt.avg_price)
                elif cryp.code == 'ETH' and fiat.code == 'USD':
                    for pnt in _data:
                        us_eth_dates.append(pnt.day_end.date())
                        us_eth_data.append(pnt.avg_price)
                elif cryp.code == 'BTC' and fiat.code == 'NZD':
                    for pnt in _data:
                        nz_btc_dates.append(pnt.day_end.date())
                        nz_btc_data.append(pnt.avg_price)
                elif cryp.code == 'BTC' and fiat.code == 'USD':
                    for pnt in _data:
                        us_btc_dates.append(pnt.day_end.date())
                        us_btc_data.append(pnt.avg_price)
                elif cryp.code == 'BCH' and fiat.code == 'NZD':
                    for pnt in _data:
                        nz_bch_dates.append(pnt.day_end.date())
                        nz_bch_data.append(pnt.avg_price)
                elif cryp.code == 'BCH' and fiat.code == 'USD':
                    for pnt in _data:
                        us_bch_dates.append(pnt.day_end.date())
                        us_bch_data.append(pnt.avg_price)
        data = {
            'nz_eth_data': nz_eth_data,
            'nz_eth_dates': nz_eth_dates,
            'nz_btc_data': nz_btc_data,
            'nz_btc_dates': nz_btc_dates,
            'nz_bch_data': nz_bch_data,
            'nz_bch_dates': nz_bch_dates,
            'us_eth_data': us_eth_data,
            'us_eth_dates': us_eth_dates,
            'us_btc_data': us_btc_data,
            'us_btc_dates': us_btc_dates,
            'us_bch_data': us_bch_data,
            'us_bch_dates': us_bch_dates,
        }
        return Response(data)


'''
Takes a CryptoCompare API URL, Returns JSON Package
'''
class CC_GetMarketHistory():
    def __init__(self, url, cur, cyp):
        self._URL = url
        self.Crypto = cyp
        self.Currency = cur
    def run(self):
        url = self._URL
        url += 'data/histoday?fsym='
        url += self.Crypto
        url += '&tsym='
        url += self.Currency
        url += '&limit=60&aggregate=1'
        
        r = requests.get(url)
        return r.json()

'''
Takes a Independent Reserve Spot Price API URL, Returns JSON Package
'''
class IR_GetMarketSummary():
    def __init__(self, url, cur, cyp):
        self._URL = url
        self.Crypto = cyp
        self.Currency = cur

    def run(self):
            
        url = self._URL
        url += 'Public/GetMarketSummary'
        url += '?primaryCurrencyCode='
        url += self.Crypto
        url += '&secondaryCurrencyCode='
        url += self.Currency
        r = requests.get(url)
        return r.json()

'''
Takes a Independent Reserve Hourly Market History API URL, Returns JSON Package
'''
class IR_MarketHistorySummary():
    def __init__(self, url, cur, cyp, hours):
        self._URL = url
        self.Crypto = cyp
        self.Currency = cur
        self.Hours = hours

    def run(self):
            
        url = self._URL
        url += 'Public/GetTradeHistorySummary?primaryCurrencyCode='
        url += self.Crypto
        url += '&secondaryCurrencyCode='
        url += self.Currency
        url += '&numberOfHoursInThePastToRetrieve='
        url += str(self.Hours)
        r = requests.get(url)
        sub = r.json()
        return sub['HistorySummaryItems']

'''
Takes a Cryptopia Spot Price API URL, Returns JSON Package
'''

class Cry_GetMarketSummary():
    def __init__(self, url, cur, cyp):
        self._URL = url
        self.Crypto = cyp
        self.Currency = cur

    def run(self):
            
        url = self._URL
        url += 'GetMarket/'
        url += self.Crypto
        url += '_'
        url += self.Currency
        r = requests.get(url).json()
        return r['Data']

'''
Takes a CoinMarketCap Spot Price API URL, Returns JSON Package
'''
class Coin_GetMarketSummary():
    def __init__(self, url, cur, cyp_name):
        self._URL = url
        self.Crypto = cyp_name
        self.Currency = cur

    def run(self):
        url = self._URL
        url += self.Crypto
        url += '/?convert='
        url += self.Currency
        r = requests.get(url).json()
        j = r[0]
        return j


