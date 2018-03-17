from django.shortcuts import render, redirect
from profilemanager.models import UserProfile, ExchangesTraded
from dash.apis import IR_GetMarketSummary, Cry_GetMarketSummary, Coin_GetMarketSummary
from dash.models import SpotPrice, Exchange, Crypto
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
                response = IR_GetMarketSummary(markets.exchange_one.api_url, profile.currency, crypto.code_alt).run()
                # Clear DB of past Spot Data
                SpotPrice.objects.filter(source_data=markets.exchange_one.name, crypto=crypto).delete()
                #Convert Request Response

                # Put response data in DB
                sp = SpotPrice()
                sp.crypto = crypto
                sp.currency = profile.currency
                sp.timestamp = response['CreatedTimestampUtc']
                sp.source_api = markets.exchange_one.api_url
                sp.source_data = markets.exchange_one.name
                sp.avg_day = "{0:,.2f}".format(response['CurrentLowestOfferPrice'])
                sp.high_day = "{0:,.2f}".format(response['DayHighestPrice'])
                sp.low_day = "{0:,.2f}".format(response['DayLowestPrice'])
                sp.vol_crypto = 0
                sp.vol_currency = "{0:,.2f}".format(response['DayVolumeXbt'])
                sp.last_price = "{0:,.2f}".format(response['LastPrice'])
                sp.save()

            if (markets.exchange_two is not None and 
                markets.exchange_two.name == 'Independent Reserve'):
                response = IR_GetMarketSummary(markets.exchange_two.api_url, profile.currency, crypto.code_alt).run()
                # Clear DB of past Spot Data
                SpotPrice.objects.filter(source_data=markets.exchange_two.name, crypto=crypto).delete()
                #Convert Request Response

                # Put response data in DB
                sp = SpotPrice()
                sp.crypto = crypto
                sp.currency = profile.currency
                sp.timestamp = response['CreatedTimestampUtc']
                sp.source_api = markets.exchange_two.api_url
                sp.source_data = markets.exchange_two.name
                sp.avg_day = "{0:,.2f}".format(response['CurrentLowestOfferPrice'])
                sp.high_day = "{0:,.2f}".format(response['DayHighestPrice'])
                sp.low_day = "{0:,.2f}".format(response['DayLowestPrice'])
                sp.vol_crypto = 0
                sp.vol_currency = "{0:,.2f}".format(response['DayVolumeXbt'])
                sp.last_price = "{0:,.2f}".format(response['LastPrice'])
                sp.save()

            if (markets.exchange_three is not None and 
                markets.exchange_three.name == 'Independent Reserve'):
                response = IR_GetMarketSummary(markets.exchange_three.api_url, profile.currency, crypto.code_alt).run()
                # Clear DB of past Spot Data
                SpotPrice.objects.filter(source_data=markets.exchange_three.name, crypto=crypto).delete()
                #Convert Request Response

                # Put response data in DB
                sp = SpotPrice()
                sp.crypto = crypto
                sp.currency = profile.currency
                sp.timestamp = response['CreatedTimestampUtc']
                sp.source_api = markets.exchange_three.api_url
                sp.source_data = markets.exchange_three.name
                sp.avg_day = "{0:,.2f}".format(response['CurrentLowestOfferPrice'])
                sp.high_day = "{0:,.2f}".format(response['DayHighestPrice'])
                sp.low_day = "{0:,.2f}".format(response['DayLowestPrice'])
                sp.vol_crypto = 0
                sp.vol_currency = "{0:,.2f}".format(response['DayVolumeXbt'])
                sp.last_price = "{0:,.2f}".format(response['LastPrice'])
                sp.save()
            
            '''
            Cryptopia Spot Calls
            '''
            if (markets.exchange_one is not None and 
                markets.exchange_one.name == 'Cryptopia'):
                response = Cry_GetMarketSummary(markets.exchange_one.api_url, profile.currency_alt, crypto.code_alt).run()
                # Clear DB of past Spot Data
                SpotPrice.objects.filter(source_data=markets.exchange_one.name, crypto=crypto).delete()
                #Convert Request Response

                # Put response data in DB
                sp = SpotPrice()
                sp.crypto = crypto
                sp.currency = profile.currency
                sp.timestamp = timezone.now()
                sp.source_api = markets.exchange_one.api_url
                sp.source_data = markets.exchange_one.name
                sp.avg_day = "{0:,.2f}".format(response['AskPrice'])
                sp.high_day = "{0:,.2f}".format(response['High'])
                sp.low_day = "{0:,.2f}".format(response['Low'])
                sp.vol_crypto = "{0:,.2f}".format(response['Volume'])
                sp.vol_currency = "{0:,.2f}".format(response['BaseVolume'])
                sp.last_price = "{0:,.2f}".format(response['LastPrice'])
                sp.save()

            if (markets.exchange_two is not None and 
                markets.exchange_two.name == 'Cryptopia'):
                response = Cry_GetMarketSummary(markets.exchange_two.api_url, profile.currency_alt, crypto.code).run()
                
                # Clear DB of past Spot Data
                SpotPrice.objects.filter(source_data=markets.exchange_two.name, crypto=crypto).delete()
                #Convert Request Response
                # Put response data in DB
                sp = SpotPrice()
                sp.crypto = crypto
                sp.currency = profile.currency
                sp.timestamp = timezone.now()
                sp.source_api = markets.exchange_two.api_url
                sp.source_data = markets.exchange_two.name
                sp.avg_day = "{0:,.2f}".format(response['AskPrice'])
                sp.high_day = "{0:,.2f}".format(response['High'])
                sp.low_day = "{0:,.2f}".format(response['Low'])
                sp.vol_crypto = "{0:,.2f}".format(response['Volume'])
                sp.vol_currency = "{0:,.2f}".format(response['BaseVolume'])
                sp.last_price = "{0:,.2f}".format(response['LastPrice'])
                sp.save()

            if (markets.exchange_three is not None and 
                markets.exchange_three.name == 'Cryptopia'):
                response = Cry_GetMarketSummary(markets.exchange_three.api_url, profile.currency, crypto.code_alt).run()
                # Clear DB of past Spot Data
                SpotPrice.objects.filter(source_data=markets.exchange_three.name, crypto=crypto).delete()
                #Convert Request Response

                # Put response data in DB
                sp = SpotPrice()
                sp.crypto = crypto
                sp.currency = profile.currency
                sp.timestamp = timezone.now()
                sp.source_api = markets.exchange_three.api_url
                sp.source_data = markets.exchange_three.name
                sp.avg_day = "{0:,.2f}".format(response['AskPrice'])
                sp.high_day = "{0:,.2f}".format(response['High'])
                sp.low_day = "{0:,.2f}".format(response['Low'])
                sp.vol_crypto = "{0:,.2f}".format(response['Volume'])
                sp.vol_currency = "{0:,.2f}".format(response['BaseVolume'])
                sp.last_price = "{0:,.2f}".format(response['LastPrice'])
                sp.save()
            
            '''
            Coinbase Spot Calls
            '''
            if (markets.exchange_one is not None and 
                markets.exchange_one.name == 'Coinbase'):
                response = Cbase_GetMarketSummary(markets.exchange_one.api_url, profile.currency_alt, cmc_conv1).run()
                # Clear DB of past Spot Data
                SpotPrice.objects.filter(source_data=markets.exchange_one.name, crypto=crypto).delete()
                #Convert Request Response

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
                markets.exchange_two.name == 'Coinbase'):
                response = Cbase_GetMarketSummary(markets.exchange_two.api_url, profile.currency_alt, cmc_conv1).run()
                
                # Clear DB of past Spot Data
                SpotPrice.objects.filter(source_data=markets.exchange_two.name, crypto=crypto).delete()
                #Convert Request Response
                # Put response data in DB
                sp = SpotPrice()
                sp.crypto = crypto
                sp.currency = profile.currency
                sp.timestamp = timezone.now()
                sp.source_api = markets.exchange_two.api_url
                sp.source_data = markets.exchange_two.name
                sp.avg_day = "%.2f" % response['price_nzd']
                sp.high_day = 0
                sp.low_day = 0
                sp.vol_crypto = 0
                sp.vol_currency = "%.2f" % response['24h_volume_nzd']
                sp.last_price = 0
                sp.save()

            if (markets.exchange_three is not None and 
                markets.exchange_three.name == 'Coinbase'):
                
                response = Cbase_GetMarketSummary(markets.exchange_three.api_url, profile.currency, cmc_conv1).run()
                # Clear DB of past Spot Data
                SpotPrice.objects.filter(source_data=markets.exchange_three.name, crypto=crypto).delete()
                #Convert Request Response
                # Put response data in DB
                
                sp = SpotPrice()
                sp.crypto = crypto
                sp.currency = profile.currency
                sp.timestamp = timezone.now()
                sp.source_api = markets.exchange_three.api_url
                sp.source_data = markets.exchange_three.name
                sp.avg_day = response['price_nzd']
                sp.high_day = 0
                sp.low_day = 0
                sp.vol_crypto = 0
                sp.vol_currency = response['24h_volume_nzd']
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