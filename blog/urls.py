from django.urls import path
from .views import PostCreateView
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
]