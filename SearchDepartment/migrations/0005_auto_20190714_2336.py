# Generated by Django 2.2.3 on 2019-07-14 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SearchDepartment', '0004_auto_20190714_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='AdministrativeDistrict',
            field=models.CharField(max_length=17),
        ),
        migrations.AlterField(
            model_name='department',
            name='TypeOfDefect',
            field=models.CharField(max_length=68),
        ),
    ]
