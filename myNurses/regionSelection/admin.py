from django.contrib import admin
from .models import region, city, country

admin.site.register(country)
admin.site.register(city)
admin.site.register(region)

