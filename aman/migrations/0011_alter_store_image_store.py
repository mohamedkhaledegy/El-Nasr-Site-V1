# Generated by Django 3.2.9 on 2022-02-01 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aman', '0010_auto_20220201_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='image_store',
            field=models.ImageField(blank=True, null=True, upload_to='Stores/MainPic', verbose_name='صورة الفرع'),
        ),
    ]