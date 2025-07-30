from django.shortcuts import render
from django.http import HttpResponse
from todoApp.models import Task
from django.shortcuts import redirect
from todoApp.forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages


# Create your views here.


def accueil(request):
    return render(request, 'todoApp/accueil.html',{'body_class': 'background-accueil'})

def about_us(request):
    return render(request, 'todoApp/about_us.html', {'body_class': 'background-about-us'})

def todo_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'todoApp/todo_list.html', {'tasks':tasks})

def task_details(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'todoApp/task_details.html', {'task':task})

@login_required(login_url='/login/')
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task = form.save()
            return redirect('task-details', task.id)
    else :
        form = TaskForm()

    return render(request, 'todoApp/task_create.html', {'form':form})

def task_update(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-details', task.id)

    else:
        form = TaskForm(instance=task)

    return render(request, 'todoApp/task_update.html', {'form':form})

def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        if 'confirm' in request.POST:
            task.delete()
        return redirect('todo-list')

    return render(request, 'todoApp/task_delete.html', {'task':task})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'todoApp/register.html', {'form': form, 'background_class': 'background-login'})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Bienvenue {user.username} !')
            return redirect('accueil')
        else:
            messages.error(request, 'Nom d’utilisateur ou mot de passe incorrect.')
    else:
        form = AuthenticationForm()
    return render(request, 'todoApp/login.html', {'form': form})
