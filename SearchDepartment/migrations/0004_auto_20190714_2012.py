# Generated by Django 2.2.3 on 2019-07-14 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SearchDepartment', '0003_auto_20190713_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestimage',
            name='Image',
            field=models.FileField(upload_to='request_images'),
        ),
    ]
