from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.views.generic import TemplateView


urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('login',views.login,name="login"),
    path('search',views.search,name="search"),
    path('register',views.register,name="register"),
    path('home',views.home,name="home"),
    path('logout',views.logout,name="logout"),
    path('items/logout',views.ilogout,name="ilogout"),
    path('myprofile',views.myprofile,name="myprofile"),
    path('future',views.future,name="future"),
    path('log',views.log,name="log"),
    path('pass_reset',views.change_pass,name="pass_reset"),
    
    # forgot   
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='commons/password-reset/password_reset.html',
             subject_template_name='commons/password-reset/password_reset_subject.txt',
             email_template_name='commons/password-reset/password_reset_email.html',
             success_url='done/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='commons/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='commons/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='commons/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),   
]