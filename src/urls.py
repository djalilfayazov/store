from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from shop.views import *

urlpatterns = [
    path('store-admin/', admin.site.urls),
    path('', home, name='home'),

    path('products/', items, name='items'),
    path('products/item-<int:pk>/', item),

    path('register', Registration.as_view(), name='register'),
    path('register/success/', success, name='register-success'),
    
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),    
]
