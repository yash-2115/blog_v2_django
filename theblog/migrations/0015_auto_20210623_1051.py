# Generated by Django 3.1 on 2021-06-23 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0014_auto_20210623_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=255),
        ),
    ]
