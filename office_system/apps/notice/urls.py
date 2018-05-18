from django.conf.urls import url

from notice import views


urlpatterns = [
    url(r'^category/$', views.notice_category, name='notice_category'),
    url(r'^notice_list/$', views.notice_list, name='notice_list'),
    url(r'^notice_detail/(?P<notice_id>\d+)/$', views.notice_detail, name='notice_detail'),
    # # url(r'^editstaff/(?P<user_id>\d+)/$', views.user_editstaff, name='user_editstaff'),
    # url(r'^editstaff/(?P<user_id>\d+)/$', Editstaff.as_view(), name='user_editstaff'),
    # url(r'^addstaff/$', Addstaff.as_view(), name='user_addstaff'),
]