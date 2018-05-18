import xadmin
from .models import ApplyModel


class ApplyAdmin(object):
    list_display = ['title', 'content', 'file', 'is_examine', 'add_time']
    list_filter = ['title', 'content', 'file', 'is_examine', 'add_time']
    search_fields = ['title', 'content', 'file', 'is_examine', 'add_time']


xadmin.site.register(ApplyModel, ApplyAdmin)