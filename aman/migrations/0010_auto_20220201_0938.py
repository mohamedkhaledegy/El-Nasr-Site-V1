# Generated by Django 3.2.9 on 2022-02-01 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aman', '0009_auto_20220201_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admenaman',
            name='tag',
            field=models.ManyToManyField(blank=True, to='aman.Tags', verbose_name='Tag'),
        ),
        migrations.AlterField(
            model_name='store',
            name='location_store',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='الموقع'),
        ),
        migrations.AlterField(
            model_name='store',
            name='tag',
            field=models.ManyToManyField(blank=True, to='aman.Tags', verbose_name='Tag'),
        ),
    ]