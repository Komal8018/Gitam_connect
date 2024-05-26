from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_u,name='logout'),
    path("<str:slug>", views.room, name="room"),
]