from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm 
from django.contrib import messages
from .models import UserProfile
from products.models import Product
from .forms import  ProfileUpdateForm


def home(request):
    return render(request, 'users/home.html') 

# Profile view
@login_required
def profile(request):
    userprofile = UserProfile.objects.get(user=request.user)
    return render(request, 'users/profile.html',{'userprofile': userprofile})

@login_required
def profile_update(request):
    user_profile = request.user.userprofile
    
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)

        if p_form.is_valid():
            p_form.save() 
            return redirect('profile') 
    else:
        p_form = ProfileUpdateForm(instance=user_profile)

    context = {
        'p_form': p_form
    }
    return render(request, 'users/profile_update.html', context)