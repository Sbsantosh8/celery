from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_scheduled_email(subject, message, from_email, recipient_list):
    """
    Sends an email asynchronously.

    Args:
        subject (str): The subject of the email.
        message (str): The body of the email.
        from_email (str): Sender's email address.
        recipient_list (list): List of recipient email addresses.
    """
    print('Email sent successfully before !')
    send_mail(subject, message, from_email, recipient_list)
    print('Email sent successfully after ..!')
    return "Email sent successfully."
