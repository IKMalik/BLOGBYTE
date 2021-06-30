from . import views
from django.urls import path

urlpatterns = [
    path('', views.homepage, name="blog-homepage"),
    path("about/", views.siteInformation, name="about")
]
