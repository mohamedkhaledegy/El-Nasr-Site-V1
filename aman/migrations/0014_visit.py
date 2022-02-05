# Generated by Django 3.2.9 on 2022-02-04 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aman', '0013_admenaman_email_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of', models.CharField(blank=True, choices=[('شهرية', 'شهرية'), ('طارئة', 'طارئة'), ('شهرية-تكميلية', 'شهرية-تكميلية'), ('معاينة', 'معاينة')], max_length=100, null=True, verbose_name='نوع الزيارة')),
                ('short_desc', models.CharField(blank=True, max_length=300, null=True, verbose_name='ملخص المشكلة')),
                ('describe_proplem', models.TextField(blank=True, max_length=3000, null=True, verbose_name='وصف المشكلة')),
                ('done', models.BooleanField(default=False)),
                ('argent', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now=True, verbose_name='تايخ تقديم الطلب')),
                ('date_visit', models.DateTimeField(blank=True, null=True, verbose_name='تاريخ الزيارة')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aman.admenaman', verbose_name='انشاء بواسطة')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aman.store', verbose_name='الفرع')),
            ],
        ),
    ]
