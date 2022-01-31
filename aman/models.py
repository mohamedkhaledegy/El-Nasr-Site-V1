from email.policy import default
from django.db import models



# Create your models here.

class Tags(models.Model):
    name_tag = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.name_tag

class AdmenAman(models.Model):
    name = models.CharField(verbose_name=("الاسم"), max_length=50)
    mobile_num = models.CharField(max_length=11, default=0, verbose_name='رقم الموبايل')
    mobile_num2 = models.CharField(verbose_name=("رقم الموبايل 2"), max_length=11, blank=True,null=True)
    location_tag = models.ForeignKey(Tags,on_delete=models.DO_NOTHING)
    name_area = models.CharField(verbose_name=("اسم المنطقة"), max_length=20)
    
    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    image_store = models.ImageField(upload_to="Stores/MainPic",blank=True,verbose_name='صورة الفرع')
    monthly_visited = models.BooleanField(default=True, verbose_name='زيارة شهرية')
    name_area = models.CharField(verbose_name=("اسم المنطقة"), max_length=20)
    active = models.BooleanField(default=True, verbose_name='يعمل')
    def __str__(self):
        return self.name

class FixRequest(models.Model):
    short_desc = models.CharField(max_length=200 ,verbose_name='وصف قصير للمشكلة')
    store = models.ForeignKey(Store ,verbose_name='الفرع',null=True, blank=True, on_delete=models.SET_NULL)
    admin = models.CharField(max_length=200 ,verbose_name='الادمن المسئول')
    date_created = models.DateTimeField(auto_now=True,verbose_name='تايخ الطلب')
    date_modified = models.DateTimeField(auto_now_add=True,verbose_name='اخر تعديل')
    monthly_visited = models.BooleanField(default=True, verbose_name='مع الزيارة الشهرية')
    emergency = models.CharField(max_length=100,blank=True, null=True,verbose_name='درجة الأهمية')
    
    def __str__(self):
        return self.short_desc[:10]