from django.contrib import admin

from .models import CustomUser, Provider, Polygon


admin.site.register(CustomUser)
admin.site.register(Provider)
admin.site.register(Polygon)
