from django.shortcuts import render,redirect
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Consultation

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy

from .forms import ConsultationForm

from.filters import ConsultationFilter

class MedecinRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, 'medecin'):
            raise PermissionDenied("acces reserve aux medecins")
        return super().dispatch(request, *args, **kwargs)


class BaseConsultationView(LoginRequiredMixin, MedecinRequiredMixin):
    model = Consultation
    def get_queryset(self):
        qs= super().get_queryset()
        return qs.filter(medecin__user=self.request.user)


class EditConsultation :
    template_name = 'consultation/consultation_form.html'
    success_url = reverse_lazy('consultations:list')
    form_class = ConsultationForm
    def form_valid(self, form):
        form.instance.medecin = self.request.user.medecin
        
        return  super().form_valid(form)    
            



class ConsultationListView(BaseConsultationView, ListView): 
    
    template_name = 'consultation/consultation_list.html'
    context_object_name = 'consultations'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset().select_related(
            'patient', 'medecin'
        ).order_by('-date')

        self.filterset = ConsultationFilter(
            self.request.GET,
            queryset=queryset
        )

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset

        # conserver les filtres dans pagination
        query_params = self.request.GET.copy()
        if 'page' in query_params:
            query_params.pop('page')

        context['query_params'] = query_params

        return context
    
class ConsultationDetailView(BaseConsultationView, DetailView ):
    template_name = 'consultation/consultation_detail.html'
    context_object_name = 'consultation'

    
    
class ConsultationActualiserView(BaseConsultationView, EditConsultation, UpdateView):
    
        pass

class ConsultationSupprimerView(BaseConsultationView, DeleteView):
    model = Consultation
    template_name = 'consultation/consultation_confirm_delete.html'
    success_url = reverse_lazy('consultations:list')
    
    



    


class ConsultationCreateView(BaseConsultationView,EditConsultation, CreateView):
    

    pass

   

    # def get_patient(self):
    #     return Patient.objects.get(
    #         id=self.kwargs['patient_id']
    #     )
   



# class ConsultationSupprimerView(LoginRequiredMixin, MedecinRequiredMixin, DeleteView):





         

# Create your views here.
