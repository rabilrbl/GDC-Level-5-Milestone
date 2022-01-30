from django.shortcuts import render, redirect

# Add your Views Here
from tasks.models import Task


# Create your views here.
def index(request):
    return redirect('tasks')
# Add a new task
def add_task(request):
    # get the task as parameter
    task = request.GET.get('task')
    # create a new task
    new_task = Task(title=task, completed=False)
    # save the task
    new_task.save()
    # redirect to the tasks view
    return redirect('tasks')

# Delete a task
def delete_task(request, task_id):
    # get the task as parameter
    task = Task.objects.get(id=task_id)
    # delete the task
    task.delete()
    # redirect to the tasks view
    return redirect('tasks')

# Complete a task
def complete_task(request, task_id):
    # get the task as parameter
    task = Task.objects.get(id=task_id)
    task.completed = True
    # save the task
    task.save()
    # redirect to the tasks view
    return redirect('tasks')

# View all tasks
def tasks(request):
    search_term = request.GET.get('search')
    if search_term:
        tasks = Task.objects.filter(title__icontains=search_term, completed=False)
    else:
        tasks = Task.objects.filter(completed=False)
    # render the tasks
    return render(request, 'tasks.html', {'tasks': tasks})

# View all completed tasks
def completed_tasks(request):
    # get all completed tasks
    completed_tasks = Task.objects.filter(completed=True).order_by('-created_date')
    # render the completed tasks
    return render(request, 'completed_tasks.html', {'tasks': completed_tasks})

# delete  completed task
def delete_completed_task(request, task_id):
    # get the task as parameter
    task = Task.objects.get(id=task_id)
    # delete the task
    task.delete()
    # redirect to the tasks view
    return redirect('completed-tasks')

# view all tasks and completed tasks
def all_tasks(request):
    # get all tasks
    tasks = Task.objects.filter(completed=False)
    # get all completed tasks
    completed_tasks = Task.objects.filter(completed=True).order_by('-created_date')
    # render the tasks and completed tasks
    return render(request, 'all_tasks.html', {'tasks': tasks, 'completed_tasks': completed_tasks})
