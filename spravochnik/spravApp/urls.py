from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "spravApp"
urlpatterns = [
    path('', main, name='main' ),
    path('change/<int:ItemPK>/', mainItemChange, name='mainItemChange' ),
    path('change/<str:ParentTable>/<int:ItemPK>/', change_fk, name='fk_change' ),
    path('<str:ParentTable>/', ParentTable, name='ParentTable' ),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
