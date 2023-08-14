from django.urls import path
from . import views

urlpatterns = [
    path('class/',views.about_me),
    path('', views.landing),
]