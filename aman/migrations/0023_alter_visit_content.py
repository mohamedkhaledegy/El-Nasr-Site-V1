# Generated by Django 3.2.9 on 2022-02-05 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aman', '0022_alter_visit_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='content',
            field=models.ManyToManyField(blank=True, to='aman.Item', verbose_name='الوحدة'),
        ),
    ]
