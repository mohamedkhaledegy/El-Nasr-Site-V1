# Generated by Django 3.2.9 on 2022-02-05 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aman', '0021_alter_store_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='content',
            field=models.ManyToManyField(blank=True, db_column='name', to='aman.Item', verbose_name='الوحدة'),
        ),
    ]