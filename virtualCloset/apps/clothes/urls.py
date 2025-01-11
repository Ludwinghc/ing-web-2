from django.urls import path
from . import views


urlpatterns = [ 
    path("newClothes/", views.newClothes, name="newClothes"),
    path("verClothes/", views.verClothes, name="verClothes"),
    path("formularioActualizar/<str:ID_CLOTHES>/", views.FormularioClothes, name='FormularioActualizar'),
    path("Actualizar/<str:ID_CLOTHES>/", views.actualizarClothes, name='Actualizar'),

]