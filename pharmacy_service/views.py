# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from pharmacy_manager.models import Drug
from pharmacy_service.serializer import DrugSerializer


class GetDrugs(APIView):
    serializer_class = DrugSerializer

    def get(self, request, format=None):
        drugs = Drug.objects.all()
        serializer = self.serializer_class(drugs, many=True, read_only=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


