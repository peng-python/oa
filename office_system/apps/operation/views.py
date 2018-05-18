from django.shortcuts import render
from django.views.generic.base import View

from .models import ApplyModel

# Create your views here.


def apply(request):
    application = ApplyModel.objects.filter(nick_name=request.user).order_by('-id')
    context = {'application': application}
    return render(request, 'operation/RSEventApply.html', context)


# def add_apply(request):
#     post = request.POST
#     title = post.get('title', '')
#     content = post.get('content', '')
#     user = request.user
#     application = ApplyModel()
#     application.title = title
#     application.content = content
#     application.nick_name = user
#     application.save()
#     return render(request, 'operation/AddRSEventApply.html')


class Apply(View):
    """
    增加审批信息
    """
    def get(self, request):
        return render(request, 'operation/AddRSEventApply.html')

    def post(self, request):
        post = request.POST
        title = post.get('title', '')
        content = post.get('content', '')
        user = request.user
        application = ApplyModel()
        application.title = title
        application.content = content
        application.nick_name = user
        application.save()
        return render(request, 'operation/AddRSEventApply.html')


def applydetail(request, apply_id):
    application = ApplyModel.objects.get(id=int(apply_id))
    context = {'application': application}
    return render(request, 'operation/RSEventApplyDetail.html', context)