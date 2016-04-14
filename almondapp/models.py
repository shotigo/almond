from django.db import models
from django.utils import timezone

class Employees(models.Model):
    FullName = models.CharField(max_length=50)
    JobDescription = models.CharField(max_length=300)
    DateOfHire = models.DateTimeField(
            blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

class TimeStamp(models.Model):
    Employee = models.ForeignKey('almondapp.Employees', related_name='EmployeeLog')
    CheckInDateTime = models.DateTimeField(default=timezone.now)
    CheckOutDateTime = models.DateTimeField(default=timezone.now)

class Leaves(models.Model):
    LeaveDescription = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)

class LeaveApplication(models.Model):
    Employee = models.ForeignKey('almondapp.Employees', related_name='EmployeeApplyingForLeave')
    DateOfLeave = models.DateTimeField(
        blank=True, null=True)
    Status = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

class OffsetApplication(models.Model):
    Employee = models.ForeignKey('almondapp.Employees', related_name='EmployeeApplyingForOffset')
    DateOfOffset = models.DateTimeField(
        blank=True, null=True)
    DateTimeApplied = models.DateTimeField(default=timezone.now)
    HoursOffsetted = models.TimeField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title