# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-13 12:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=50)),
                ('JobDescription', models.CharField(max_length=300)),
                ('DateOfHire', models.DateTimeField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateOfLeave', models.DateTimeField(blank=True, null=True)),
                ('Status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EmployeeApplyingForLeave', to='almondapp.Employees')),
            ],
        ),
        migrations.CreateModel(
            name='Leaves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LeaveDescription', models.CharField(max_length=300)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='OffsetApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateOfOffset', models.DateTimeField(blank=True, null=True)),
                ('DateTimeOffsetted', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EmployeeApplyingForOffset', to='almondapp.Employees')),
            ],
        ),
        migrations.CreateModel(
            name='TimeStamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CheckInDateTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('CheckOutDateTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EmployeeLog', to='almondapp.Employees')),
            ],
        ),
    ]