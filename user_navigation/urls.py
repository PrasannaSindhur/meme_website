from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('complete_registration', views.complete_registration, name='complete_registration'),
    path(r'display_meme/', views.display_meme, name='display_meme'),
    path(r'logout/(?P<username>\w+/<int:flag>)', views.logout, name='logout')
]