from django.contrib import admin
from .models import Employee, DailyTimeLog,LeaveApplication, OffsetApplication

# Register your models here.
admin.site.register(Employee),
admin.site.register(DailyTimeLog),
admin.site.register(LeaveApplication),
admin.site.register(OffsetApplication),
