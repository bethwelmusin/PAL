from django.urls import path, include
from . import views

appname = 'CRM'
urlpatterns=[
    path('', views.home_view, name='index'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('register/',views.register_view,name='register'),
    path('user_login/',views.user_login,name='loginpage'),
    #path("logout", views.logout_request, name="logout"),

]                                                             
