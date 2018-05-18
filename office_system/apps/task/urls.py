from django.conf.urls import url

from task import views


urlpatterns = [
    url(r'^list/$', views.task_list, name='task_list'),
    url(r'^result_list/$', views.result_list, name='result_list'),
    url(r'^task_detail/(?P<task_id>\d+)/$', views.task_detail, name='task_detail'),
    url(r'^task_done/(?P<task_id>\d+)/$', views.task_done, name='task_done'),
    url(r'^task_up/(?P<task_id>\d+)/$', views.task_up, name='task_up'),
    # url(r'^task_delaylist/$', views.task_delaylist, name='task_delaylist'),
    # url(r'^task_delaydetail/(?P<task_id>\d+)/$', views.task_delaydetail, name='task_delaydetail'),
    # url(r'^task_adddelay/$', views.task_adddelay, name='task_adddelay'),
]