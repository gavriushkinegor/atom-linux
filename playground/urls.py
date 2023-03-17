from django.urls import path
from .views import home

#URLConf
urlpatterns = [
    path('home/', home, name = 'home'),
]