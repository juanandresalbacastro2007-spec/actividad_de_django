from django.urls import path #acceder a las urls
from . import views #acceder a las vistas
urlpatterns=[
    path('',views.inicio,name='inicio'),
    path('nosotros',views.nosotros, name='nosotros'),
    path('hojas',views.hojas, name='hojas'), #la funcion es la deviews.hojas
    path('hojas/crear',views.crearh, name='crearh'), #no se repita la url de hojas, se agrega hojas/crear
    path('hojas/editar',views.editarh, name='editarh'),
    ]