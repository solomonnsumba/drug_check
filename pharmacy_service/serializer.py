from rest_framework.serializers import ModelSerializer
from pharmacy_manager.models import Drug


class DrugSerializer(ModelSerializer):
    class Meta:
        model = Drug
        fields = ['id', 'drug_name', 'description', 'manufacturer', 'code', 'thumb_nail','exp_date']