# Generated by Django 4.1 on 2022-08-26 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('specializations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('contact', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('additionalInfo', models.CharField(max_length=255)),
                ('inTime', models.TimeField()),
                ('outTime', models.TimeField()),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('specialization', models.ManyToManyField(to='specializations.specialization')),
            ],
        ),
    ]