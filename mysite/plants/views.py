from base import common
from . import models
from django.forms.models import model_to_dict
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
