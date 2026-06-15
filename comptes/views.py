from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patient.models import  Patient
from medecin.models import Medecin
from rendez_vous.models import RendezVous
from consultations.models import Consultation
from django.db.models import Count, Sum
from django.db.models.functions import ExtractMonth
from facturations.models import Facture, DetailFacture
from rendez_vous.models import RendezVous
from django.utils import timezone
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.http import HttpResponseForbidden

class PannelAdminView(LoginRequiredMixin, UserPassesTestMixin, View):
    """Admin dashboard view"""
    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return HttpResponseForbidden("Vous n'avez pas la permission d'accéder à cette page.")
        return super().handle_no_permission()
    def get(self, request):
        return render(request, 'admin_dashboard.html')

    def get(self, request):
        nb_medecin = Medecin.objects.count()
        nb_patient = Patient.objects.count()
        nb_rendez_vous = RendezVous.objects.count()
        nb_consultation = Consultation.objects.count()

        context = {
            'nb_medecin': nb_medecin,
            'nb_patient': nb_patient,
            'nb_rendez_vous': nb_rendez_vous,
            'nb_consultation': nb_consultation
        }
        return render(request, 'dashboard.html', context)


@login_required
def dashboard(request):

   nb_medecin = Medecin.objects.count()
   nb_patient = Patient.objects.count()
   nb_rendez_vous = RendezVous.objects.count()
   nb_consultation = Consultation.objects.count()


   return render(request, 'dashboard.html', {'nb_medecin':nb_medecin,
                                              'nb_patient':nb_patient,
                                              'nb_rendez_vous':nb_rendez_vous,
                                              'nb_consultation':nb_consultation})



from django.shortcuts import render
from django.http import HttpResponseForbidden, JsonResponse
from django.utils import timezone
from django.db.models import Count
from datetime import date

from consultations.models import Consultation
from rendez_vous.models import RendezVous


def dashboard_rapport(request):
    today = date.today()
    now = timezone.now()

    nb_r_par_ce_mois = RendezVous.objects.filter(
        date__month=now.month,
        date__year=now.year
    ).count()

    nb_c_par_ce_mois = Consultation.objects.filter(
        date__month=now.month,
        date__year=now.year
    ).count()

    nb_c_ce_jour = Consultation.objects.filter(date=today).count()
    nb_r_ce_jour = RendezVous.objects.filter(date__date=today).count()

    return render(request, "rapport.html", {
        'nb_r_par_ce_mois': nb_r_par_ce_mois,
        'nb_c_par_ce_mois': nb_c_par_ce_mois,
        'nb_c_ce_jour': nb_c_ce_jour,
        'nb_r_ce_jour': nb_r_ce_jour
    })


def dashboard_data(request):
    today = date.today()
    now = timezone.now()

    # 🔢 CARTES
    nb_r_mois = RendezVous.objects.filter(
        date__month=now.month,
        date__year=now.year
    ).count()

    nb_c_mois = Consultation.objects.filter(
        date__month=now.month,
        date__year=now.year
    ).count()

    nb_c_jour = Consultation.objects.filter(date=today).count()
    nb_r_jour = RendezVous.objects.filter(date__date=today).count()

    # 📈 CHART 1 (PAR MOIS)
    data_mois = Consultation.objects.filter(
        date__year=now.year
    ).values('date__month').annotate(total=Count('id')).order_by('date__month')

    mois_labels_all = [
        "Jan", "Fev", "Mar", "Avr", "Mai", "Juin",
        "Juil", "Aou", "Sep", "Oct", "Nov", "Dec"
    ]

    chart1_labels = []
    chart1_data = []

    for item in data_mois:
        chart1_labels.append(mois_labels_all[item['date__month'] - 1])
        chart1_data.append(item['total'])

    # 🍩 CHART 2 (PAR JOUR SEMAINE)
    data_week = Consultation.objects.values(
        'date__week_day'
    ).annotate(total=Count('id')).order_by('date__week_day')

    jours_map = {
        1: "Dim",
        2: "Lun",
        3: "Mar",
        4: "Mer",
        5: "Jeu",
        6: "Ven",
        7: "Sam"
    }

    chart2_labels = []
    chart2_data = []

    for item in data_week:
        chart2_labels.append(jours_map[item['date__week_day']])
        chart2_data.append(item['total'])

    return JsonResponse({
        'nb_r_mois': nb_r_mois,
        'nb_c_mois': nb_c_mois,
        'nb_c_jour': nb_c_jour,
        'nb_r_jour': nb_r_jour,

        'chart1_labels': chart1_labels,
        'chart1_data': chart1_data,

        'chart2_labels': chart2_labels,
        'chart2_data': chart2_data,
    })