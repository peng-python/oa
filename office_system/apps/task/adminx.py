import xadmin

from .models import TaskModel, ApplyTaskModel


class TaskAdmin(object):
    list_display = ['title', 'task_man', 'state', 'urgent', 'content', 'done_time', 'time', 'add_time']
    list_filter = ['title', 'task_man', 'state', 'urgent', 'content', 'done_time', 'time']
    search_fields = ['title', 'task_man', 'state', 'urgent', 'content', 'done_time', 'time', 'add_time']
    style_fields = {'content': 'ueditor'}


class ApplyTaskAdmin(object):
    list_display = ['task', 'cause', 'time', 'state', 'leader', 'detail', 'add_time']
    list_filter = ['task', 'cause', 'time', 'state', 'leader', 'detail']
    search_fields = ['task', 'cause', 'time', 'state', 'leader', 'detail', 'add_time']


xadmin.site.register(TaskModel, TaskAdmin)
xadmin.site.register(ApplyTaskModel, ApplyTaskAdmin)