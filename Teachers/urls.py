# This is the teachers app urls file. N\B It must not contain any reference to the admin
# It is advisable that each app ti have its own default app.


from django.urls import path
# From this directory import views.py file, which contains the functions
from . import views

urlpatterns = [
    path("", views.default),
    path("about", views.about),
    path("services", views.services)
]
