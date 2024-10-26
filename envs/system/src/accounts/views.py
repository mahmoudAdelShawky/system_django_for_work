from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth import login , logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            redirect('login')
            # return redirect('home')
    else:
        form = SignUpForm()
        # print("faild create you account!")
    
    return render(request, '../templates/register.html', {'form':form})



def logout_view(request):
    logout(request)
    return redirect('login')

def profile(request):
    return render(request, '../templates/profile.html')

