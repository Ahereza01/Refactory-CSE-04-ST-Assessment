# Generated by Django 5.0.6 on 2024-09-13 11:24

import booking.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), booking.models.validate_letters])),
                ('gender', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('nationality', models.CharField(default=False, max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('email_address', models.CharField(max_length=50)),
                ('P_O_box_number', models.CharField(max_length=50)),
                ('emergency_phone_number', models.CharField(max_length=225)),
                ('passport_number', models.CharField(default=False, max_length=30)),
                ('visa_document', models.FileField(upload_to='cvs/')),
                ('departure_city', models.CharField(default=False, max_length=50)),
                ('destination_city', models.CharField(max_length=50)),
            ],
        ),
    ]
