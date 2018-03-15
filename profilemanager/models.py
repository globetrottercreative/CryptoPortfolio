from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

#Core Website User Data Model
class UserProfile(models.Model):
    django_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstname = models.CharField(max_length=100, default='')
    lastname = models.CharField(max_length=100, default='')
    currency = models.CharField(max_length=4, default='NZD')

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
    ethereum = models.FloatField(default=0)
    bitcoin = models.FloatField(default=0)
    bitcoincash = models.FloatField(default=0)

#Create Wallet on any UserProfile create event
def create_wallet(sender, **kwargs):
    if kwargs['created']:
        wallet = Wallet.objects.create(user_id=kwargs['instance'])
post_save.connect(create_wallet, sender=UserProfile)