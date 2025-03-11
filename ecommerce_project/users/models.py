from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models

class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname=models.CharField(max_length=100,null=True)
    lname=models.CharField(max_length=100,null=True)
    address = models.TextField()
    image = models.ImageField(upload_to='profile_img/',null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table='user_userprofile'

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()  # Fix to 'userprofile' instead of 'profile'
