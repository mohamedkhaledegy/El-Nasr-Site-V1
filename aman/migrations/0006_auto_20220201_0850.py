# Generated by Django 3.2.9 on 2022-02-01 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aman', '0005_alter_fixrequest_admen_aman'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admenaman',
            name='tag',
        ),
        migrations.AddField(
            model_name='admenaman',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='aman.Tags', verbose_name='Tag'),
        ),
    ]
