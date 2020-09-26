from django.urls import path,include
from . import views
app_name = "AuthInterceptor"

urlpatterns = [
    path("register/", views.register, name = "signup"),
    path("login/", views.sign_in, name = "signin"),
    path("logout/", views.logout_view, name = "logout"),
]