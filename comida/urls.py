from django.contrib import admin
from django.urls import path
from comida.views import menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu, name='menu'),
]
