# Generated by Django 2.1.15 on 2020-09-28 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_app_api', '0007_metadata_activity'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaData_Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technical_category', models.CharField(blank=True, max_length=100, null=True)),
                ('equipment_name', models.CharField(blank=True, max_length=100, null=True)),
                ('nfc_tag', models.CharField(blank=True, max_length=100, null=True)),
                ('service_interval', models.CharField(blank=True, max_length=100, null=True)),
                ('legit', models.CharField(blank=True, max_length=100, null=True)),
                ('expected_service', models.DateTimeField(blank=True, null=True)),
                ('latest_service', models.DateTimeField(blank=True, null=True)),
                ('contacts', models.CharField(blank=True, max_length=100, null=True)),
                ('longitude', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude', models.CharField(blank=True, max_length=100, null=True)),
                ('meta_data_picture', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
