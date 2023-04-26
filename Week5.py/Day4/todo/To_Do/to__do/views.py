from django.shortcuts import render
from .models import Category, Todo_model
from .forms import ToDoForm

def display_todos(request):
    todos = Todo_model.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos.html', context)

def add_todo(request):
    if request.method =='POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            todo_new = Todo_model(
                title = data['title'],
                details = data['details'],
                has_been_done = data['has_been_done'],
                # date_completion = data['date_completion'],
                deadline_date = data['deadline_date'],
                category = data['category']
            )
            todo_new.save()
            msg = 'Todo was uploaded'
        else:
            msg = 'Somehing went wrong'
    else:
        form = ToDoForm()
        msg = ''
    context = {
        'form': form,
        'msg': msg
    }
    return render(request,'addtodo.html',context)


# Create your views here.
