# Generated by Django 3.2.9 on 2022-02-01 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aman', '0003_alter_fixrequest_emergency'),
    ]

    operations = [
        migrations.AddField(
            model_name='admenaman',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fixrequest',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='store',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
