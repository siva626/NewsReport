from django.db import models


class Userreg(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    EmailID = models.EmailField(max_length=60)
    MobileNo = models.CharField(max_length=10)
    Gender = models.CharField(max_length=10)
    MaritalStatus = models.CharField(max_length=10)
    DOB = models.CharField(max_length=10)
    class Meta:
        db_table = "UserList"
