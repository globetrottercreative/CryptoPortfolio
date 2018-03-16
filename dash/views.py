from django.shortcuts import render, redirect
from profilemanager.models import UserProfile

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        profile = UserProfile.objects.get(django_user=request.user)
        data = {
            'Profile': profile,
        }

        #Return View
        return render(request, 'dash/homepage.html', data)