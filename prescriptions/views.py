from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PrescriptionFormset

from django.views.generic.base import TemplateResponseMixin, View
from django.urls import reverse_lazy
from .models import Prescription
from .forms import PrescriptionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden, HttpResponse
from weasyprint import HTML
from django.contrib.auth.decorators import login_required   

from .filters import PrescriptionFilter 
from django.template.loader import render_to_string
class DoctorLoginRequiredMixin(LoginRequiredMixin):
    
    """Mixin to ensure the user is logged in and is a doctor"""
    def dispatch(self, request, *args, **kwargs):
        
            
        if not hasattr(request.user, 'medecin'):
            return HttpResponseForbidden("Vous devez être un médecin pour accéder à cette page.")
        return super().dispatch(request, *args, **kwargs)
    
    
class BaseMixin:
    model = Prescription
    

    def get_queryset(self):
        qs= super().get_queryset()
        return qs.select_related("patient").prefetch_related("lignes").filter(medecin=self.request.user.medecin)
class PrescriptionListView(DoctorLoginRequiredMixin, BaseMixin, ListView):
    
    template_name = 'prescriptions/prescription_list.html'
    context_object_name = 'prescriptions'
    paginate_by = 6
    def get_queryset(self):
        qs= super().get_queryset()
        self.filterset = PrescriptionFilter(self.request.GET,  qs)
        return self.filterset.qs
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['filterset']= self.filterset
        query_params = self.request.GET.copy()
        if 'page'in query_params:
            query_params.pop('page', None)
        context['query_params'] = query_params.urlencode   
        return context

class PrescriptionDetailView(DoctorLoginRequiredMixin,BaseMixin, DetailView):
    template_name = 'prescriptions/prescription_form_detail.html'
    context_object_name = 'prescription' 
    
class EditPrescriptionView:
    
    def form_valid(self, form):

        print("FORMULAIRE VALIDE")
        print(form.cleaned_data)
        form.instance.medecin=self.request.user.medecin
        return super().form_valid(form)
    def form_invalid(self, form):
        print("FORMULAIRE INVALIDE")
        print(form.errors)

        return super().form_invalid(form)    
class CreatePrescriptionView(DoctorLoginRequiredMixin, EditPrescriptionView, BaseMixin, CreateView):
    form_class = PrescriptionForm
    template_name = 'prescriptions/prescription_form.html'
    
    success_url = reverse_lazy('prescriptions:list_prescriptions')  
class DeletePrescriptionView(DoctorLoginRequiredMixin,BaseMixin, DeleteView):
    template_name = 'prescriptions/prescription_confirm_delete.html'
    success_url = reverse_lazy('prescriptions:list_prescriptions')
class UpdatePrescriptionView(DoctorLoginRequiredMixin, EditPrescriptionView,BaseMixin, UpdateView):
    form_class = PrescriptionForm  
    template_name = 'prescriptions/prescription_form.html'
    
    success_url = reverse_lazy('prescriptions:list_prescriptions')   

class CreateDetailPrescriptionView(DoctorLoginRequiredMixin,TemplateResponseMixin, View):

    template_name = 'prescriptions/prescription_form_detail.html'
    
    
   

    def dispatch(self, request, *args, **kwargs):
        self.prescription = get_object_or_404(Prescription, pk=kwargs['pk'], medecin=request.user.medecin)
        return super().dispatch(request, *args, **kwargs)   
    def get_formset(self, data=None):
        return PrescriptionFormset(data, instance=self.prescription)  
    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'formset': formset, 'prescription': self.prescription}) 
    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('prescriptions:list_prescriptions')
        return self.render_to_response({'formset': formset, 'prescription': self.prescription})

@login_required
def prescription_pdf(request, pk):
    prescription = Prescription.objects.get(pk=pk)
    lignes = prescription.lignes.all()

   

    html_string = render_to_string("prescriptions/prescription_pdf.html", {
        "prescription": prescription,
        "lignes": lignes
    })

    html = HTML(string=html_string)
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type="application/pdf")
    response['Content-Disposition'] = f'filename="prescription_{prescription.id}.pdf"'

    return response

# Create your views here.


                  

# Create your views here.
