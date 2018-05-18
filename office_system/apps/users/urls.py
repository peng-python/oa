from django.conf.urls import url
from users import views
from users.views import Editstaff, Addstaff
# import views


urlpatterns = [
    url(r'index/$', views.user_index, name='user_index'),
    url(r'^personnel/$', views.user_personnel, name='user_personnel'),
    url(r'^staffdetail/(?P<user_id>\d+)/$', views.user_staffdetail, name='user_staffdetail'),
    # url(r'^editstaff/(?P<user_id>\d+)/$', views.user_editstaff, name='user_editstaff'),
    url(r'^editstaff/(?P<user_id>\d+)/$', Editstaff.as_view(), name='user_editstaff'),
    url(r'^addstaff/$', Addstaff.as_view(), name='user_addstaff'),
]