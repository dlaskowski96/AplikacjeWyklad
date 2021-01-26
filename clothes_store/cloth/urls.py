from django.urls import path
from . import views

urlpatterns = [
    path('cloth',views.clothList.as_view(), name=views.clothList.name),
    path('cloth/<int:pk>',views.clothDetail.as_view(), name=views.clothDetail.name),
    path('Client', views.ClientList.as_view(), name=views.ClientList.name),
    path('Client/<int:pk>', views.ClientDetail.as_view(), name=views.ClientDetail.name),
    path('users', views.UserList.as_view(), name=views.UserList.name),
    path('users/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    ]
