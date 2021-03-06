# Generated by Django 3.2.9 on 2022-02-06 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aman', '0024_alter_visit_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='aman.admenaman', verbose_name='انشاء بواسطة'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='date_created',
            field=models.DateTimeField(auto_now=True, verbose_name='وقت تقديم الطلب'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='date_visit',
            field=models.DateTimeField(blank=True, null=True, verbose_name='موعد الزيارة'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='aman.store', verbose_name='الفرع'),
        ),
    ]
