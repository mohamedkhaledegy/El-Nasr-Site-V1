# Generated by Django 3.2.9 on 2022-02-06 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aman', '0027_alter_profile_stores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='stores',
            field=models.ManyToManyField(blank=True, null=True, to='aman.Store', verbose_name='الفروع المسئول عنها'),
        ),
    ]
