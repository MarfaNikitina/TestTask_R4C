from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.services import send_email_to_customer
from robots.models import Robot


@receiver(post_save, sender=Robot)
def send_mail_on_create(sender, created=None, instance=None, **kwargs):
    """Signal, that sends emails to customers
     at the moment of creating a robot from the waiting list."""
    if created:
        send_email_to_customer(instance.serial)
