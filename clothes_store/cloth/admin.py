from django.contrib import admin
from .models import cloth
from .models import Client

# Register your models here.
admin.site.register(cloth)
admin.site.register(Client)