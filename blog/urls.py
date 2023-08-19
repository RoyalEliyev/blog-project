from django.urls import path
from blog import views

urlpatterns = [
    path("index/", views.IndexView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("post/", views.PostView.as_view(), name="post"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("detail/", views.DetailView.as_view(), name="detail"),
    path("blog/", views.BlogView.as_view(), name="blog"),
]