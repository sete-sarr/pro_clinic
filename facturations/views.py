from django.shortcuts import render, get_object_or_404, redirect
from .forms import ModelFormset
from .models import Facture
from django.urls import reverse_lazy

from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .filters import FactureFilter

from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Facture, DetailFacture

class DocteurLoginRequiredMixin(LoginRequiredMixin):
    """Mixin to ensure the user is logged in and is a doctor"""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not hasattr(request.user, 'medecin'):
            return HttpResponseForbidden("Vous devez être un médecin pour accéder à cette page.")
        return super().dispatch(request, *args, **kwargs)

class DocteurMixin:
    def get_queryset(self):
        qs= super().get_queryset()
        return qs.prefetch_related("patient__factures").filter(medecin=self.request.user.medecin)
class DocteurEditMixin:

    def form_valid(self, form):
        form.instance.medecin=self.request.user.medecin
        return super().form_valid(form)
class DocteurFactureMixin(DocteurLoginRequiredMixin,DocteurMixin, ):
    
    model = Facture
    fields=[ "patient"]
    success_url =   reverse_lazy("facturations:list_factures")
class DocteurEditFactureMixin( DocteurFactureMixin): 
    template_name = "factures/factures_form.html"

class ListFactureView(DocteurFactureMixin, ListView):
    


    context_object_name='factures'
    template_name="factures/factures_list.html" 
    paginate_by =6
    def get_queryset(self):
        qs= super().get_queryset()
        
        self.filterset = FactureFilter(self.request.GET,  qs)
        return self.filterset.qs
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['filterset']= self.filterset
        query_params = self.request.GET.copy()
        if 'page'in query_params:
            query_params.pop('page', None)
        context['query_params'] = query_params.urlencode   
        return context

class CreerFactureView(DocteurEditFactureMixin,DocteurEditMixin ,CreateView)  :
    pass 

class ActualiserFactureView(DocteurEditFactureMixin, DocteurEditMixin, UpdateView ):

    pass

class SupprimerFactureView(DocteurFactureMixin, DeleteView):
    template_name="factures/factures_confirm_delete.html"

       
    

class CreerDetailFactureCustomView(TemplateResponseMixin, View):

    template_name = "factures/factures_detail_form.html"
    

    def dispatch(self, request, *args, **kwargs):
        self.facture = get_object_or_404(Facture, id=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def get_formset(self, data=None):
        return ModelFormset(instance=self.facture, data=data)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({
            'facture': self.facture,
            'formset': formset
        })

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            
            return redirect('facturations:list_factures')

        return self.render_to_response({
            'facture': self.facture,
            'formset': formset
        })



def facture_pdf(request, pk):
    facture = Facture.objects.get(pk=pk)
    details = DetailFacture.objects.filter(facture=facture)

    total = sum([ d.quantite * d.prix for d in details])

    from decimal import Decimal

    details = facture.details_facture.all()

    for d in details:
        d.total = d.quantite * d.prix

    total = sum(d.total for d in details)

    tva = total * Decimal('0.18')
    total_ttc = total + tva

    html_string = render_to_string("factures/facture_pdf.html", {
        "facture": facture,
        "details": details,
        "total": total,
        "tva": tva,
        "total_ttc": total_ttc
    })

    html = HTML(string=html_string)
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type="application/pdf")
    response['Content-Disposition'] = f'filename="facture_{facture.id}.pdf"'

    return response

# Create your views here.
