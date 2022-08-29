from rest_framework import serializers
from .models import DoctorDetail
# from doctor.serializers import DoctorSerializer
from specializations.serializers import SpecializationSerializer


class CreateDoctorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorDetail
        fields = '__all__'

class ListDoctorDetailSerializer(serializers.ModelSerializer):
    # doctor = DoctorSerializer(read_only=True)
    specialization= SpecializationSerializer(read_only=True,many=True)
    class Meta:
        model = DoctorDetail
        fields = '__all__'


