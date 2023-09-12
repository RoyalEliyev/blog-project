from rest_framework import serializers
from blog.models import BlogModel, CategoryModel, TagModel, SettingsModel, ContactModel, SosialMediaModel, CommentModel, LikeModel

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogModel
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = TagModel
        fields = "__all__"


class SettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SettingsModel
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactModel
        fields = "__all__"


class SosialMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = SosialMediaModel
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentModel
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = LikeModel
        fields = "__all__"