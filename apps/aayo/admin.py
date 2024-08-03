from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Cafe)
admin.site.register(MenuItem)
admin.site.register(Room)
admin.site.register(RoomAccount)
admin.site.register(Order)