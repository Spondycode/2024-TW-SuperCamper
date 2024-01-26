from django.dispatch import receiver
from django.db.models.signals import post_save  # Import the post_save signal
from django.contrib.auth.models import User  # Import the User model
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        Profile.objects.create(
            user=user,
            email=user.email
        )
        