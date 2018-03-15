from django.shortcuts import render, redirect
from profilemanager.forms import CreateUserForm

# Sign Up
def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
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