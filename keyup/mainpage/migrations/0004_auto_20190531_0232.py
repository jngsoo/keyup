# Generated by Django 2.1.5 on 2019-05-30 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_timegraph_1_timegraph_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='timegraph_1',
            name='company_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timegraph_2',
            name='company_name',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
