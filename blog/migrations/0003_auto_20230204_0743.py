# Generated by Django 3.2 on 2023-02-04 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230204_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='img'),
        ),
        migrations.AlterField(
            model_name='contentimageblog',
            name='image',
            field=models.ImageField(upload_to='img'),
        ),
    ]
