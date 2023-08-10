from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/'),
    path('categories/<id:id>'),
    path('register/',views.register, name='register'),
    path('login/', views.login_site, name='login'),
    path('logout/', views.logout_site, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name="about"),
    path('create_product/', views.create_product, name='create_product'),
    path('edit_product/<slug:slug>', views.edit_product, name='edit_product'),  
    path('delete_product/<slug:slug>/', views.delete_product, name = 'delete_product'), 
    path('profile_detail/<int:profile_id>/', views.profile_detail, name='profile_detail'),
    path('login/', views.login_site, name='login_site'),
    path('logout/', views.logout_site, name='logout_site'),
]
