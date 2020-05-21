from django.db import models
import time
# Create your models here.
class FloraInfo(models.Model):
    pid = models.IntegerField(u'上级名称', default=0)
    flora_name = models.CharField(u'名称', max_length=256)
    introduction = models.TextField(u'简介', blank=True, null=True)
    pid_tree = models.CharField(u'祖先树', max_length=100)
    is_del = models.IntegerField(u'是否删除', default=0, editable=False)
    create_time = models.IntegerField(u'添加时间', default=int(time.time()), editable=False)
    update_time = models.IntegerField(u'修改时间', default=int(time.time()), editable=False)
    delete_time = models.IntegerField(u'删除时间', default=0, editable=False)
    class Meta:
        db_table = 'flora'

    flora = models.Manager()

