# Generated by Django 3.2.9 on 2022-02-05 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aman', '0014_visit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='اسم الفرع'),
        ),
    ]