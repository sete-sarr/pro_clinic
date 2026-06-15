from django.shortcuts import render


from django.views.generic import (
    ListView, CreateView,
    DetailView, DeleteView,
    UpdateView
)
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Patient
from .filters import PatientFilterset
from .forms import PatientForm


# # ----------- MIXINS -----------

# class MedecinQuerysetMixin:
#     def get_queryset(self):
#         return Patient.objects.filter(
#             consultations__medecin__user=self.request.user
#         )


class LoginMedecinMixin:
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, 'medecin'):
            raise PermissionDenied("Accès réservé aux médecins")
        return super().dispatch(request, *args, **kwargs)


# ----------- BASE VIEW -----------

class PatientBaseView(LoginRequiredMixin, LoginMedecinMixin):
    model = Patient
    context_object_name = "patient"


class EditPatient:
    success_url = reverse_lazy('patient:list_patient')
    template_name = "patients/patient/patient_form.html"
    form_class= PatientForm
class PatientListView(PatientBaseView, ListView):
    template_name = "patients/patient/patient_list.html"
    context_object_name = "patients"
    paginate_by=6
    def get_queryset(self):
        qs= super().get_queryset()
        self.filterset = PatientFilterset(self.request.GET, qs)
        return self.filterset.qs
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['filterset']=self.filterset
        params_query = self.request.GET.copy()
        if 'page' in params_query:
            params_query.pop('page')
        context['params_query'] =params_query.urlencode 
        return context

class PatientDetailView(PatientBaseView, DetailView):
    
    template_name = "patients/patient/patient_detail.html"


class PatientActualiserView(PatientBaseView,EditPatient, UpdateView):
    pass


class PatientCreerView(PatientBaseView, EditPatient, CreateView):


    pass
class PatientSupprimerView(PatientBaseView,  DeleteView):
    template_name = "patients/patient/patient_confirm_delete.html"
    success_url = reverse_lazy('patient:list_patient')
            

# Create your views here.
