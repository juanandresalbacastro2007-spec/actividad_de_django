from django.urls import path # acceder a las urls
from . import views # acceder a las vistas
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'), 
    path('hojas/', views.hojas, name='hojas'), 
    path('hojas/crearh/', views.crearh, name='crearh'), 
    path('hojas/editarh/<int:id>/', views.editarh, name='editarh'), 
    path('editar/<int:id>',views.editarh, name='editarh'),
    path('eliminar/<int:id>',views.eliminarh, name='eliminarh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 