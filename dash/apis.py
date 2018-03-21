import requests, json
from rest_framework.views import APIView
from rest_framework.response import Response
from dash.models import HourlyPrice, Crypto, FiatCurrency, Exchange, SpotPrice, CryptoAverage
from profilemanager.models import UserProfile
from datetime import datetime, timedelta
import calendar, time

'''
Expose Chart Data
'''
class ChartData(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, format=None):
        _crypts = Crypto.objects.all()
        nz_eth_dates = []
        nz_eth_data = []
        nz_btc_dates = []
        nz_btc_data = []
        nz_bch_dates = []
        nz_bch_data = []
        for cryp in _crypts:
            _data = HourlyPrice.objects.filter(
                    crypto=cryp,
                    currency='NZD',
                    source_data='CryptoCompare',
                )
            if cryp.code == 'ETH':
                for pnt in _data:
                    nz_eth_dates.append(pnt.day_end.date())
                    nz_eth_data.append(pnt.avg_price)
            elif cryp.code == 'BTC':
                for pnt in _data:
                    nz_btc_dates.append(pnt.day_end.date())
                    nz_btc_data.append(pnt.avg_price)
            elif cryp.code == 'BCH':
                for pnt in _data:
                    nz_bch_dates.append(pnt.day_end.date())
                    nz_bch_data.append(pnt.avg_price)
        data = {
            'nz_eth_data': nz_eth_data,
            'nz_eth_dates': nz_eth_dates,
            'nz_btc_data': nz_btc_data,
            'nz_btc_dates': nz_btc_dates,
            'nz_bch_data': nz_bch_data,
            'nz_bch_dates': nz_bch_dates,
        }
        return Response(data)

'''
Expose CMC Data
'''
class CMCData(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, format=None):
        _Cryptos = Crypto.objects.all()
        _CMC = Exchange.objects.get(idkey='CMC')
        cmc_eth = {}
        cmc_btc = {}
        cmc_bch = {}
        for cryp in _Cryptos:
            try:
                crypto = CryptoAverage.objects.get(crypto=cryp, fiat='NZD')
                if cryp.code == 'ETH':
                    cmc_eth['marketcap'] = crypto.cmc_marketcap
                    cmc_eth['change24'] = crypto.cmc_pct_change24
                    cmc_eth['change7'] = crypto.cmc_pct_change7d
                    cmc_eth['supply'] = crypto.cmc_total_sply
                    cmc_eth['price'] = crypto.cmc_avg_price
                elif cryp.code == 'BTC':
                    cmc_btc['marketcap'] = crypto.cmc_marketcap
                    cmc_btc['change24'] = crypto.cmc_pct_change24
                    cmc_btc['change7'] = crypto.cmc_pct_change7d
                    cmc_btc['supply'] = crypto.cmc_total_sply
                    cmc_btc['price'] = crypto.cmc_avg_price
                elif cryp.code == 'BCH':
                    cmc_bch['marketcap'] = crypto.cmc_marketcap
                    cmc_bch['change24'] = crypto.cmc_pct_change24
                    cmc_bch['change7'] = crypto.cmc_pct_change7d
                    cmc_bch['supply'] = crypto.cmc_total_sply
                    cmc_bch['price'] = crypto.cmc_avg_price
            except:
                print('CMC Data ERROR')
        data = {
            'cmc_eth': cmc_eth,
            'cmc_btc': cmc_btc,
            'cmc_bch': cmc_bch,
        }
        return Response(data)

'''
Expose Spot Data
'''
class SpotData(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, format=None):
        eth_ir = {}
        btc_ir = {}
        bch_ir = {}
        eth_cry = {}
        btc_cry = {}
        bch_cry = {}

        _Cryptos = Crypto.objects.all()
        _Exchanges = Exchange.objects.all()
        for crypto in _Cryptos:
            for exchange in _Exchanges:
                    try:
                        updated = SpotPrice.objects.get(crypto=crypto, source_data=exchange.name, currency='NZD')
                        print(updated)
                        if crypto.code == 'ETH' and exchange.idkey == 'IR':
                            eth_ir['high'] = updated.high_day
                            eth_ir['low'] = updated.low_day
                            eth_ir['price'] = updated.avg_day
                        elif crypto.code == 'BTC' and exchange.idkey == 'IR':
                            btc_ir['high'] = updated.high_day
                            btc_ir['low'] = updated.low_day
                            btc_ir['price'] = updated.avg_day
                        elif crypto.code == 'BCH' and exchange.idkey == 'IR':
                            bch_ir['high'] = updated.high_day
                            bch_ir['low'] = updated.low_day
                            bch_ir['price'] = updated.avg_day
                        elif crypto.code == 'ETH' and exchange.idkey == 'CRY':
                            eth_cry['high'] = updated.high_day
                            eth_cry['low'] = updated.low_day
                            eth_cry['price'] = updated.avg_day
                        elif crypto.code == 'BTC' and exchange.idkey == 'CRY':
                            btc_cry['high'] = updated.high_day
                            btc_cry['low'] = updated.low_day
                            btc_cry['price'] = updated.avg_day
                        elif crypto.code == 'BCH' and exchange.idkey == 'CRY':
                            bch_cry['high'] = updated.high_day
                            bch_cry['low'] = updated.low_day
                            bch_cry['price'] = updated.avg_day

                    except:
                        print('Not Found')
                    

        data = {
           'eth_ir': eth_ir,
           'btc_ir': btc_ir,
           'bch_ir': bch_ir,
           'eth_cry': eth_cry,
           'btc_cry': btc_cry,
           'bch_cry': bch_cry,
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


