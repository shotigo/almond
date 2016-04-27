from django import forms
from .models import Employee, DailyTimeLog,LeaveApplication, OffsetApplication

class CheckInForm(forms.ModelForm):

	class Meta:
		model = DailyTimeLog
		fields = '__all__'

class CheckOutForm(forms.ModelForm):

	class Meta:
		model = DailyTimeLog
		fields = {'caption',}