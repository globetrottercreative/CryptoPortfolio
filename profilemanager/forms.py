from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from profilemanager.models import UserProfile

class CreateUserForm(UserCreationForm):
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
        ('AUD', 'AUD'),
        ]
    currency = forms.CharField(label='Base Fiat', widget=forms.Select(choices=CURRENCY_CHOICES))
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

        #Save To DB
        if commit:
            profile.save()
        else:
            print('COMMIT ERROR')

        return profile