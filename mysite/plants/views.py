from base import common
from . import models
from django.forms.models import model_to_dict
from django.core import serializers
import time
# Create your views here.

def plants_add(request):
    plant_name = request.POST.get('plant_name')
    flora_id = request.POST.get('flora_id')
    introduction = request.POST.get('introduction','')
    photo = request.FILES.get('file')
    shooting_time = request.POST.get('shooting_time')
    plant = models.PlantsInfo(plant_name = plant_name,flora_id = flora_id,introduction = introduction,photo = photo,shooting_time = shooting_time)
    plant.save()
    return common.success()

def plants_info(request):
    id = request.POST.get('id')
    tmp_data = models.PlantsInfo.plants.get(id = id)
    # print('http://127.0.0.1:8000/media/img/'+str(tmp_data.photo))
    data = {}
    data['id'] = tmp_data.id
    data['plant_name'] = tmp_data.plant_name
    data['flora_id'] = tmp_data.flora_id
    data['introduction'] = tmp_data.introduction
    data['photo'] = 'http://127.0.0.1:8000/media/'+str(tmp_data.photo)
    data['shooting_time'] = tmp_data.shooting_time

    return common.success(data)

def plants_delete(request):
    id = request.POST.get('id')

    data = models.PlantsInfo.plants.get(id = id)
    data.is_del = 1
    data.delete_time = time.time()
    data.save()
    return common.success()

def plants_update(request):
    id = request.POST.get('id')
    plant_name = request.POST.get('plant_name')
    flora_id = request.POST.get('flora_id')
    introduction = request.POST.get('introduction', '')
    photo = request.FILES.get('file',0)
    shooting_time = request.POST.get('shooting_time')
    data = models.PlantsInfo.plants.get(id = id)
    data.plant_name = plant_name
    data.flora_id = flora_id
    data.introduction = introduction
    data.shooting_time = shooting_time
    if photo :
        data.photo = photo
    data.update_time = time.time()
    data.save()
    return common.success()

def plants_list(request):
    flora_id = request.POST.get('flora_id')
    page = request.POST.get('page',1)
    limit = request.POST.get('limit',20)
    total = models.PlantsInfo.plants.filter(is_del=0, flora_id=flora_id).count()

    data = common.paging(page,limit,total)
    ret = models.PlantsInfo.plants.filter(is_del = 0,flora_id = flora_id).values()[data.get('offset'):data.get('offset') + data.get('size')]
    tmp_data = list(ret)
    data = {}
    data['list'] = tmp_data
    data['total'] = total
    return common.success(data)