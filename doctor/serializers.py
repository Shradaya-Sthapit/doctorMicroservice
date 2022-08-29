from rest_framework import serializers
from .models import Doctor
from doctorDetails.serializers import ListDoctorDetailSerializer


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class ListDoctorSerializer(serializers.ModelSerializer):
    doctordetail = ListDoctorDetailSerializer(read_only=True)
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'email', 'password','doctordetail']
        extra_kwargs = {
            'password': {'write_only': True}
        }



        
