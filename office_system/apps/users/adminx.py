import xadmin
from xadmin import views
from .models import UserDetail, DivisionModel


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = '办公管理后台'
    site_footer = '版权所有'


class UserDetailAdmin(object):
    list_display = ['user', 'work_year', 'division', 'position', 'add_time']
    list_filter = ['user', 'work_year', 'division', 'position']
    search_fields = ['user', 'work_year', 'division', 'position', 'add_time']


class DivisionAdmin(object):
    list_display = ['name', 'add_time']
    list_filter = ['name', 'add_time']
    search_fields =['name', 'add_time']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(UserDetail, UserDetailAdmin)
xadmin.site.register(DivisionModel, DivisionAdmin)
