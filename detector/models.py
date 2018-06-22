from __future__ import unicode_literals
from django.db import models
import uuid
from django.core.validators import RegexValidator

#Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=120)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    password = models.CharField(max_length=40, validators=[RegexValidator(regex='^.{5,}$',
                            message='Password should be atleast 6 character long.', code='min_length')])
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

#class Input(models.Model):
#    age = models.IntegerField()
#    chest_pain = models.CharField(max_length=120)
#    rest_bpress = models.IntegerField()
#    blood_sugar = models.CharField(max_length=120)
#    rest_electro = models.CharField(max_length=120)
#    max_heart_rate = models.IntegerField()
#    exercice_angina = models.CharField(max_length=120)

class Values(models.Model):
    age = models.IntegerField()
    sex = models.IntegerField()
    cp = models.IntegerField()
    trestbps = models.IntegerField()
    chol = models.IntegerField()
    fbs = models.IntegerField()
    restecg = models.IntegerField()
    thalach = models.IntegerField()
    exang = models.IntegerField()
    slope = models.IntegerField()
    ca = models.IntegerField()
    thal = models.IntegerField()
