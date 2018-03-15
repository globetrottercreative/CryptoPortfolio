from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        #Return View
        return render(request, 'dash/homepage.html', {})