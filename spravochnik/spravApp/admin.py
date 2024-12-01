from django.contrib import admin
from .models import Name, Fam, Otc, Street, MainItem

for i in [Name, Fam, Otc, Street, MainItem]:
    admin.site.register(i)
# Register your models here.
