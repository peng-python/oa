from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import TaskModel, ApplyTaskModel

# Create your views here.


def task_list(request):
    tasks = TaskModel.objects.all().filter(task_man=request.user)

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(tasks, 5, request=request)

    tasks = p.page(page)

    context = {'tasks': tasks}
    return render(request, 'task/tasklist.html', context)


def task_detail(request, task_id):
    task = TaskModel.objects.get(id=int(task_id))
    post = request.POST
    state = post.get('state', '')
    if state == '':
        return render(request, 'task/taskdetail.html', {'task': task})
    else:
        task.state = state
        task.save()
        # return render(request, result_list)
        return HttpResponseRedirect(reverse('task:task_list'))


def result_list(request):
    tasks = TaskModel.objects.filter(task_man=request.user)
    context = {'tasks': tasks}
    return render(request, 'task/taskresultlist.html', context)


def task_done(request, task_id):
    task = TaskModel.objects.get(id=int(task_id))
    post = request.POST
    state = post.get('state', '')
    if state == '':
        return render(request, 'task/taskdone.html', {'task': task})
    else:
        task.state = state
        task.save()
        return HttpResponseRedirect(reverse('task:result_list'))


def task_up(request, task_id):
    task = TaskModel.objects.get(id=int(task_id))
    if request.method == 'POST':
        f1 = request.FILES['file1']
        fname = '%s/task/file/%s' % (settings.MEDIA_ROOT, f1.name)
        with open(fname, 'wb') as f:
            for c in f1.chunks():
                f.write(c)
        return HttpResponseRedirect(reverse('task:result_list'))
    else:
        return render(request, 'task/TaskResultUp.html', {'task': task})


# def task_delaylist(request):
#     apply_tasks = ApplyTaskModel.objects.filter(task__task_man=request.user)
#     context = {'apply_tasks': apply_tasks}
#     return render(request, 'task/DelayTaskList.html', context)
#
#
# def task_delaydetail(request, task_id):
#     apply_detail = ApplyTaskModel.objects.get(id=int(task_id))
#     context = {'apply_detail': apply_detail}
#     return render(request, 'task/DelayTaskDetail.html', context)
#
#
# def task_adddelay(request):
#     tasks = TaskModel.objects.filter(task_man=request.user, state='not')
#
#     if request.method == 'POST':
#         post = request.POST
#         title1 = post.get('textfield2', '')
#         task = TaskModel.objects.get(title=str(title1))
#         try:
#             time = post.get('textfield1', '')
#             cause = post.get('textfield3', '')
#             task1 = ApplyTaskModel.objects.get(task_id=task.id)
#             task1.time = time
#             task1.cause = cause
#             task1.task = task
#             task1.save()
#             # return render(request, 'task/AdddelayTask.html', context)
#             return render(request, 'task/AdddelayTask.html')
#         except:
#             return render(request, 'task/AdddelayTask.html')
#     else:
#         return render(request, 'task/AdddelayTask.html')
#     # context = {'tasks': tasks}
#     # return render(request, 'task/AdddelayTask.html', context)