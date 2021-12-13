from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from todos.form import TodosForm
from .models import Todos
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def homePage(request):
    if request.user.is_authenticated:
        user = request.user
        todos = user.todos_set.all().filter(is_completed=False).order_by('-created')
        total_todos = user.todos_set.all().count()
        completed_todos = user.todos_set.all().filter(is_completed=True).order_by('-updated')
        completed_todos_count = user.todos_set.all().filter(is_completed=True).count()
        form = TodosForm()

        # creating todos
        if request.method == 'POST':
            form = TodosForm(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = user
                todo.save()
                return redirect('homepage')

        context = {
            'form':form,
            'todos': todos,
            'total_todos':total_todos,
            'completed_todos':completed_todos,
            'completed_todos_count':completed_todos_count,
        }
    else:
        return redirect('login')
    return render(request, 'todos.html', context)

# updating todos
def updateTodos(request, pk):
    page = 'update'
    todo = Todos.objects.get(id=pk)
    form = TodosForm(instance=todo)
    if request.method == 'POST':
        form = TodosForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('homepage')
            

    context = {
        'form':form,
        'page':page,
    }
    return render(request, 'todos.html', context)
def deleteTodo(request, pk):
    todo = Todos.objects.get(id=pk)
    
    todo.delete()
    return redirect('homepage')

def CompleteTodo(request, pk):
    todo = Todos.objects.get(id=pk)
    if todo.is_completed == False:
        todo.is_completed = True
        todo.save()
    return redirect('homepage')

def undoComplete(request, pk):
    todo = Todos.objects.get(id=pk)
    if todo.is_completed == True:
        todo.is_completed = False
        todo.save()
    return redirect('homepage')

# creating user 
def signUp(request):
    page = 'signup'
    userForm = UserCreationForm()
    if request.method == 'POST':
        userForm = UserCreationForm(request.POST)
        if userForm.is_valid():
            user = userForm.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('homepage')

    context = {
        'userForm':userForm,
        'page':page,
    }
    return render(request, 'user-form.html', context)



# login user 
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            print('user does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        
    context ={}
    return render(request, 'user-form.html', context)



# Logout the user 
def logoutUser(request):
    logout(request)
    return redirect('homepage')