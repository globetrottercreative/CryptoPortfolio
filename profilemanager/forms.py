from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from profilemanager.models import UserProfile, Wallet

class CreateUserForm(UserCreationForm):
    print('n create form')
    email = forms.EmailField(required=True)
    class Meta():
        model = User
        fields = {
            'username',
            'email',
            'password1',
            'password2',
        }
    field_order = [
        'username',
        'email',
        'password1',
        'password2',]
    def save(self, commit=True):
            #Create Current Logged In User
            user = super(CreateUserForm, self).save(commit=False)

            #Change Native Logged In User Data
            user.first_name = ''
            user.last_name = ''
            user.email = self.cleaned_data['email']

            #Commit to DB
            if commit:
                user.save()

            return user

class EditProfileForm(forms.ModelForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    CURRENCY_CHOICES= [
        ('NZD', 'NZD'),
        ('USD', 'USD'),
        ]
    currency = forms.CharField(widget=forms.Select(choices=CURRENCY_CHOICES))
    class Meta():
        model = UserProfile
        fields = {
            'firstname',
            'lastname',
            'email',
            'currency',
            }
        labels = {
            'firstname': 'First Name',
            'lastname': 'First Name',
            'email': 'Email',
            'currency': 'Local Currency',
        }
    field_order = [
        'firstname',
        'lastname',    
        'email',  
        'currency',
        ]

    def save(self, commit=True):
        #Create Current Logged In User
        user = super(EditProfileForm, self).save(commit=False)

        #Edit Base User Profile
        user.first_name = self.cleaned_data['firstname']
        user.last_name = self.cleaned_data['lastname']
        user.email = self.cleaned_data['email']

        user.save()
        #Create New Data Model
        profile = UserProfile()

        #Fill Data Model With Form and Other Data
        profile.django_user = user
        profile.firstname = self.cleaned_data['firstname']
        profile.lastname = self.cleaned_data['lastname'] 
        profile.currency = self.cleaned_data['currency']
        if profile.currency == 'NZD':
            profile.currency_alt = 'NZDT'
        elif profile.currency == 'USD':
            profile.currency_alt = 'USDT'

        #Save To DB
        if commit:
            profile.save()
        else:
            print('COMMIT ERROR')

        return profile

class EditWalletForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.myid = kwargs.pop('myid')
        super(EditWalletForm, self).__init__(*args, **kwargs)

    class Meta():
        model = Wallet
        fields = {
            'name',
            'ethereum',
            'bitcoin',
            'bitcoincash',
            }
        labels = {
            'name': 'Wallet Name',
            'ethereum': 'Ethereum Holdings',
            'bitcoin': 'Bitcoin Holdings',
            'bitcoincash': 'Bitcoin Cash Holdings',
        }
    field_order = [
        'name',
        'ethereum',
        'bitcoin',
        'bitcoincash',
        ]

    def save(self, commit=True):
        #Save OneToOne Reference
        user = super(EditWalletForm, self).save(commit=False)
        user.save()

        #Get The Specific Wallet To Update
        #Uses custom form argument
        wallet = Wallet.objects.get(id=self.myid)

        #Fill Data Model With Form and Other Data
        wallet.user_id = self.instance
        wallet.name = self.cleaned_data['name']
        wallet.ethereum = self.cleaned_data['ethereum'] 
        wallet.bitcoin = self.cleaned_data['bitcoin']
        wallet.bitcoincash = self.cleaned_data['bitcoincash']

        #Save To DB
        if commit:
            wallet.save()
        else:
            print('COMMIT ERROR')

        return wallet     
