from django.urls import path
from .import views

urlpatterns = [
        path('', views.UserView, name='home'),
        path('create/', views.Addusers, name= 'Addusers'),
        path('all/', views.Readusers, name='Viewusers'),
        path('read/<int:pk>/', views.Readuser, name='Readuser'),
        path('update/<int:pk>/', views.Updateusers, name='Updateusers'),
        path('users/<int:pk>/delete/', views.Deleteusers, name='Deleteusers')
]
