import time
from base import common
from . import models
from django.forms.models import model_to_dict


# Create your views here.
def hello(request):
    return HttpResponse("Hello,world")

def orm(request):
    return HttpResponse("orm")

def flora_info(request):
    id = request.POST.get("id",0)
    ret = models.FloraInfo.flora.get(id = id)
    data = model_to_dict(ret)
    return common.success(data)

def flora_add(request):
    pid = request.POST.get("pid")
    flora_name = request.POST.get("flora_name")
    introduction = request.POST.get("introduction",'')
    if pid == 0:
        pid_tree = '0'
    else:
        temp = models.FloraInfo.flora.get(id=pid)
        pid_tree = str(temp.pid_tree) + ':' + str(temp.id)
        # print(temp.pid_tree)
    flora = models.FloraInfo(pid=pid,flora_name=flora_name,introduction=introduction,pid_tree=pid_tree)
    flora.save()
    return common.success()

def flora_list(request):
    ret = models.FloraInfo.flora.filter(is_del=0).values()
    data = list(ret)
    return common.success(data)

def flora_update(request):
    id = request.POST.get("id")
    introduction = request.POST.get("introduction", '')
    flora_name = request.POST.get("flora_name")
    data = models.FloraInfo.flora.get(id = id)
    data.flora_name = flora_name
    data.introduction = introduction
    data.update_time = time.time()
    data.save()
    return common.success()

def flora_delete(request):
    id = request.POST.get("id")
    #下面有未删除children,则无法删除
    tmpData = models.FloraInfo.flora.filter(pid=id,is_del=0).values()
    if tmpData.exists():
        return common.error('不能删除该分类')

    data = models.FloraInfo.flora.get(id=id)
    data.is_del = 1
    data.delete_time = time.time()
    data.save()
    return common.success()
# def page_not_found(request,exception,template_name='testapp/404.html'):
# 	return render(request,template_name)

