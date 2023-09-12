from django.urls import path
from blog.api import views

urlpatterns = [
    path("blog-list-create/", views.BlogListCreateAPIView.as_view(), name="blog-list-create"),
    path("blog-retrieve-update-delete/<int:id>/", views.BlogRetrieveUpdateDestroyAPIView.as_view(), name="blog-retrieve=update-delete"),
    path("category-list-create/", views.CategoryListCreateAPIView.as_view(), name="category-list-create"),
    path("category-retrieve-update-delete/<int:id>/", views.CategoryRetrieveUpdateDestroyAPIView.as_view(), name="category-retrieve=update-delete"),
    path("tag-list-create/", views.TagListCreateAPIView.as_view(), name="tag-list-create"),
    path("tag-retrieve-update-delete/<int:id>/", views.TagRetrieveUpdateDestroyAPIView.as_view(), name="tag-retrieve=update-delete"),
    path("settings-list-create/", views.SettingsListCreateAPIView.as_view(), name="settings-list-create"),
    path("settings-retrieve-update-delete/<int:id>/", views.SettingsRetrieveUpdateDestroyAPIView.as_view(), name="settings-retrieve=update-delete"),
    path("contact-list-create/", views.ContactListCreateAPIView.as_view(), name="contact-list-create"),
    path("contact-retrieve-update-delete/<int:id>/", views.ContactRetrieveUpdateDestroyAPIView.as_view(), name="contact-retrieve=update-delete"),
    path("sosial_media-list-create/", views.SosialMediaListCreateAPIView.as_view(), name="sosial_media-list-create"),
    path("sosial_media-retrieve-update-delete/<int:id>/", views.SosialMediaRetrieveUpdateDestroyAPIView.as_view(), name="sosial_media-retrieve=update-delete"),
    path("comment-list-create/", views.CommentListCreateAPIView.as_view(), name="comment-list-create"),
    path("comment-retrieve-update-delete/<int:id>/", views.CommentRetrieveUpdateDestroyAPIView.as_view(), name="coment-retrieve=update-delete"),
    path("like-list-create/", views.LikeListCreateAPIView.as_view(), name="like-list-create"),
    path("like-retrieve-update-delete/<int:id>/", views.LikeRetrieveUpdateDestroyAPIView.as_view(), name="like-retrieve=update-delete"),
]
