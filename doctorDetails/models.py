from django.db import models
from doctor.models import Doctor
from specializations.models import Specialization

class DoctorDetail(models.Model):
    id=models.AutoField(primary_key=True)
    contact= models.CharField(max_length=255)
    address= models.CharField(max_length=255)
    additionalInfo= models.CharField(max_length=255)
    specialization=models.ManyToManyField(Specialization)
    inTime=models.TimeField()
    outTime=models.TimeField()
    doctor = models.OneToOneField(
        Doctor,
        on_delete=models.CASCADE,
    )