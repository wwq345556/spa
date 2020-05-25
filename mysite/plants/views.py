from base import common
from . import models
from django.forms.models import model_to_dict
from django.core import serializers
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
    # print('http'+str(tmp_data.photo))
    # tmp_data.photo = str(tmp_data.photo)
    #data = model_to_dict(tmp_data)
    json_data = serializers.serialize("json",tmp_data)
    data = json.loads(json_data)
    return common.success(data)
