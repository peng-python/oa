from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.core.urlresolvers import reverse

from django.contrib.auth import get_user_model
from .models import UserDetail, UserProfile
from .forms import LoginFrom

User = get_user_model()

# Create your views here.


def login_user(request):
    login_form = LoginFrom(request.POST)
    if login_form.is_valid():
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('users:user_index'))
            else:
                return render(request, 'users/login.html')
        else:
            return render(request, 'users/login.html')
    else:
        return render(request, 'users/login.html')
    # return render(request, 'users/login.html')


def user_index(request):
    return render(request, 'users/index.html')


def user_personnel(request):
    """
    员工列表
    """
    workers = UserDetail.objects.all().order_by('-id')
    context = {'workers': workers}
    return render(request, 'users/personnel/personnel.html', context)


def user_staffdetail(request, user_id):
    """
    员工详情
    """
    if not request.user.is_authenticated():
        return render(request, 'users/login.html')
    worker = UserDetail.objects.get(id=int(user_id))
    context = {'worker': worker}
    return render(request, 'users/personnel/staffdetail.html', context)


class Editstaff(View):
    """
    修改员工信息
    """
    def get(self, request, user_id):
        worker = UserDetail.objects.get(id=int(user_id))
        context = {'worker': worker}
        return render(request, 'users/personnel/editStaff.html', context)

    def post(self, request, user_id):
        post = request.POST
        nick_name = post.get('Text1', '')
        user = UserDetail.objects.get(id=int(user_id))
        user.user.nick_name = nick_name
        user.save()
        context = {'worker': user}
        return render(request, 'users/personnel/editStaff.html', context)


# def user_addstaff(request):
#     post = request.POST
#     nick_name = post.get('Text1', '')
#     user = UserDetail()
#     user.user.nick_name = nick_name
#     user.save()
#     context = {'worker': user}
#     return render(request, 'users/personnel/AddStaff.html', context)


class Addstaff(View):
    """
    增加员工
    """
    def get(self, request):
        return render(request, 'users/personnel/AddStaff.html')

    # def post(self, request):
    #     post = request.POST
    #     birthday = post.get('Text2', '')
    #     worker = UserDetail()
    #     worker.birthday = birthday
    #
    #     worker.save()
    #     context = {'worker': worker}
    #     return render(request, 'users/personnel/personnel.html', context)


def page_not_found(request):
    # 全局404处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response