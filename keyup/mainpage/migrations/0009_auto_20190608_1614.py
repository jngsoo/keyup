# Generated by Django 2.1.5 on 2019-06-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0008_auto_20190606_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='dummy_for_histo_and_cloud',
            name='related_keyword_1',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dummy_for_histo_and_cloud',
            name='related_keyword_2',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dummy_for_histo_and_cloud',
            name='related_keyword_3',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dummy_for_histo_and_cloud',
            name='related_keyword_4',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dummy_for_histo_and_cloud',
            name='related_keyword_5',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
    ]
