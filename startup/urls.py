from django.urls import path, re_path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    re_path("send_data/", views.search, name="search"),
    path("createdata", views.createdata, name="createdata"),
    path("addnew", views.add_new, name="addnew"),
]
