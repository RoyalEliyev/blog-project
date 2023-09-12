from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from blog.models import BlogModel, CategoryModel, TagModel, SettingsModel, ContactModel, SosialMediaModel, CommentModel, LikeModel
from blog.api.serializers import BlogSerializer, CategorySerializer, TagSerializer, SettingsSerializer, ContactSerializer, SosialMediaSerializer, CommentSerializer, LikeSerializer


class BlogListCreateAPIView(ListCreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer

class BlogRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "id"

  
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"


class TagListCreateAPIView(ListCreateAPIView):
    queryset = TagModel.objects.all()
    serializer_class = TagSerializer

class TagRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TagModel.objects.all()
    serializer_class = TagSerializer
    lookup_field = "id"


class SettingsListCreateAPIView(ListCreateAPIView):
    queryset = SettingsModel.objects.all()
    serializer_class = SettingsSerializer

class SettingsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SettingsModel.objects.all()
    serializer_class = SettingsSerializer
    lookup_field = "id"


class ContactListCreateAPIView(ListCreateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer

class ContactRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer
    lookup_field = "id"


class SosialMediaListCreateAPIView(ListCreateAPIView):
    queryset = SosialMediaModel.objects.all()
    serializer_class = SosialMediaSerializer

class SosialMediaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SosialMediaModel.objects.all()
    serializer_class = SosialMediaSerializer
    lookup_field = "id"


class CommentListCreateAPIView(ListCreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "id"


class LikeListCreateAPIView(ListCreateAPIView):
    queryset = LikeModel.objects.all()
    serializer_class = LikeSerializer

class LikeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = LikeModel.objects.all()
    serializer_class = LikeSerializer
    lookup_field = "id"
    