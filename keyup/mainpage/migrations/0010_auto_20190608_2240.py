# Generated by Django 2.1.5 on 2019-06-08 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0009_auto_20190608_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timegraph',
            name='time',
            field=models.CharField(choices=[('1', '2019 1월'), ('2', '2019 2월'), ('3', '2019 3월'), ('4', '2019 4월'), ('5', '2019 5월'), ('6', '2019 6월')], max_length=2),
        ),
    ]
