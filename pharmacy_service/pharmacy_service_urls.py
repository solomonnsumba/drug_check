from pharmacy_service.views import GetDrugs

from django.conf.urls import url

urlpatterns = [
    url(r'^get_drugs/$', GetDrugs.as_view(), name='get_drugs'),
]