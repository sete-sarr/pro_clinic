from celery import shared_task
from django.core.mail import send_mail, send_mass_mail
from django.utils import timezone
from .models import RendezVous
from datetime import timedelta


@shared_task
def notify_upcoming_appointments(rdv_id):

    try:
        rdv = RendezVous.objects.get(id=rdv_id)

        send_mail(
            'Rappel de rendez-vous',
            f'Bonjour, vous avez un rendez-vous prévu le {rdv.date}.',
            'from@example.com',
            [rdv.patient.email],
        )

        return f'Email envoyé à {rdv.patient.email}'

    except RendezVous.DoesNotExist:
        return "Rendez-vous introuvable"

    except Exception as e:
        return f'Erreur : {str(e)}'


@shared_task
def notify_upcoming_appointments_batch():

    now = timezone.now()
    tomorrow = now + timedelta(days=1)

    # 🎯 seulement les RDV de demain
    upcoming_rdvs = RendezVous.objects.select_related('patient').filter(
    date__date=tomorrow.date())

    messages = []

    for rdv in upcoming_rdvs:
        if rdv.patient.email:  # ✅ sécurité

            messages.append((
                'Rappel de rendez-vous',
                f'Bonjour {rdv.patient}, vous avez un rendez-vous prévu le {rdv.date}.',
                'from@example.com',
                [rdv.patient.email],
            ))

    if messages:
        for rdv in upcoming_rdvs:
         rdv.notification_envoyee = True
         rdv.save()
        send_mass_mail(messages, fail_silently=False)
        return f'{len(messages)} emails envoyés'
    
    

    return "Aucun rendez-vous à notifier"