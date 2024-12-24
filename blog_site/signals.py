from .models import CustomUser
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.core.mail import send_mail

@receiver(post_save, sender=CustomUser)
def notify_user_status_change(sender, instance, created, **kwargs):
    if not created:
        if instance.is_blocked:
            subject = "Account Temporarily Blocked"
            message = f"Hello {instance.username},\n\nYour account has been Temporarily blocked, Kindly contact the Admin."
            try:
                send_mail(
                    subject,
                    message,
                    'kaasupanamkd@gmail.com',
                    [instance.email],
                    fail_silently=False,
                )
                print("====================")
                print("Blocked mail sent successfully")
                print("====================")
            except Exception as e:
                print(f"Error sending email:{e}")

@receiver(pre_delete, sender=CustomUser)
def notify_user_deletion(sender, instance, **kwargs):
    subject = "Account Deleted"
    message = f"Hello {instance.username},\n\nYour account has been deleted, Thank you for being with us"
    try:
        send_mail(
            subject,
            message,
            'kaasupanamkd@gmail.com',
            [instance.email],
            fail_silently=False,
        )
    except Exception as e:
        print(f"Error sending email:{e}")