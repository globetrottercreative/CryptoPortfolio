import requests

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
        print(url)
        r = requests.get(url)
        return r
    
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
        print(url)
        r = requests.get(url)
        return r

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
        print(url)
        r = requests.get(url)
        return r