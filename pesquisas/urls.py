from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dizeroi', views.dizer_oi, name='dizer_oi'),
    path('somarnumeros', views.somar_numeros, name='somar_numeros'),

]
