from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('general',views.general,name="general"),
    path('ccr',views.ccr,name="ccr")
]