from celery import shared_task
from django.core.mail import send_mail


from django.conf import settings
from twilio.rest import Client

@shared_task
def send_opt( opt, email):

    message = f"Votre code de vérification est : {opt} "
    subject = "Code de vérification"
    email= send_mail(subject, message, 'de pro@gmail.com', [email])
    return email



@shared_task
def send_otp_sms(phone_number, otp):

    client = Client(
        settings.TWILIO_ACCOUNT_SID,
        settings.TWILIO_AUTH_TOKEN
    )

    message = client.messages.create(
        body=f"Votre code de vérification est : {otp}",
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone_number
    )

    return message.sid