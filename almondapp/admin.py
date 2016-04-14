from django.contrib import admin
from .models import Employees, TimeStamp, Leaves, LeaveApplication, OffsetApplication

# Register your models here.
admin.site.register(Employees),
admin.site.register(TimeStamp),
admin.site.register(Leaves),
admin.site.register(LeaveApplication),
admin.site.register(OffsetApplication),
