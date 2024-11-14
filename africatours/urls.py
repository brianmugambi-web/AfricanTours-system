from django.urls import path
from .import views

#define a list of the url
urlpatterns=[
    path('',views.index)
]
