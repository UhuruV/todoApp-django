from django.shortcuts import render,redirect
from .models import TodoList,Category

# Create your views here.
def index(request):
    todos = TodoList.object.all()
    categories = Category.object.all()
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            date = str(request.POST["date"])
            category = request.POST["category_select"]
            content = title + --+date + " " + category
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            return redirect("/")
            
        if "taskDelete" in request.POST:
            checkedList = request.POST["checkedbox"]
            
            for todo_id in checkedList:
                todo = TodoList.object.get(id=int(todo_id))
                
                todo.delete()

    return render(request, "index.html", {"todos": todos, "categories": categories})
    
            
            