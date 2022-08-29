from django.urls import path,include
from .views import createSpecialization,getSpecialization,getSpecializationById,deleteSpecialization,updateSpecialization


urlpatterns = [

    path('create',  createSpecialization.as_view()),
    path('get', getSpecialization.as_view()),
    path('get/<str:id>', getSpecializationById.as_view()),
    path('update/<str:id>', updateSpecialization.as_view()),
    path('delete/<str:id>', deleteSpecialization.as_view()),
]

