from django.shortcuts import get_object_or_404, redirect, render

from .models import Todo


def todo_list(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if title:
            Todo.objects.create(title=title)
        return redirect("todo_list")

    todos = Todo.objects.order_by("-created_at")
    return render(request, "todos/list.html", {"todos": todos})


def todo_toggle(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return redirect("todo_list")


def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect("todo_list")
