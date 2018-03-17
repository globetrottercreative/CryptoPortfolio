import requests, json

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
        print(r)
        j = r[0]
        return j

class Cbase_GetMarketSummary():
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
        print(r)
        j = r[0]
        return j