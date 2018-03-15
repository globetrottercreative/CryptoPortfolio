from django.shortcuts import render, redirect
from profilemanager.forms import CreateUserForm, EditProfileForm
from profilemanager.models import UserProfile

# Sign Up
def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        else:
            print('DEAD FORM')
    else:
        form = CreateUserForm()
        data = {
            'form': form,
            'user': request.user,
        }
        return render(request, 'profilemanager/signup.html', data)

def editprofile(request):
    if not request.user.is_authenticated:
        return redirect('/');

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print('DEAD FORM')
    else:
        profile = UserProfile.objects.get(django_user=request.user)
        form = EditProfileForm(initial={
            'currency': profile.currency,
            'firstname': profile.firstname,
            'lastname': profile.lastname,
            'email': profile.django_user.email,
            })
        data = {
            'form': form,
            'user': request.user
        }
        return render(request, 'profilemanager/editprofile.html', data)