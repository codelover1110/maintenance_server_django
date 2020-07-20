from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100,)
    age = models.IntegerField()
    gender = models.CharField(max_length=30,)

class ShopData(models.Model):
    nfc_uid = models.CharField(max_length=100, null=True, blank=True)
    nfc_store_id = models.CharField(max_length=100, null=True, blank=True)
    store_name = models.CharField(max_length=100, null=True, blank=True)
    store_address = models.CharField(max_length=100, null=True, blank=True)
    store_postcode = models.CharField(max_length=100, null=True, blank=True)
    stroe_city = models.CharField(max_length=100, null=True, blank=True)
    store_picture = models.ImageField(max_length=100, null=True, blank=True, upload_to='')
    longtitude = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)

class AdminUser(models.Model):
    email = models.CharField(max_length=100, null=True, blank=True)
    user_name = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)

class VoteData(models.Model):
    customer_email = models.CharField(max_length=100, null=True, blank=True)
    vote_name = models.CharField(max_length=100, null=True, blank=True)
    vote = models.CharField(max_length=100, null=True, blank=True)
    nfc_store_id = models.CharField(max_length=100, null=True, blank=True)
    election = models.CharField(max_length=100, null=True, blank=True)
    shop_name = models.CharField(max_length=100, null=True, blank=True)
    longtitude = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    
class MetaData(models.Model):
    tag_id = models.CharField(max_length=100, null=True, blank=True)
    nfc_tag = models.CharField(max_length=100, null=True, blank=True)
    media_type = models.CharField(max_length=100, null=True, blank=True)
    energy_media_type = models.CharField(max_length=100, null=True, blank=True)
    meter_point_description = models.CharField(max_length=100, null=True, blank=True)
    energy_unit = models.CharField(max_length=100, null=True, blank=True)
    group = models.CharField(max_length=100, null=True, blank=True)
    column_line = models.CharField(max_length=100, null=True, blank=True)
    meter_location = models.CharField(max_length=100, null=True, blank=True)
    energy_art = models.CharField(max_length=100, null=True, blank=True)
    supply_area_child = models.CharField(max_length=100, null=True, blank=True)
    meter_level_structure = models.CharField(max_length=100, null=True, blank=True)
    supply_area_parent = models.CharField(max_length=100, null=True, blank=True)
    meta_data_picture = models.ImageField(max_length=100, null=True, blank=True, upload_to='')
    longtitude = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)

class DegreeDay(models.Model):
    name_of_degree = models.CharField(max_length=100, null=True, blank=True)
    period_form = models.CharField(max_length=100, null=True, blank=True)
    period_to = models.CharField(max_length=100, null=True, blank=True)
    month = models.CharField(max_length=100, null=True, blank=True)
    degree_days = models.CharField(max_length=100, null=True, blank=True)

class Consumption(models.Model):
    tag_id = models.CharField(max_length=100, null=True, blank=True)
    nfc_tag = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    consumption = models.CharField(max_length=100, null=True, blank=True)
    unit = models.CharField(max_length=100, null=True, blank=True)

class ConsumptionMobile(models.Model):
    tag_id = models.CharField(max_length=100, null=True, blank=True)
    last_reading_date = models.DateTimeField(null=True,blank=True)
    new_reading_date = models.DateTimeField(null=True,blank=True)
