from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.conf.urls import url
from .views import LoginView,ProfileView,Signupview,LogoutView,DeleteUser

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('profile/',ProfileView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('deleteuser/',DeleteUser.as_view())
    # path('springboard/', GetMenu.as_view())

]