from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SpecializationSerializer
from .models import Specialization
import jwt, datetime
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated,AllowAny


class createSpecialization(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SpecializationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class getSpecialization(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        specialization = Specialization.objects.all()
        serializer=SpecializationSerializer(specialization,many=True)
        return Response(serializer.data)

class getSpecializationById(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,id):
        specialization = Specialization.objects.get(id=id)
        serializer=SpecializationSerializer(specialization,many=False)
        return Response(serializer.data)

class updateSpecialization(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request,id):
        specialization = Specialization.objects.get(id=id)
        serializer=SpecializationSerializer(instance=specialization,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class deleteSpecialization(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request,id):
        specialization = Specialization.objects.get(id=id)
        specialization.delete()
        return Response("Item Successfully Deleted")



    