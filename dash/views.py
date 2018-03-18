from django.shortcuts import render, redirect
from profilemanager.models import UserProfile
from dash.apis import IR_GetMarketSummary, Cry_GetMarketSummary, Coin_GetMarketSummary
from dash.models import SpotPrice, Exchange, Crypto, CryptoAverage
from django.utils import timezone

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        profile = UserProfile.objects.get(django_user=request.user)
        
        _spots = SpotPrice.objects.all()
        _cryptos = Crypto.objects.all()
        _cryp_avgs = CryptoAverage.objects.all()
        _exchanges = Exchange.objects.all()

        data = {
            'cryp_avgs': _cryp_avgs,
            'cryptos': _cryptos,
            'exchanges': _exchanges,
            'Profile': profile,
            'spots': _spots,
        }

        #Return View
        return render(request, 'dash/homepage.html', data)