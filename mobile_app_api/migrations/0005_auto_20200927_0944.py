# Generated by Django 2.1.15 on 2020-09-27 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_app_api', '0004_metadata_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadata_main',
            name='expected_service',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metadata_main',
            name='latest_service',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
