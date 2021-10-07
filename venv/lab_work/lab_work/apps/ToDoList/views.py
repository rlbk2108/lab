from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Task

def index(request):
    exercises_list = Task.objects.order_by('-date_added')
    return render(request, 'to_do_list/list.html', {'exercises_list' : exercises_list})

def TaskDetail(request, exercise_id):
	try:
		a = Task.objects.get( id = exercise_id )
	except:
		raise Http404('Задача не найдена')

	return render(request, 'to_do_list/taskdetail.html')
