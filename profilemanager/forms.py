from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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