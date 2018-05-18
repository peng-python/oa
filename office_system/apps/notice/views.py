from django.shortcuts import render

from .models import CategoryModel, NoticeModel

# Create your views here.


def notice_category(request):
    categorys = CategoryModel.objects.all().order_by('-id')
    context = {'categorys': categorys}
    return render(request, 'notice/NoticeCategory.html', context)


def notice_list(request):
    notices = NoticeModel.objects.all().order_by('-id')
    context = {'notices': notices}
    return render(request, 'notice/NoticeShow.html', context)


def notice_detail(request, notice_id):
    detail = NoticeModel.objects.get(id=int(notice_id))
    context = {'detail': detail}
    return render(request, 'notice/NoticeDetail.html', context)