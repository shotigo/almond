from django.db import models
from django.utils import timezone

class Employee(models.Model):
    employee = models.ForeignKey('auth.User')
    job_description = models.CharField(max_length=300)
    shift_hours = models.IntegerField(default=8)
    date_of_hire = models.DateTimeField(
            blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.employee.username

class DailyTimeLog(models.Model):
    employee = models.ForeignKey('almondapp.Employee', related_name='EmployeeLog')
    check_in_date_time = models.DateTimeField(default=timezone.now)
    check_out_date_time = models.DateTimeField(blank=True, null=True)
    caption = models.TextField();
    created_date = models.DateTimeField(default=timezone.now)

class LeaveApplication(models.Model):
    employee = models.ForeignKey('almondapp.Employee', related_name='EmployeeApplyingForLeave')
    leaves = (('SL','Sick Leave'),('VL','Vacation Leave'),('EL','Emergency Leave'))
    leave_type = models.CharField(max_length=2,choices=leaves)
    reason = models.TextField()
    date_of_leave = models.DateTimeField(
        blank=True, null=True)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

class OffsetApplication(models.Model):
    employee = models.ForeignKey('almondapp.Employee', related_name='EmployeeApplyingForOffset')
    date_of_offset = models.DateTimeField(
        blank=True, null=True)
    date_time_requested = models.DateTimeField(default=timezone.now)
    hours_requested_for_offset = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
