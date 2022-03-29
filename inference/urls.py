from django.urls import path
from . import views

urlpatterns = [
    path('inference/', views.PostView.as_view(), name= 'inference'),
]