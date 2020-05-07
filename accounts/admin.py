from django.contrib import admin
from .models import roomservice,cabservice,complaintservice

# Register your models here.
admin.site.register(roomservice)
admin.site.register(cabservice)
admin.site.register(complaintservice)

