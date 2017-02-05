from django.forms import ModelForm
from pharmacy_manager.models import Drug


class DrugForm(ModelForm):
    class Meta:
        model = Drug
        fields = ['drug_name', 'manufacturer', 'description', 'thumb_nail', 'code','exp_date']
