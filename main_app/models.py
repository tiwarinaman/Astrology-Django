from django.db import models


# Create your models here.

class UserDetails(models.Model):
    full_name = models.CharField(max_length=150, null=True)
    email = models.EmailField(null=True)
    mobile = models.BigIntegerField(null=True)
    alternate_number = models.BigIntegerField(null=True, blank=True)
    dob = models.DateField(null=True)
    time_of_birth = models.TimeField(null=True)
    user_info = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.full_name
