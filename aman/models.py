
from tkinter import N
from django.db import models
from django.contrib.auth import login ,logout , authenticate

from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.text import slugify

app_name = 'aman'

# Create your models here.

class Tags(models.Model):
    name_tag = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name_tag

class AdmenAman(models.Model):
    name = models.CharField(verbose_name=("الاسم"), max_length=50)
    mobile_num = models.CharField(max_length=11,  verbose_name='رقم الموبايل')
    mobile_num2 = models.CharField(verbose_name=("رقم الموبايل 2"), max_length=11, blank=True,null=True)
    email_address = models.EmailField(verbose_name=("الايميل"), blank=True,null=True)
    tag = models.ManyToManyField(Tags,verbose_name=("Tag"), blank=True)
    name_area = models.CharField(verbose_name=("اسم المنطقة"), max_length=20, blank=True, null=True)
    slug = models.SlugField(blank=True,null=True)
    
    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(AdmenAman,self).save(*args, **kwargs)
    def __str__(self):
        return self.name
class Store(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    image_store = models.ImageField(upload_to="Stores/MainPic",blank=True,null=True,verbose_name='صورة الفرع')
    monthly_visited = models.BooleanField(default=True, verbose_name='زيارة شهرية',blank=True,null=True)
    admen = models.ForeignKey("aman.AdmenAman", verbose_name=("ادمين الفرع حاليا"), on_delete=models.DO_NOTHING , blank=True,null=True)
    active = models.BooleanField(default=True, verbose_name='يعمل',blank=True,null=True)
    name_area = models.CharField(verbose_name=("اسم المنطقة"), max_length=20, blank=True, null=True)
    line = models.CharField(verbose_name=("خط السير"), max_length=50 ,blank=True, null=True)
    city = models.CharField(verbose_name=("المدينة"), max_length=50,blank=True, null=True)
    address_store = models.CharField(verbose_name=("العنوان"), max_length=1000,blank=True,null=True)
    location_store = models.CharField(max_length=1000, verbose_name="الموقع",blank=True,null=True)
    tag = models.ManyToManyField(Tags,verbose_name=("Tag"), blank=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Store,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

class FixRequest(models.Model):
    
    emergency_type = (
        ("Urgent","Urgent"),
        ("Important","Important"),
        ("Postpone","Postpone")
       )
    short_desc = models.CharField(max_length=200 ,verbose_name='وصف قصير للمشكلة')
    store = models.ForeignKey(Store ,verbose_name='الفرع',null=True, blank=True, on_delete=models.SET_NULL)
    admen_aman = models.ForeignKey(AdmenAman, verbose_name='الادمن المسئول' , on_delete=models.SET_NULL,null=True,blank=True)
    date_created = models.DateTimeField(auto_now=True,verbose_name='تايخ الطلب')
    date_modified = models.DateTimeField(auto_now_add=True,verbose_name='اخر تعديل')
    monthly_visited = models.BooleanField(default=True, verbose_name='مع الزيارة الشهرية')
    emergency = models.CharField(max_length=100,blank=True, null=True,verbose_name='درجة الأهمية',choices=emergency_type)
    slug = models.SlugField(blank=True, null=True)
    
    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.short_desc)
        super(FixRequest,self).save(*args, **kwargs)

    def __str__(self):
        return self.short_desc[:15]