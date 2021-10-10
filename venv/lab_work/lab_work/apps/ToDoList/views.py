from django.http import Http404, HttpResponseRedirect
from .models import Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy


def index(request):
    exercises_list = Task.objects.order_by('-date_added')
    return render(request, 'to_do_list/list.html', {'exercises_list' : exercises_list})

    


def detail(request, exercise_id):
	try:
		a = Task.objects.get( id = exercise_id )
	except:
		raise Http404('Задача не найдена')

	return render(request, 'to_do_list/task_detail.html', {'exercise' : a})

# class IndexView(ListView):
#     template_name = 'to_do_list/index.html'
#     context_object_name = 'contact_list'

#     def get_queryset(self):
#         return Task.objects.all()

# class DetailView(DetailView):
#     model = Task
#     template_name = 'to_do_list/task_detail.html'



def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todolist/')
    form = ContactForm()

    return render(request,'to_do_list/task_create.html', {'form' : form })


def delete(request, pk, template_name='to_do_list/task_delete.html'):
    contact = get_object_or_404(Task, pk=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('todolist/')
    return render(request, template_name, {'object' : contact})


def edit(request, pk, template_name = 'to_do_list/task_edit.html'):
    contact = get_object_or_404(Task, pk=pk)
    if request.method=='POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact.save()
            return redirect('todolist/')
    else:
        form = ContactForm(instance=contact)
    return render(request, template_name, {'form' : form})
