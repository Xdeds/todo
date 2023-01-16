from django.http import HttpResponseRedirect
from django.shortcuts import render
from main.models import Message, Todo
def main(request):
    todo = Todo.objects.all()
    return render(request, 'index.html', {'todo':todo})
def message(request):
    todo = Todo()
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
    return HttpResponseRedirect('/')
def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect('/')
def edit(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return HttpResponseRedirect('/')
    return render(request, 'edit.html')
def complete(request, id):
    todo = Todo.objects.get(id=id)
    if todo.is_complete:
        todo.is_complete = False
        todo.save()
    else:
        todo.is_complete = True
        todo.save()
    return HttpResponseRedirect('/')