from django.db import models
import time
# Create your models here.
class PlantsInfo(models.Model):
    plant_name = models.CharField(u'名称', max_length=256)
    flora_id = models.IntegerField(u'种类ID', default=0)
    introduction = models.TextField(u'简介', blank=True, null=True)
    photo = models.ImageField(upload_to='img', null=True)
    shooting_time = models.IntegerField(u'添加时间', default=int(time.time()), editable=False)
    is_del = models.IntegerField(u'是否删除', default=0, editable=False)
    create_time = models.IntegerField(u'添加时间', default=int(time.time()), editable=False)
    update_time = models.IntegerField(u'修改时间', default=int(time.time()), editable=False)
    delete_time = models.IntegerField(u'删除时间', default=0, editable=False)
    class Meta:
        db_table = 'plants'

    plants = models.Manager()