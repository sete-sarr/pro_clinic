from django.shortcuts import render
from django.views.generic import (
                                   ListView,
                                   CreateView,
                                     UpdateView,
                                     DeleteView,
                                     DetailView
                                     )
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from patient.models import Patient
from .models import RendezVous
from .forms import RendezVousForm
from .filters import RendezVousFilter

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import json

class BaseMixin:
    def get_queryset(self):
        return RendezVous.objects.select_related('patient', 'medecin').filter(medecin__user=self.request.user)


class MedecinRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
     if not hasattr(request.user, 'medecin'):
        raise PermissionDenied("acces reserve aux medecins")
     return super().dispatch(request, *args, **kwargs)
    
class RendezVousMixin(LoginRequiredMixin, MedecinRequiredMixin):
        pass
class EditRendezVous:

    def form_valid(self, form):
        rendez_vous = form.save(commit=False)

        # ✅ Assigner le médecin correctement
        rendez_vous.medecin = self.request.user.medecin
        

        rendez_vous.save()

        
        from .tasks import notify_upcoming_appointments
        notify_upcoming_appointments.delay(rendez_vous.id)

        return super().form_valid(form)

class RendezVousListView(RendezVousMixin,  ListView):
    model = RendezVous
    template_name = 'rendez_vous/rendez_vous_list.html'
    context_object_name = 'rendez_vous'
    paginate_by=6
    
    def get_queryset(self):
        self.queryset= RendezVous.objects.select_related(
            'patient', 'medecin'
        ).filter(
            medecin__departement=self.request.user.medecin.departement
        )
        self.filterSet = RendezVousFilter(self.request.GET, queryset=self.queryset)
        return self.filterSet.qs
    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['filter']=self.filterSet
        query_params = self.request.GET.copy()
        if 'page'in query_params:
            query_params.pop('page')
        context['query_params'] = query_params    
        return context
    
    
class RendezVousDetailView(RendezVousMixin, BaseMixin, DetailView):
    
    template_name = 'rendez_vous/rendez_vous_detail.html'
    context_object_name = 'rendez_vous'

    def get_queryset(self):
        qs= super().get_queryset()
        return qs.filter(medecin__departement=self.request.user.medecin.departement)
class RendezVousActualiserView(RendezVousMixin, EditRendezVous,
                                  UpdateView):
    model = RendezVous
    template_name = 'rendez_vous/rendez_vous_form.html'
    form_class = RendezVousForm
    
    success_url = reverse_lazy('rendez_vous:list')
    



    def get_queryset(self):
        qs= super().get_queryset()
        return qs.filter(medecin__user=self.request.user) 

class RendezVousCreateView(RendezVousMixin, EditRendezVous, CreateView):
    model = RendezVous
    form_class = RendezVousForm
    template_name = 'rendez_vous/rendez_vous_form.html'
    success_url = reverse_lazy('rendez_vous:list')

class RendezVousDeleteView(RendezVousMixin,BaseMixin, DeleteView):
    
    template_name = 'rendez_vous/rendez_vous_delete.html'
    success_url = reverse_lazy('rendez_vous:list')

    def get_queryset(self):
        qs= super().get_queryset()
        return qs.filter(medecin__user=self.request.user)

   

    
        
# views.py


def search_patient(request):
    q = request.GET.get('q', '')

    patients = Patient.objects.filter(nom__icontains=q)[:10]

    data = [
        {
            'id': p.id,
            'text': f"{p.nom} {p.prenom}-{p.telephone}"
        }
        for p in patients
    ]

    return JsonResponse({'results': data}) 

# views.py

@csrf_exempt
def create_patient_ajax(request):
    if request.method == "POST":
        data = json.loads(request.body)

        patient = Patient.objects.create(
            nom=data.get('nom'),
            prenom=data.get('prenom'),
            telephone=data.get('telephone'),
            email=data.get('email'),
            adresse=data.get('adresse')
        )

        return JsonResponse({
            'id': patient.id,
            'text': f"{patient.nom} {patient.prenom}"
        })       
             


# Create your views here.
