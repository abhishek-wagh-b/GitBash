from django.urls import path
from . import views


urlpatterns=[
    path("blogposts/", views.BlogpostView.as_view(), name="blogpost_view"),
    path("blogposts/<int:pk>",views.Blogpostupdatedestry.as_view(), name="update")
]
