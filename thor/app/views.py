from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


from datetime import timedelta
from django.utils.timezone import now
from app.tasks import send_scheduled_email

def schedule_email_view(request):
    subject = "Scheduled Email"
    message = "This email is sent asynchronously using Django Celery."
    sender_email = "your_email@example.com"
    recipient_emails = ["recipient1@example.com", "recipient2@example.com"]
    
    # Schedule the email to be sent after 5 minutes
    send_scheduled_email.apply_async(
        args=[subject, message, sender_email, recipient_emails],
        eta=now() + timedelta(minutes=5)
    )
    return HttpResponse("Email has been scheduled.")


from datetime import timedelta
from django.utils.timezone import now
from app.tasks import send_scheduled_email

def schedule_email_view(request):
    subject = "Scheduled Email"
    message = "This email is sent asynchronously using Django Celery."
    recipient_emails = ["recipient1@example.com", "recipient2@example.com"]
    
    # Schedule the email to be sent after 5 minutes
    send_scheduled_email.apply_async(
        args=[subject, message, recipient_emails],
        eta=now() + timedelta(minutes=5)
    )
    return HttpResponse("Email has been scheduled.")
