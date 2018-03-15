from django.shortcuts import render, redirect
from profilemanager.forms import CreateUserForm, EditProfileForm, EditWalletForm
from profilemanager.models import UserProfile, Wallet

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

    #Check if GET or POST
    if request.method == 'POST':
        #Check what form made the POST
        if 'profile_post_button' in request.POST:
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('/editprofile/')
            else:
                print('DEAD PROFILE FORM (SAVE)')
        else:
            wallets = Wallet.objects.filter(user_id=request.user.pk)
            #Find the wallet that the POST object references
            for wallet in wallets:
                wal_id = str(wallet.pk) + '_button'
                if wal_id in request.POST:
                    profile = UserProfile.objects.get(django_user=request.user)
                    wallet = Wallet.objects.get(id=wallet.id)
                    #Pass the matched wallet id as a custom form arg so the form can save the correct wallet record
                    wal = EditWalletForm(request.POST, myid=wallet.pk, instance=profile)
                    if wal.is_valid():
                        wal.save()
                        return redirect('/editprofile/')
                    else:
                        print('DEAD WALLET FORM (SAVE)')

    else:
        profile = UserProfile.objects.get(django_user=request.user)
        wallets = Wallet.objects.filter(user_id=request.user.pk)
        Wallet_forms = {}
        if len(wallets) > 0:
            for wallet in wallets:
                wallet_form = EditWalletForm(initial={
                    'name': wallet.name,
                    'ethereum': wallet.ethereum,
                    'bitcoin': wallet.bitcoin,
                    'bitcoincash': wallet.bitcoincash,
                    }, myid=wallet.pk)

                Wallet_forms.update({wallet.id: wallet_form})
        
        form = EditProfileForm(initial={
            'currency': profile.currency,
            'firstname': profile.firstname,
            'lastname': profile.lastname,
            'email': profile.django_user.email,
            })
        data = {
            'form': form,
            'wallet_forms': Wallet_forms,
            'wallets': wallets,
            'user': request.user
        }
        return render(request, 'profilemanager/editprofile.html', data)