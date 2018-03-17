from django.shortcuts import render, redirect
from profilemanager.models import UserProfile, ExchangesTraded
from dash.apis import IR_GetMarketSummary, Cry_GetMarketSummary, Coin_GetMarketSummary
from dash.models import SpotPrice, Exchange, Crypto
import json, requests
from django.utils import timezone

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        profile = UserProfile.objects.get(django_user=request.user)
        markets = ExchangesTraded.objects.get(user_id=profile)
        if (markets.exchange_one is None and 
            markets.exchange_two is None and 
            markets.exchange_three is None):
            print('NO EXCHANGES IN PROFILE')
        cryptos = Crypto.objects.all()
        
        for crypto in cryptos:
            '''
            Independant Reserve Spot Calls
            '''
            if (markets.exchange_one is not None and 
                markets.exchange_one.name == 'Independent Reserve'):
                r = IR_GetMarketSummary(markets.exchange_one.api_url, profile.currency, crypto.code_alt).run()
                # Clear DB of past Spot Data
                SpotPrice.objects.filter(source_data=markets.exchange_one.name, crypto=crypto).delete()
                #Convert Request Response
                response = r.json()

                # Put response data in DB
                sp = SpotPrice()
                sp.crypto = crypto
                sp.currency = profile.currency
                sp.timestamp = response['CreatedTimestampUtc']
                sp.source_api = markets.exchange_one.api_url
                sp.source_data = markets.exchange_one.name
                sp.avg_day = "%.2f" % response['CurrentLowestOfferPrice']
                sp.high_day = "%.2f" % response['DayHighestPrice']
                sp.low_day = "%.2f" % response['DayLowestPrice']
                sp.vol_crypto = 0
                sp.vol_currency = "%.2f" % response['DayVolumeXbt']
                sp.last_price = "%.2f" % response['LastPrice']
                sp.save()

            if (markets.exchange_two is not None and 
                markets.exchange_two.name == 'Independent Reserve'):
                r = IR_GetMarketSummary(markets.exchange_two.api_url, profile.currency, crypto.code_alt).run()
                # Clear DB of past Spot Data
                SpotPrice.objects.filter(source_data=markets.exchange_two.name, crypto=crypto).delete()
                #Convert Request Response
                response = r.json()

                # Put response data in DB
                sp = SpotPrice()
                sp.crypto = crypto
                sp.currency = profile.currency
                sp.timestamp = response['CreatedTimestampUtc']
                sp.source_api = markets.exchange_two.api_url
                sp.source_data = markets.exchange_two.name
                sp.avg_day = "%.2f" % response['CurrentLowestOfferPrice']
                sp.high_day = "%.2f" % response['DayHighestPrice']
                sp.low_day = "%.2f" % response['DayLowestPrice']
                sp.vol_crypto = 0
                sp.vol_currency = "%.2f" % response['DayVolumeXbt']
                sp.last_price = "%.2f" % response['LastPrice']
                sp.save()

            if (markets.exchange_three is not None and 
                markets.exchange_three.name == 'Independent Reserve'):
                r = IR_GetMarketSummary(markets.exchange_three.api_url, profile.currency, crypto.code_alt).run()
                # Clear DB of past Spot Data
                SpotPrice.objects.filter(source_data=markets.exchange_three.name, crypto=crypto).delete()
                #Convert Request Response
                response = r.json()

                # Put response data in DB
                sp = SpotPrice()
                sp.crypto = crypto
                sp.currency = profile.currency
                sp.timestamp = response['CreatedTimestampUtc']
                sp.source_api = markets.exchange_three.api_url
                sp.source_data = markets.exchange_three.name
                sp.avg_day = "%.2f" % response['CurrentLowestOfferPrice']
                sp.high_day = "%.2f" % response['DayHighestPrice']
                sp.low_day = "%.2f" % response['DayLowestPrice']
                sp.vol_crypto = 0
                sp.vol_currency = "%.2f" % response['DayVolumeXbt']
                sp.last_price = "%.2f" % response['LastPrice']
                sp.save()
            
            '''
            Cryptopia Spot Calls
            '''
            if (markets.exchange_one is not None and 
                markets.exchange_one.name == 'Cryptopia'):
                r = Cry_GetMarketSummary(markets.exchange_one.api_url, profile.currency_alt, crypto.code_alt).run()
                # Clear DB of past Spot Data
                SpotPrice.objects.filter(source_data=markets.exchange_one.name, crypto=crypto).delete()
                #Convert Request Response
                response = r.json()

                # Put response data in DB
                sp = SpotPrice()
                sp.crypto = crypto
                sp.currency = profile.currency
                sp.timestamp = timezone.now()
                sp.source_api = markets.exchange_one.api_url
                sp.source_data = markets.exchange_one.name
                sp.avg_day = "%.2f" % response['AskPrice']
                sp.high_day = "%.2f" % response['High']
                sp.low_day = "%.2f" % response['Low']
                sp.vol_crypto = "%.2f" % response['Volume']
                sp.vol_currency = "%.2f" % response['BaseVolume']
                sp.last_price = "%.2f" % response['LastPrice']
                sp.save()

            if (markets.exchange_two is not None and 
                markets.exchange_two.name == 'Cryptopia'):
                r = Cry_GetMarketSummary(markets.exchange_two.api_url, profile.currency_alt, crypto.code).run()
                
                # Clear DB of past Spot Data
                SpotPrice.objects.filter(source_data=markets.exchange_two.name, crypto=crypto).delete()
                #Convert Request Response
                f = r.json()
                response = f['Data']
                # Put response data in DB
                sp = SpotPrice()
                sp.crypto = crypto
                sp.currency = profile.currency
                sp.timestamp = timezone.now()
                sp.source_api = markets.exchange_two.api_url
                sp.source_data = markets.exchange_two.name
                sp.avg_day = "%.2f" % response['AskPrice']
                sp.high_day = "%.2f" % response['High']
                sp.low_day = "%.2f" % response['Low']
                sp.vol_crypto = "%.2f" % response['Volume']
                sp.vol_currency = "%.2f" % response['BaseVolume']
                sp.last_price = "%.2f" % response['LastPrice']
                sp.save()

            if (markets.exchange_three is not None and 
                markets.exchange_three.name == 'Cryptopia'):
                r = Cry_GetMarketSummary(markets.exchange_three.api_url, profile.currency, crypto.code_alt).run()
                # Clear DB of past Spot Data
                SpotPrice.objects.filter(source_data=markets.exchange_three.name, crypto=crypto).delete()
                #Convert Request Response
                response = r.json()

                # Put response data in DB
                sp = SpotPrice()
                sp.crypto = crypto
                sp.currency = profile.currency
                sp.timestamp = timezone.now()
                sp.source_api = markets.exchange_three.api_url
                sp.source_data = markets.exchange_three.name
                sp.avg_day = "%.2f" % response['AskPrice']
                sp.high_day = "%.2f" % response['High']
                sp.low_day = "%.2f" % response['Low']
                sp.vol_crypto = "%.2f" % response['Volume']
                sp.vol_currency = "%.2f" % response['BaseVolume']
                sp.last_price = "%.2f" % response['LastPrice']
                sp.save()
            
            '''
            CoinMarketCap Spot Calls
            '''
            cmc_conv1 = ''
            if crypto.code == 'ETH':
                cmc_conv1 = 'ethereum'
            elif crypto.code == 'BTC':
                cmc_conv1 = 'bitcoin'
            elif crypto.code == 'BCH':
                cmc_conv1 = 'bitcoincash'

            if (markets.exchange_one is not None and 
                markets.exchange_one.name == 'CoinMarketCap'):
                r = Coin_GetMarketSummary(markets.exchange_one.api_url, profile.currency_alt, cmc_conv1).run()
                # Clear DB of past Spot Data
                SpotPrice.objects.filter(source_data=markets.exchange_one.name, crypto=crypto).delete()
                #Convert Request Response
                response = r.json()

                # Put response data in DB
                sp = SpotPrice()
                sp.crypto = crypto
                sp.currency = profile.currency
                sp.timestamp = timezone.now()
                sp.source_api = markets.exchange_one.api_url
                sp.source_data = markets.exchange_one.name
                sp.avg_day = "%.2f" % response['price_nzd']
                sp.high_day = 0
                sp.low_day = 0
                sp.vol_crypto = 0
                sp.vol_currency = "%.2f" % response['24h_volume_nzd']
                sp.last_price = 0
                sp.save()

            if (markets.exchange_two is not None and 
                markets.exchange_two.name == 'CoinMarketCap'):
                r = Coin_GetMarketSummary(markets.exchange_two.api_url, profile.currency_alt, cmc_conv1).run()
                
                # Clear DB of past Spot Data
                SpotPrice.objects.filter(source_data=markets.exchange_two.name, crypto=crypto).delete()
                #Convert Request Response
         
                response = r.json()
                # Put response data in DB
                sp = SpotPrice()
                sp.crypto = crypto
                sp.currency = profile.currency
                sp.timestamp = timezone.now()
                sp.source_api = markets.exchange_one.api_url
                sp.source_data = markets.exchange_one.name
                sp.avg_day = "%.2f" % response['price_nzd']
                sp.high_day = 0
                sp.low_day = 0
                sp.vol_crypto = 0
                sp.vol_currency = "%.2f" % response['24h_volume_nzd']
                sp.last_price = 0
                sp.save()

            if (markets.exchange_three is not None and 
                markets.exchange_three.name == 'CoinMarketCap'):
                
                r = Coin_GetMarketSummary(markets.exchange_three.api_url, profile.currency, cmc_conv1).run()
                # Clear DB of past Spot Data
                SpotPrice.objects.filter(source_data=markets.exchange_three.name, crypto=crypto).delete()
                #Convert Request Response
                response = r.json()
                print(response)

                # Put response data in DB
                sp = SpotPrice()
                sp.crypto = crypto
                sp.currency = profile.currency
                sp.timestamp = timezone.now()
                sp.source_api = markets.exchange_one.api_url
                sp.source_data = markets.exchange_one.name
                sp.avg_day = "%.2f" % float(response['price_nzd'])
                sp.high_day = 0
                sp.low_day = 0
                sp.vol_crypto = 0
                sp.vol_currency = "%.2f" % response['24h_volume_nzd']
                sp.last_price = 0
                sp.save()

        _spots = SpotPrice.objects.all()
        _cryptos = Crypto.objects.all()
        _exchanges = Exchange.objects.all()

            
        data = {
            'cryptos': _cryptos,
            'exchanges': _exchanges,
            'Profile': profile,
            'spots': _spots,
        }

        #Return View
        return render(request, 'dash/homepage.html', data)