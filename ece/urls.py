from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('photo/', views.photo, name='photo'),
    path('base/', views.base, name='base'),
    path('homepage/', views.homepage, name='homepage'),
    path('UserRegisterPageCall/', views.UserRegisterPageCall, name='UserRegisterPageCall'),
    path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
  ]