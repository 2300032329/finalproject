from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('',views.home,name='home'),
    path('base/',views.base,name='base'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('contactpagecall/',views.contactpagecall,name='contactpagecall'),
    path('contactlogic/',views.contactlogic,name='contactlogic'),
]