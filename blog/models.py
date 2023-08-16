from django.db import models
from django.contrib.auth.models import User

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class TagModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.user


class SettingsModel(models.Model):
    logo = models.ImageField(upload_to="posters/")
    abaut_us = models.TextField(blank=True, null=True)
    phone_nuber = models.CharField(max_length=50)
    email = models.EmailField()
    adress = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "Settings"
    
    def __str__(self):
        return self.abaut_us


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    subject = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
    
    def __str__(self):
        return self.name


class SosialMediaModel(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=100)
    
    class Meta:
        verbose_name = "Sosial Media"
        verbose_name_plural = "Sosial Medias"
    
    def __str__(self):
        return self.name


class BlogModel(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(CategoryModel, related_name="blogs", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="used_blogs")
    pub_date = models.DateField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(TagModel, related_name="blogs", blank=True, null=True)
    poster = models.ImageField("posters/", blank=True, null=True)
    title = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.user.username


class CommentModel(models.Model):
    content = models.TextField()
    pub_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name="blog_comments")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.user.username
    

class LikeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name="blog_likes")

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"

    def __str__(self):
        return self.user.username

class AboutModel(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField()