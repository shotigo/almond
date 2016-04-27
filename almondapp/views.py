from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import date
from django.shortcuts import redirect
from .models import Employee, DailyTimeLog
from django.contrib.auth.decorators import login_required

# Create your views here.
def time_logs(request):
	logs = DailyTimeLog.objects.filter(created_date__gte=date.today()).order_by('created_date').filter(check_out_date_time=None)
	if request.method == "POST":
		caption = request.POST.get('caption')
		check = request.POST.get('check')
		user = request.user
		employee_logged_in = get_object_or_404(Employee, employee=user)
		if check == "checkin":
			DailyTimeLog.objects.create(employee=employee_logged_in, check_in_date_time=timezone.now(), caption=caption, created_date=timezone.now())
			return redirect('almond:time_logs')	
		elif check == "checkout":
			dailylog = DailyTimeLog.objects.get(employee=employee_logged_in, check_out_date_time =None)
			dailylog.check_out_date_time = timezone.now()
			dailylog.save()
			return redirect('almond:time_logs')
	else:
		return render(request, 'almondapp/time_logs.html', {'logs': logs})