from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Jobpost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    designation = models.CharField(max_length=30)
    yrs_of_exp = models.IntegerField()
    place = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100,blank=True,null=True)
    referal_code = models.CharField(max_length=8,unique=True,blank=True,null=True)
    resume = models.FileField(upload_to='resume/')
    


    def __str__(self):
        return self.user.first_name+" "+self.user.last_name+" "+" "+self.designation