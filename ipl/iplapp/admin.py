from django.contrib import admin

# Register your models here.
from .models import matches, deliveries

admin.site.register(matches)
admin.site.register(deliveries)
