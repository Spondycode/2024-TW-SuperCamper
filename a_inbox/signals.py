from django.dispatch import receiver
from django.db.models.signals import post_save  # Import the post_save signal
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from .models import InboxMessage

@receiver(post_save, sender=InboxMessage)
def send_email(sender, instance, created, **kwargs):
    message = instance
    site_domain = Site.objects.get(pk=1).domain
    if created:
        for participant in message.conversation.participants.all():
            if participant != message.sender and participant.emailaddress_set.filter(primary=True, verified=True).exists():
                try:
                    email_address = participant.emailaddress_set.get(primary=True, verified=True)
                    email_subject = f'New message from {message.sender}'
                    email_body = f'Good news!\n You have a new message at {site_domain}.\n'
                    email = EmailMessage(email_subject, email_body, to=[email_address.email])
                    email.send()
                except Exception:
                    pass