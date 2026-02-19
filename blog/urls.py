from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),   # <-- EMPTY
    path("new/slug/<slug:slug>/", views.detail, name="detail"),
    path("Updated_new_url/", views.new_url, name="new_url"),
    path("old_url/", views.old_url, name="old_url"),
    path("newAbout/", views.newAbout, name="newDetails"),
    path("contact/",views.contact,name="contact"),
    path("about/",views.about,name="about")
]
