from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("<int:product_id>", views.details, name="details"),
    path("category", views.category, name="category"),
    path("<str:product_category>", views.details_category, name="details_category")
]
