import xadmin

from .models import NoticeModel, CategoryModel


class CategoryAdmin(object):
    list_display = ['name', 'add_time']
    list_filter = ['name']
    search_fields = ['name', 'add_time']


class NoticeAdmin(object):
    list_display = ['title', 'subject', 'content', 'author', 'add_time']
    list_filter = ['title', 'subject', 'content', 'author']
    search_fields = ['title', 'subject', 'content', 'author', 'add_time']
    style_fields = {'content': 'ueditor'}


xadmin.site.register(CategoryModel, CategoryAdmin)
xadmin.site.register(NoticeModel, NoticeAdmin)