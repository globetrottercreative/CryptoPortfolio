import requests, json
from rest_framework.views import APIView
from rest_framework.response import Response

'''
Expose Chart Data
'''
class ChartData(APIView):
    authentication_classes = ()
    permission_classes = ()

    def get(self, request, format=None):
        data = {
            'name': 'leon',
            'size': 14,
        }
        return Response(data)



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


'''
Takes a NZBCX Spot Price API URL, Returns JSON Package
'''
class BCX_GetMarketSummary():
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