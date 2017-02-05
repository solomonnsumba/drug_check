from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from pharmacy_manager.forms import DrugForm
from pharmacy_manager.models import Drug


class AddDrug(SuccessMessageMixin, CreateView):
    form_class = DrugForm
    model = Drug
    success_message = "Drug Added"
    success_url = reverse_lazy('show_drugs')
    template_name = "drug_templates/create_and_edit_drug.html"


class UpdateDrug(SuccessMessageMixin, UpdateView):
    form_class = DrugForm
    model = Drug
    success_message = "Drug Updated"
    success_url = reverse_lazy('show_drugs')
    template_name = "drug_templates/create_and_edit_drug.html"


class DeleteDrug(SuccessMessageMixin, DeleteView):
    model = Drug
    success_message = "Drug deleted"
    context_object_name = "drug"
    success_url = reverse_lazy('show_drugs')
    template_name = "drug_templates/delete_drug.html"


class ListDrugs(ListView):
    model = Drug
    paginate_by = 10
    context_object_name = "drugs"
    template_name = "drug_templates/list_drugs.html"
