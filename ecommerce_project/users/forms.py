from django import forms
from .models import UserProfile

# Profile update form for updating profile-related fields
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['fname','lname','address','image']
