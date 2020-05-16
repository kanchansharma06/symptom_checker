
from django.db import models


'''
class Profilee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    '''
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import auth,User


class log(models.Model):
    log_email=models.CharField(max_length=225)
    log_password=models.CharField(max_length=225)
class registeration(models.Model):
    reg_first=models.CharField(max_length=225)
    reg_last=models.CharField(max_length=225)
    reg_username=models.CharField(max_length=225)
    reg_email=models.CharField(max_length=225)
    reg_password=models.CharField(max_length=225)
    reg_confirm_password=models.CharField(max_length=225)
class contact(models.Model):
    contact_first=models.CharField(max_length=225)
    contact_last=models.CharField(max_length=225)
    contact_email=models.CharField(max_length=225)
    contact_subject=models.CharField(max_length=225)
    contact_feedback=models.CharField(max_length=225)
class diagnose1(models.Model):
    diagnose_age=models.IntegerField()
    role=(
        ('male',"Male"),
        ('female',"Female")
    )
    diagnose_gender=models.CharField(max_length=10,choices=role,default='male')
    diagnose_symptom=models.CharField(max_length=225)
class meddata(models.Model):
    med_age=models.IntegerField()

    med_gender=models.CharField(max_length=10)
class body_loc1(models.Model):

    med_bodyloc=models.CharField(max_length=100)
    med_bodylocno=models.IntegerField()
class sub_body1(models.Model):
    med_subbody=models.CharField(max_length=100)
    med_subbodyno=models.IntegerField()
class body_data1(models.Model):
    med_bodydata=models.CharField(max_length=100)
    med_bodydatano=models.IntegerField()



# Create your models here.
