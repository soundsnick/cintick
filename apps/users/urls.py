from django.urls import path
from . import views

urlpatterns = [
    path('sign_in/', views.sign_in_template, name="sign_in"),
    path('sign_up/', views.sign_up_template, name="sign_up"),
    path('login/', views.sign_in, name="login"),
    path('register/', views.sign_up, name="register"),
    path('logout/', views.log_out, name="logout"),
]
