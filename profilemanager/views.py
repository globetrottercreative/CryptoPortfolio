from django.shortcuts import render, redirect
from profilemanager.forms import CreateUserForm

# Sign Up
def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print('VALID')
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
            print('BAD FORM')
    else:
        profile = UserProfile.objects.get(base_user=request.user)
        form = EditProfileForm(initial={
            'base_fiat': profile.base_fiat,
            'first_name': profile.base_user.first_name,
            'last_name': profile.base_user.last_name,
            'email': profile.base_user.email,
            'cc_ETH': profile.cc_ETH,
            'cc_BTC': profile.cc_BTC,
            'cc_LTC': profile.cc_LTC,
            'cc_BCH': profile.cc_BCH,
            })
        data = {
            'form': form,
            'user': request.user
        }
        return render(request, 'dashboard/editprofile.html', data)