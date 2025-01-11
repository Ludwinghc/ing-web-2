from django.urls import path
from . import views


urlpatterns = [ 
    path("newOutfit/", views.newOutfit, name="newOutfit"),
    path("verOutfit/", views.verOutfit, name="verOutfit"),
    path("calendarOutfit/", views.calendar_view, name="calendarOutfit"),


]