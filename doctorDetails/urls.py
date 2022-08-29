from django.urls import path,include
from .views import createDoctorDetail,getDoctorDetail,getDoctorDetailById,deleteDoctorDetail,updateDoctorDetail


urlpatterns = [

    path('create',  createDoctorDetail.as_view()),
    path('get', getDoctorDetail.as_view()),
    path('get/<str:id>', getDoctorDetailById.as_view()),
    path('update/<str:id>', updateDoctorDetail.as_view()),
    path('delete/<str:id>', deleteDoctorDetail.as_view()),
]

