from django.contrib import admin
from profilemanager.models import UserProfile, Wallet, ExchangesTraded

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Wallet)
admin.site.register(ExchangesTraded)