from django.shortcuts import render, get_object_or_404, redirect
from ToDo_App.form import todo_form

from .models import Todo

# Create your views here.
def view_main_todo(request, *args, **kwargs):
    form = todo_form()
    if request.method == 'POST':
        print(request.POST)
        form = todo_form(request.POST)
        if form.is_valid():
            Todo.objects.create(**form.cleaned_data)
            form = todo_form()
    
    context = {
        "form": form,
        "items": Todo.objects.all().order_by("-date"),
    }
    return render(request,"index.html", context)


def view_delete_item(request, id):
    obj = get_object_or_404(Todo, id=id)

    if request.method == 'POST':
        obj.delete()
        return redirect('../../')

    return render(request,"index.html",{})


def view_update_item(request, id):
    item = Todo.objects.get(id=id)

    context = {
        "item": item,
    }

    return render(request, "edit.html", context)