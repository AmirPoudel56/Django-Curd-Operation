from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Registration(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=255)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='profile_picture/')

    def __str__(self) -> str:
        return self.first_name
