from django.shortcuts import redirect, render
from .forms import TodoForm
from .models import Todo

# Create your views here.

def index(request):
    tasks = Todo.objects.all()
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {
        "tasks": tasks, 
        "form": form
    }
    return render(request, "todo/index.html", context)


def update(request, id):
    task = Todo.objects.get(id = id)
    form = TodoForm(instance=task)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {
        "form": form,
        "task":  task
    }
    return render(request,"todo/update.html", context)



def delete(request, id):
    task = Todo.objects.get(id = id)
    if request.method == "POST":
        task.delete()
        return redirect("/")
    context = {
        "task":  task
    }
    return render(request,"todo/delete.html", context)


