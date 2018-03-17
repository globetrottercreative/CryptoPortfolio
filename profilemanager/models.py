from django.db import models
from dash.models import Exchange
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#Core Website User Data Model
class UserProfile(models.Model):
    django_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstname = models.CharField(max_length=100, default='New')
    lastname = models.CharField(max_length=100, default='User')
    currency = models.CharField(max_length=4, default='NZD')
    currency_alt = models.CharField(max_length=4, default='NZDT')

    def __str__(self):
        return self.firstname

#Create UserProfile on any Django:User create event
def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = UserProfile.objects.create(django_user=kwargs['instance'])
post_save.connect(create_profile, sender=User)


#Multi-Crypto Wallet Data Model
class Wallet(models.Model):
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=100, default='New Wallet')
    ethereum = models.FloatField(default=0)
    bitcoin = models.FloatField(default=0)
    bitcoincash = models.FloatField(default=0)
    def __str__(self):
        return self.name

#Create Wallet on any UserProfile create event
def create_wallet(sender, **kwargs):
    if kwargs['created']:
        wallet = Wallet.objects.create(user_id=kwargs['instance'])
post_save.connect(create_wallet, sender=UserProfile)

#User Trading Exchange Reference Model
class ExchangesTraded(models.Model):
    user_id = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)
    exchange_one = models.ForeignKey(Exchange, related_name='related_one', on_delete=models.CASCADE, blank=True, null=True)
    exchange_two = models.ForeignKey(Exchange, related_name='related_two', on_delete=models.CASCADE, blank=True, null=True)
    exchange_three = models.ForeignKey(Exchange, related_name='related_three', on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.user_id.firstname

#Create Wallet on any UserProfile create event
def create_trading_exchange(sender, **kwargs):
    if kwargs['created']:
        wallet = ExchangesTraded.objects.create(user_id=kwargs['instance'])
post_save.connect(create_trading_exchange, sender=UserProfile)