from django.contrib import admin
from .models import Name, Fam, Otc, Street, MainItem, Phones

for i in [Name, Fam, Otc, Street, MainItem, Phones]:
    admin.site.register(i)
# Register your models here.
