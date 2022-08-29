from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view
from .serializers import DoctorSerializer,ListDoctorSerializer
from .models import Doctor
import jwt, datetime
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

# class RegisterView(APIView):
class RegisterView(APIView):
    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        doctor=serializer.save()
        tokenr = TokenObtainPairSerializer().get_token(doctor)  
        tokena = AccessToken().for_user(doctor)
        tokena['email'] = doctor.email
        tokena['role'] = doctor.role
        response = Response()
        response.data = {
            'doctor':serializer.data,
            'accessToken':str(tokena),
            'refreshToken': str(tokenr)
        }
        return response




class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        doctor = Doctor.objects.filter(email=email).first()
        if doctor is None:
            raise AuthenticationFailed('doctor not found!')
        if not doctor.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        tokenr = TokenObtainPairSerializer().get_token(doctor)  
        tokena = AccessToken().for_user(doctor)
        tokena['email'] = doctor.email
        tokena['role'] = doctor.role
        response = Response()
        response.set_cookie(key='jwt', value=tokena, httponly=True)
        response.data = {
            'id':doctor.id,
            'email':doctor.email,
            'accessToken':str(tokena),
            'refreshToken': str(tokenr)
        }
        return response


class getDoctor(APIView):
    def get(self, request):
        doctor = Doctor.objects.select_related('doctordetail').all()
        print("this is the doctor detail",doctor.doctordetail)
        serializer = DoctorSerializer(doctor,many=True)
        return Response(serializer.data)

class getDoctorById(APIView):
    def get(self, request,id):
        doctor = Doctor.objects.select_related('doctordetail').get(id=id)
        print("this is the doctor detail",doctor.doctordetail.id)
        serializer=ListDoctorSerializer(doctor,many=False)
        return Response(serializer.data)

class updateDoctor(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request,id):
        doctor = Doctor.objects.get(id=id)
        serializer=DoctorSerializer(instance=doctor,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class deleteDoctor(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request,id):
        doctor = Doctor.objects.get(id=id)
        doctor.delete()
        return Response("Item Successfully Deleted")

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

class ValidateToken(APIView):
    def get(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
            data=jwt.decode(token, "secret", algorithms=["HS256"])
            return Response(data)
        except Exception as e:
            return Response(e)
        

