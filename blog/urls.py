from django.urls import path
from blog import views

urlpatterns = [
    path("index/", views.IndexView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("post/<int:id>/", views.PostView.as_view(), name="post"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("blog/", views.BlogView.as_view(), name="blog"),
    path("base/", views.SosialMedia.as_view(), name="base"),
]