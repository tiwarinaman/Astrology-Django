from django.contrib import admin
from django.contrib.auth.models import Group

from .models import UserDetails

# Register your models here.

admin.site.site_header = "Astrology Admin Dashboard"
admin.site.unregister(Group)
admin.site.register(UserDetails)
