from django.contrib import admin
from .models import ShopData
from .models import User

# Register your models here.
admin.site.register(ShopData)
admin.site.register(User)