from django.conf.urls import url
from operation import views
from operation.views import Apply


urlpatterns = [
    url(r'detail/(?P<apply_id>\d+)/$', views.applydetail, name='apply_detail'),
    url(r'add_apply/$', Apply.as_view(), name='add_apply'),
    url(r'^apply/$', views.apply, name='apply'),
    # url(r'^staffdetail/(?P<user_id>\d+)/$', views.user_staffdetail, name='user_staffdetail'),
    # # url(r'^editstaff/(?P<user_id>\d+)/$', views.user_editstaff, name='user_editstaff'),
    # url(r'^editstaff/(?P<user_id>\d+)/$', Editstaff.as_view(), name='user_editstaff'),
    # url(r'^addstaff/$', Addstaff.as_view(), name='user_addstaff'),
]