from django.db import models
import pymysql
import time
from django.db.models.query import QuerySet
from django.utils import timezone
# class SoftDeleteQuerySet(QuerySet):
#     def delete(self):
#         self.update(delete_time=timezone.now())

# Create your models here.
class Flora(models.Model):
    #查询所有可选id
    sql = "select id,flora_name from base_flora where is_del = 0"
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123456",
                           database="spa", charset="utf8")
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()

    alldata = data + (('0','植物'),)
    cursor.close()
    conn.close()
    #pid = models.CharField(u'上级名称', max_length=10, choices=(('0', '植物'), ('2', '女')),default=0)
    pid = models.CharField(u'上级名称', max_length=100, choices=alldata, default=0)
    flora_name = models.CharField(u'名称', max_length=256)
    introduction = models.TextField(u'简介',blank=True,null=True)
    pid_tree = models.TextField(u'简介1',blank=True,null=True)
    is_del = models.IntegerField(u'是否删除', default=0,editable=False)
    create_time = models.IntegerField(u'添加时间', default=int(time.time()),editable=False)
    update_time = models.IntegerField(u'修改时间',default=int(time.time()),editable=False)
    delete_time = models.IntegerField(u'删除时间', default=0,editable=False)

    # def getPersonDropDownList(self):
    #     return tuple([(0, '无')] + list(Flora.objects.values_list('id', 'flora_name')))
    def delete(self, using=None, keep_parents=False):
        self.is_del = 1
        self.delete_time = int(time.time())
        super(Flora, self).save()
