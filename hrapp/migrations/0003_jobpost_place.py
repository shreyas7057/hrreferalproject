# Generated by Django 2.2 on 2020-10-09 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrapp', '0002_auto_20200916_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='place',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]