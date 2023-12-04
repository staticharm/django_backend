from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.homepage,name="homepage" ),
    path("<series>", views.series, name="series"),
    path("<series>/<article>", views.article, name="article"),
    path("error/",views.error,name="error")
    
]
