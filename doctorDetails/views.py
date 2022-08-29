from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateDoctorDetailSerializer,ListDoctorDetailSerializer
from specializations.models import Specialization
from .models import DoctorDetail
import jwt, datetime
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated,AllowAny


class createDoctorDetail(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        doctor= request.user
        request.data['doctor']=doctor
        data=request.data
        newDoctorDetail= DoctorDetail.objects.create(contact=data['contact'],address=data['address'],additionalInfo=data['additionalInfo'],inTime=data['inTime'],outTime=data['outTime'],doctor=data['doctor'])
        for specializationId in data['specialization']:
            specialization=Specialization.objects.get(id=specializationId)
            newDoctorDetail.specialization.add(specialization)
        serializer = CreateDoctorDetailSerializer(newDoctorDetail) 
        return Response(serializer.data)

class getDoctorDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data=request.data
        doctorDetail = DoctorDetail.objects.all()
        serializer=ListDoctorDetailSerializer(doctorDetail,many=True)
        return Response(serializer.data)

class getDoctorDetailById(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,id):
        doctorDetail = DoctorDetail.objects.get(id=id)
        serializer=ListDoctorDetailSerializer(doctorDetail,many=False)
        return Response(serializer.data)

class updateDoctorDetail(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request,id):
        data=request.data
        doctorDetail = DoctorDetail.objects.get(id=id)
        doctorDetail.specialization.clear() 
        for specializationId in data['specialization']:
            specialization=Specialization.objects.get(id=specializationId)
            doctorDetail.specialization.add(specialization)
        serializer=CreateDoctorDetailSerializer(instance=doctorDetail,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class deleteDoctorDetail(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request,id):
        doctorDetail = DoctorDetail.objects.get(id=id)
        print("this is the DoctorDetail",doctorDetail)
        doctorDetail.delete()
        return Response("Item Successfully Deleted")



    