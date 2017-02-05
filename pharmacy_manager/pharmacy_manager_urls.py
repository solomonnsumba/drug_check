from django.views.generic import TemplateView
from pharmacy_manager.views import AddDrug, UpdateDrug, DeleteDrug, ListDrugs

from django.conf.urls import url

urlpatterns = [
    url(r'^add_drug/$', AddDrug.as_view(), name='add_drug'),
    url(r'^update_drug(?P<pk>\d+)/$', UpdateDrug.as_view(), name='update_drug'),
    url(r'^remove_drug(?P<pk>\d+)/$', DeleteDrug.as_view(), name='remove_drug'),
    url(r'^show_drugs/$', ListDrugs.as_view(), name='show_drugs'),
    url(r'^', TemplateView.as_view(template_name='drug_templates/home.html'), name='home'),

]